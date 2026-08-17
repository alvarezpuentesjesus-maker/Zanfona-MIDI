from dependencias.fenciones import *

class Cuerda:

    def __init__(self, tipo, tono_base, canal):
        """
        tipo: Tipo de cuerda "cantora", "bordon", "trompeta", "perro", "simpatica"
        tono_base: Nota MIDI base número entero o notación inglesa
        canal: Canal de comunicación del 0 al 15
        """
        
        self.tipo = tipo.lower()
        self.canal = canal

        # Básicamente el estado de la cuerda
        self.activa = True

        self.midi = MIDI(midi_out=usb_midi.ports[1], out_channel= self.canal)


        # Puesto que se puede definir el tono base con un entero o con la nota
        # Se comprueba en qué caso se encuentra
        if isinstance(tono_base, int):
            self.tono_base = tono_base
        elif isinstance(tono_base, str):
            self.tono_base = nota2MIDI(tono_base)

        # En el caso de las cantoras se podrá modificar su tono a lo largo de la ejecución,
        # con lo que se definirá el tono actual y el tono anterior para esa gestión
        if self.tipo == "cantora":
            self.tono_actual = self.tono_base
            self.tono_anterior = self.tono_base

    def des_activar(self):
        self.suena(False)   # Primero deja de sonar por si las moscas
        self.activa = False # Luego se desactiva

    def activar(self):
        self.activa = True

    def suena(self, onOff = True,  volumen = 100):
        """
        onOff: False desactiva el tono, True activa
        volumen: se define con la velocidad de la rueda y modifica el volumen 

        Por defecto activa el tono

        El tono que suene en cada cuerda se define por variables internas de cada objeto
        """

        # Primero asegura que esta cuerda esté activa
        # Si lo que se quiere es que deje de sonar, se compreba que sea cantora o no si se "apaga" el tono
        # Si quiere que suene se comprueba también, se apagará el tono anterior en caso de ser cantora y se activará el nuevo
        if self.activa == True:

            if onOff == False:
                if self.tipo == "cantora":
                    self.midi.send(NoteOff(self.tono_anterior, 0))
                else:
                    self.midi.send(NoteOff(self.tono_base, 0))

            if onOff == True:
                if self.tipo == "cantora":
                    self.midi.send(NoteOn(self.tono_actual, volumen))
                    # Si cambió el tono se apaga el anterior y se actualiza, si no no
                    if self.tono_actual != self.tono_anterior:
                        self.suena(False)
                        self.tono_anterior = self.tono_actual
                else:
                    self.midi.send(NoteOn(self.tono_base, volumen))

class Rueda:
    def __init__(self):
        """
        Esta clase gesiona el sonido de las cuerdas.
        Si la cuerda está en modo activo la hace sonar y si está en modo "perreando" hace sonar el perro
        """
        self.cuerdas = []
        self.perro = None

    def agregar_cuerda(self,cuerda):
        """
        En un principio se esperaba que agregases un objeto cuerda desde la variable cuerda
        """
        self.cuerdas.append(cuerda)

    def girar(self, velocidad = 100):
        """
        Se reocrrerán las cuerdas asegurando que estén activas y se harán sonar a la velocidad indicada
        """

        for cuerda in self.cuerdas:
            # El perro solo "perreando"
            if cuerda.activa == True and cuerda.tipo is not "perro":
                cuerda.suena(volumen = velocidad)

            

    def parar(self):
        """
        Simplemente hace que todas las cuerdas dejen de sonar
        """
        for cuerda in self.cuerdas:
            if cuerda.activa == True:
                cuerda.suena(False)

    def perreando(self, onOff = True):
        """
        Si la velocidad supera un margen establecido, se activará el perro
        """
        if onOff == True and self.perro.activa == True:
            self.perro.suena()
        else:
            self.perro.suena(False)

    # Estemétodo aplica bending a las cuerdas cnatoras correspondiendo con el valor de entrada
    # analógica medida en la galga. POr defecto el valor central de 8192 para el tono base
    def bending(self, bend_val = 8192):
        for cuerda in self.cuerdas:
            if cuerda.activa == True and cuerda.tipo == "cantora":
                    cuerda.midi.send(PitchBend(bend_val))

class Teclado:
    def __init__(self):
        """
        Esta clase se encarga del tono de las cuerdas cantoras según la tecla pulsada
        """
        self.cuerdas = []

    def agregar_cuerda(self,cuerda):
        """
        En principio solo debería admitir cantoras o como mucho simpáticas
        """
        self.cuerdas.append(cuerda)

    def cambiaTono(self, tecla = None):
        """
        Este método se encarga de cambiar el tono actual de las cuerdas según la tecla pulsada
        cogerá la tecla y sumará un offset a las cuerdas proporcional a la tecla
        """

        # Esto se hace cogiendo el tono base y sumando la relación establecida con la tecla.
        # teniendo en cuenta que las notas MIDI son números enteros simplemente se suma
        # Valorará si hay una tecla pulsada y asignará el nuevo tono para que suene, si no hay nada
        # se quedará con el tono base (cuerda al aire)
        
        if tecla is not None:
            for cuerda in self.cuerdas:
                if cuerda.activa == True:
                    cuerda.tono_actual = cuerda.tono_base + tecla
        else:
            for cuerda in self.cuerdas:
                if cuerda.activa == True:
                    cuerda.tono_actual = cuerda.tono_base

    

