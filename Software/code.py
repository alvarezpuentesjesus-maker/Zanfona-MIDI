from dependencias.zanfona import *



# Hacer una media con los valores del bending para ver de qué partimos y usar eso para definir el "0"
sumatorio_bending = 0

for i in range (1000):
    valor_bending = bending_in.value
    sumatorio_bending += valor_bending
    time.sleep(0.001)

media_bending = sumatorio_bending/1000

print(f"Media bending: {media_bending}")



# --------- TEMA CUERDAS ----------

# FALTA LA GESTIÓN DE LAS CUERDAS SIMPÁTICAS !!!!!!!!

zanfona = Zanfona()

zanfona.agregar_cuerda(("cantora", "G4", 0))
zanfona.agregar_cuerda(("cantora", "G3", 1))
zanfona.agregar_cuerda(("cantora", "G3", 2)) # OJO, se ve que no le gusta esa parte a la zonafona que hay

zanfona.agregar_cuerda(("bordon", "C3", 3))
zanfona.agregar_cuerda(("bordon", "G2", 4))
zanfona.agregar_cuerda(("bordon", "G2", 5))

zanfona.agregar_cuerda(("trompeta", "C4", 6))
zanfona.agregar_cuerda(("trompeta", "C4", 7))
zanfona.agregar_cuerda(("trompeta", "C4", 8))

# zanfona.agregar_cuerda(("perro", "D4", 9)) # LMMS Studio Perro.WAW
zanfona.agregar_cuerda(("perro", "C4", 10)) # Fluidsynth o LMMS Studio Perro.sf2



print("Estado cuerdas:")
print(zanfona.estado_selector_cuerdas())


while True:
    # ----- Lectura de manivela -----
    lectura_encoder = lectura_angulo()
    angulo = (lectura_encoder * 360.0) / 4096.0
    t_angulo = time.monotonic()

    # Gestión de la manivela
    if angulo_ant is not None:
        dt_angulo = t_angulo - t_angulo_ant

        if dt_angulo > 0:

            # Corrección salto 360°
            delta = correcion_angulo(angulo, angulo_ant)

            # -------- VELOCIDAD --------
            vel = delta / dt_angulo  # velocidad en º/s
            vel_f = media_movil_velocidad(vel)

            t_vel = t_angulo

        # De esta forma se pueden ignorar valores bajos de velocidad derivados de ruido
        if vel_f is not None and vel_f > velocidad_base_manivela:

            # -----  Actualización de las teclas -------
            lectura_teclas = teclado_in.value
            tension = (lectura_teclas/65535)*3.3
            tecla_pulsada = rango2Teclas(tension)
            # print(f"Tension: {tension} || Tecla: {tecla_pulsada}")


                     
            # De esta forma no la actualiza si no es necesario
            # Un pequeño antibounce suprimientdo cambios de menos de un tiempo pertinente
            if tecla_pulsada != None and tecla_pulsada != tecla_ant and (time.monotonic() - tiempo_ultima_tecla) > anti_bounce:
                print(f"Tension: {tension} || Tecla: {tecla_pulsada}")
                zanfona.teclado.cambiaTono(tecla_pulsada)
                # Se debe activar girar, para actualizar los valores de las teclas pulsadas
                tecla_ant = tecla_pulsada
                ACTUALIZADO = False # De esta forma actualiza los valores
                tiempo_ultima_tecla = time.monotonic()

            
            # Se mide la entrada analógica de la galga con el amplificador
            valor_bending = bending_in.value
            #print(f"Valor bending: {valor_bending}")

            # Por simplificación inicial, se define un umbral que superar habiendo hecho la meida previamente
            # Esto se hace porque la galga va a estar en tensión inicialmente y no tendrá un vlaor de 0
            if valor_bending > media_bending + zanfona.umbral_bending and BENDING_ACTIVO == True:
                # Esta variable simplemente se usa para que se mande el mensaje una única vez
                if BENDING == False:  
                    # Si se supera este humbral se pone el valor de pitch bend hacia arriba   
                    bend_val = 12000       
                    print("BENDEADNDO")  
                    zanfona.rueda.bending(bend_val)
                    BENDING = True  

            # Si tiene
            elif (BENDING == True):
                zanfona.rueda.bending()
                BENDING = False



            # Al marcar el giro, actualiza todo lo que se haya modificado antes   
            # Se valorará el uso de la velocidad para el volumen, pero de esta forma no se reenvían notas innecesariamente
            if ACTUALIZADO == False: 
                zanfona.rueda.girar()
                ACTUALIZADO = True
                # print("Sonando")


            # Simplemente si se supera una velocidad hace sonar el perro, si no lo para
            if vel_f > zanfona.umbral_perro and zanfona.perro.activa and PERREANDO == False:
                zanfona.rueda.perreando()
                PERREANDO = True
                # print("Perreando")
               

            elif vel_f < zanfona.umbral_perro and  zanfona.perro.activa and PERREANDO == True:
                zanfona.rueda.perreando(False)
                PERREANDO = False

        else:
            zanfona.rueda.parar()
            zanfona.rueda.perreando(False)
            ACTUALIZADO = False
            PERREANDO = False


    # ------------ PERRO ------------
    perro_lectura_clk = perro_clk.value 

    if perro_clk_ant and not perro_lectura_clk:
        zanfona.modificar_umbral_perro(perro_dt.value)

        # --- Botón ---
    perro_lectura_boton = perro_sw.value  
    # Detectar pulsación con debounce y activas o desactivar el perro
    if not perro_lectura_boton and perro_boton_ant and (time.monotonic() - perro_tiempo_boton_ant) > anti_bounce:
        if zanfona.perro.activa == True:
            zanfona.perro.des_activar()
            print("Desactivando perro")
            
        else:
            zanfona.perro.activar()
            print("Activando perro")
        perro_tiempo_boton_ant = time.monotonic()
    # ------------------------------------

    # ------------ BENDING ------------
    bending_lectura_clk = bending_clk.value 

    if bending_clk_ant and not bending_lectura_clk:
        zanfona.modificar_umbral_bending(bending_dt.value)

        # --- Botón ---
    bending_lectura_boton = bending_sw.value  
    # Detectar pulsación con debounce y activas o desactivar el perro
    if not bending_lectura_boton and bending_boton_ant and (time.monotonic() - bending_tiempo_boton_ant) > anti_bounce:
        if BENDING_ACTIVO == True:
            BENDING_ACTIVO = False
            zanfona.rueda.bending()
            print("Desactivando bending")
            
        else:
            BENDING_ACTIVO = True
            print("Activando bending")
        bending_tiempo_boton_ant = time.monotonic()
    # ------------------------------------

    # ------------ SELECTOR CUERDAS ------------
    cuerdas_lectura_clk = cuerdas_clk.value

    if cuerdas_clk_ant and not cuerdas_lectura_clk:
        zanfona.indice_selector_cuerdas(cuerdas_dt.value)

        # --- Botón ---
    cuerdas_lectura_boton = cuerdas_sw.value  
    # Detectar pulsación con debounce para activar o desactivar la cuerda 
    if not cuerdas_lectura_boton and cuerdas_boton_ant and (time.monotonic() - cuerdas_tiempo_boton_ant) > anti_bounce:
        zanfona.actualiza_estado_cuerdas()
        cuerdas_tiempo_boton_ant = time.monotonic()

    zanfona.actualiza_selector_cuerdas()
    # ------------------------------------

    angulo_ant = angulo # Tema manivela                
    t_angulo_ant = t_angulo 

    perro_clk_ant = perro_lectura_clk # Tema perro
    perro_boton_ant = perro_lectura_boton

    bending_clk_ant = bending_lectura_clk # Tema bending
    bending_boton_ant = bending_lectura_boton

    cuerdas_clk_ant = cuerdas_lectura_clk # Tema selector cuerdas
    cuerdas_boton_ant = cuerdas_lectura_boton