class Zanfona:
    def __init__(self):
         """
         Esta clase se encarga de la gestión total de las cuerdas el teclado y la rueda
         """
         self.rueda = Rueda()
         self.teclado = Teclado()
         self.cuerdas = []
         self.perro = None

         self.idx_cuerda = 0
         self.umbral_perro = umbral_perro
         self.umbral_bending = umbral_bending
         self.tiempo_selector_cuerdas = tiempo_selector_cuerdas
                
    def agregar_cuerda(self, cuerda):
        """
        Se puede agregar un objeto cuerda o una tupla con los atributos de una cuerda
        
        tipo: Tipo de cuerda "cantora", "bordon", "trompeta", "perro"
        tono_base: Nota MIDI base número entero o notación inglesa
        canal: Canal de comunicación del 0 al 15
        """

        # Si es una tupla, define la cuerda como objeto
        if isinstance(cuerda,tuple) and len(cuerda) == 3:
            tipo, tono_base, canal = cuerda
            cuerda = Cuerda(tipo, tono_base, canal)

        # Si ya es un objeto se guarda, si no se define arriba y ya puede guardarla
        if isinstance(cuerda, Cuerda):
            # EL perro no es una cuerda como tal, así que no se agrega a la lista de cuerdas
            if cuerda.tipo == "perro":
                self.perro = cuerda
                self.rueda.perro = cuerda
                return 0
            
            self.cuerdas.append(cuerda)
            self.rueda.agregar_cuerda(cuerda)
            if cuerda.tipo == "cantora":
                self.teclado.agregar_cuerda(cuerda)
    
    def estado_selector_cuerdas(self):
        """
        Este método trabaja con un array de booleanos
        Esto representa la cuerda seleccionada en el momento con un True y todo lo demás a False
        Tiene además un índice a mayores, que representa el estado de la cuerda seleccionada
        Esto se pude usar directamente para conrolar un array de leds
        """
        selector = [False]*10

        selector[self.idx_cuerda] = True
        selector[-1] = self.cuerdas[self.idx_cuerda].activa

        # Cambia los valores de los leds según el estado
        for idx, led in enumerate(leds_selector_cuerdas):
            led.value = selector[idx]

        # Actualización del tiempo transcurrido tras la última visualización
        self.tiempo_selector_cuerdas = time.monotonic()
        # print(selector)
            
        return selector
    
    def actualiza_estado_cuerdas(self):
        """
        Este método se utilizará el encóder para seleccionar la cuerda que se desea 
        activar o desactivar en cada caso mediante el índice correspondiente
        """
        if time.monotonic() - self.tiempo_selector_cuerdas < duracion_selector_cuerdas:
            if self.cuerdas[self.idx_cuerda].activa == True:
                self.cuerdas[self.idx_cuerda].des_activar()
            else:
                self.cuerdas[self.idx_cuerda].activar()

        # No se tiene porqué imprimir, pero se debe llamar para actualizar el estado de los leds
        self.estado_selector_cuerdas()
    
    def indice_selector_cuerdas(self, dt):
        """
        Modifica el índice de la cuerda seleccionada para elegir una diferente
        """
        # De esta forma lo primero que hace es enseñarte lo que hay sin modificar nada
        # Si ya se encendió, lo siguiente sí que es modificar cosas
        if time.monotonic() - self.tiempo_selector_cuerdas < duracion_selector_cuerdas:
            if dt:
                self.idx_cuerda += 1
            else:
                self.idx_cuerda -= 1

            # Limitar valores
            if self.idx_cuerda < 0:
                self.idx_cuerda = len(self.cuerdas) - 1
            elif self.idx_cuerda > len(self.cuerdas) - 1:
                self.idx_cuerda = 0
            
        # No se tiene porqué imprimir, pero se debe llamar para actualizar el estado de los leds
        self.estado_selector_cuerdas()

    def actualiza_selector_cuerdas(self):
        """
        Este método es sencillo, simplemente comprueba que haya pasado el tiempo determinado
        y apaga los leds del selector de cuerdas para que no estén siempre encendidos
        """
        if time.monotonic() - self.tiempo_selector_cuerdas > duracion_selector_cuerdas:
            for led in leds_selector_cuerdas:
                led.value = False

    def modificar_umbral_perro(self, dt):
        """
        Básicamente sube o baja el umbral del perro según un valor dado respetando unos márgenes
        """
    
        if dt:
            self.umbral_perro += 10
        else:
            self.umbral_perro -= 10

        # Limitar valores
        if self.umbral_perro <= rango_perro[0]:
            self.umbral_perro = rango_perro[0]
        elif self.umbral_perro >= rango_perro[1]:
            self.umbral_perro = rango_perro[1]

        print(f"Modificando umbral perro: {self.umbral_perro} º/s")

    def modificar_umbral_bending(self, dt):
        """
        Ídem con el bending
        """

        if dt:
            self.umbral_bending += 1000
        else:
            self.umbral_bending -= 1000

        # Limitar valores
        if self.umbral_bending <= rango_bending[0]:
            self.umbral_bending = rango_bending[0]
        elif self.umbral_bending >= rango_bending[1]:
            self.umbral_bending = rango_bending[1]

        print(f"Modificando umbral bending: {self.umbral_bending}")