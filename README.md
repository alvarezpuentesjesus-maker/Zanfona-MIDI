# Zanfona-MIDI

En este repositorio se recogen tanto los archivos de fabricación mecánica como el software y los esquemas electrónicos para la fabricación de un prototipo funcional de una zanfona MIDI. Este proyecto ha sido desarrollado como TFG para el grado en Robótica en la Universidad de Santiago de Compostela.

## [Electrónica](Electrónica) 

En esta carpeta están contenidos los diferentes esquemáticos utilizados en este proyecto. Además, se ha añadido el archivo de simulación empleado para la placa Resitor_Ladder, llamdo Simulación_Resistor_Ladder.txt.
Para emplear este archivo correctamente es necesario cargarlo en el simulador de circuitos de [MasterPLC](https://masterplc.com/simulador/).

Se adjunta aquí mismo una tabla con las conexiones de la placa principal para mayor facilidad de lectura:

<div align="center">

| Pin | Nombre | Conexión |
| :---: | :---: | :---: |
| 1 | GP0 | Manivela SDA |
| 2 | GP1 | Manivela SCL |
| 3 | GND | |
| 4 | GP2 | Display cuerdas 1 |
| 5 | GP3 | Display cuerdas 2 |
| 6 | GP4 | Display cuerdas 3 |
| 7 | GP5 | Display cuerdas 4 |
| 8 | GND | |
| 9 | GP6 | Display cuerdas 5 |
| 10 | GP7 | Display cuerdas 6 |
| 11 | GP8 | Display cuerdas 7 |
| 12 | GP9 | Display cuerdas 8 |
| 13 | GND | |
| 14 | GP10 | Display cuerdas 9 |
| 15 | GP11 | Display cuerdas Estado |
| 16 | GP12 | CLK Encoder Cuerdas |
| 17 | GP13 | DT Encoder Cuerdas |
| 18 | GND | |
| 19 | GP14 | SW Encoder Cuerdas |
| 20 | GP15 | CLK Encoder Perro |
| 21 | GP16 | DT Encoder Perro |
| 22 | GP17 | SW Encoder Perro |
| 23 | GND | |
| 24 | GP18 | CLK Encoder Bending |
| 25 | GP19 | DT Encoder Bending |
| 26 | GP20 | SW Encoder Bending |
| 27 | GP21 | NC |
| 28 | GND | |
| 29 | GP22 | NC |
| 30 | RUN | NC |
| 31 | GP26 A0 | Teclado Resistencias |
| 32 | GP27 A1 | NC |
| 33 | ADC GND | |
| 34 | GP28 A2 | Bending |
| 35 | ADV Vref | NC |
| 36 | 3v3 Vout | |
| 37 | 3v3 En | NC |
| 38 | GND | |
| 39 | VSYS 5V* | NC |
| 40 | VBUS 5V | |

</div>

## [Hardware](Hardware)

Aquí se ven contenidos los archivos de fabricación mecánica. Como archivo principal Archivo_Corte.CDR, permite el uso de una cortadora láser para fabricar todas las piezas necesarias en MDF de 3mm. se facilitan también los archivos individuales de cada pieza en la carpeta [Piezas_individuales](Hardware/Piezas_individuales)

## [Software](Software)

Este proyecto se ha desarrollado utilizando una Raspberry Pi Pico como microcontrolador principal. A su vez, se ha necesitado el firmware de [CircuitPython](https://circuitpython.org/board/raspberry_pi_pico/) para poder utilizarla como USB nativo, además de poder cargarle las librerías necesarias de [Adafruit_MIDI](https://github.com/adafruit/Adafruit_CircuitPython_MIDI). En este caso se deben tener incluidas las librerías: adafruit_bus_device, adafruit_midi y adafruit_register.

Una vez configurada la Raspberry, es necesario copiar en el interior de su carpeta el archivo [code.py](Software/code.py) y la carpeta [dependencias](Software/dependencias), para el correcto funcionamiento de la zanfona.

Por otra parte, se facilita un archivo llamado [MEDIAS.py](Software/MEDIAS.py), que se utiliza para medir el rango de tensión de cada tecla pulsada y completar la tabla contenida en el archivo [variables.py](Software/dependencias/variables.py).


## BOM

En la siguiente tabla se puede ver el BOM tanto de elementos de hardware como electrónica para todo lo necesario en este proyecto:

<div align="center">

| Categoría | Referencia | Descripción | Cantidad | Precio ud | Precio Total | Proveedor |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| Electrónica | SC0915 | Microcontrolador Raspberry Pi Pico | 1 | 3,51 € | 3,51 € | [TME]([URL](https://www.tme.eu/es/details/sc0915/raspberry-pi-sistemas-embebidos/raspberry-pi/raspberry-pi-pico/) |
| Electrónica | CF1/4W-10K | Resistencia 10K 100ud | 1 | 0,87 € | 0,87 € | [TME](URL) |
| Electrónica | CF1/4W-150R | Resistencias 150Ω 100ud | 1 | 0,90 € | 0,90 € | [TME](URL) |
| Electrónica | CF1/4W-2K | Resistencias teclado 2K 100ud | 1 | 0,74 € | 0,74 € | [TME](URL) |
| Electrónica | TAL220B | Galga extensiométrica 5Kg | 1 | 9,49 € | 9,49 € | [Amazon](URL) |
| Electrónica | AD620 | Amplificador Galga | 1 | 5,79 € | 5,79 € | [Funduino](URL) |
| Electrónica | OSX10201-R | Barra Led 10 segmentos Roja | 1 | 0,82 € | 0,82 € | [TME](URL) |
| Electrónica | EC11E12-15P30C-SW | Encóders | 3 | 1,42 € | 4,26 € | [TME](URL) |
| Electrónica | AS5600 | Sensor Magneto resistivo | 1 | 0,99 € | 0,99 € | [Aliexpress](URL) |
| Electrónica | XY308-2P 2.54MM GREEN | Conector Bloque Terminal 10ud | 1 | 2,29 € | 2,29 € | [TME](URL) |
| Electrónica | XHP-3 | Conector JST 3 pines 2.5mm Hembra | 4 | 0,06 € | 0,24 € | [TME](URL) |
| Electrónica | B3B-XH-A (LF)(SN) | Conector JST 3 pines 2.5mm Macho | 4 | 0,09 € | 0,36 € | [TME](URL) |
| Electrónica | XHP-4 | Conector JST 4 pines 2.5mm Hembra | 2 | 0,07 € | 0,14 € | [TME](URL) |
| Electrónica | B4B-XH-A (LF)(SN) | Conector JST 4 pines 2.5mm Macho | 2 | 0,11 € | 0,22 € | [TME](URL) |
| Electrónica | XHP-5 | Conector JST 5 pines 2.5mm Hembra | 6 | 0,06 € | 0,36 € | [TME](URL) |
| Electrónica | B5B-XH-A (LF)(SN) | Conector JST 5 pines 2.5mm Macho | 6 | 0,16 € | 0,96 € | [TME](URL) |
| Electrónica | Cable AWG 26 | Bobina de cable para usos varios | 1 | 8,99 € | 8,99 € | [Amazon](URL) |
| Electrónica | PCBs | Coste producción PCBs | 3 | 5,00 € | 15,00 € | [PCBWay](URL) |
| **Subtotal Electrónica** | | | | | **55,93 €** | |
| Hardware | B5X10/BN3 | Tornillos M5 10mm 100ud | 1 | 3,18 € | 3,18 € | [TME](URL) |
| Hardware | M3X20/D912-A2 | Tornillos M3 20mm 100ud | 1 | 2,63 € | 2,63 € | [TME](URL) |
| Hardware | M3X30/D912-A2 | Tornillos M3 30mm 100ud | 1 | 3,10 € | 3,10 € | [TME](URL) |
| Hardware | B3/BN124 | Tuercas M3 5,5mm 100ud | 1 | 0,63 € | 0,63 € | [TME](URL) |
| Hardware | ST-093/1 | Punteras conexiones teclas M3 20ud | 2 | 1,09 € | 2,18 € | [TME](URL) |
| Hardware | Eje de acero 8mm x 200mm | Eje de acero 8mm x 200mm | 1 | 3,71 € | 3,71 € | [Amazon](URL) |
| Hardware | Cable de acero 1mm | Cable de acero 1mm | 1 | 2,49 € | 2,49 € | [Leroy Merlin](URL) |
| Hardware | Clavijas 3L3R | Clavijas Guitarra | 1 | 8,45 € | 8,45 € | [Amazon](URL) |
| Hardware | TABLERO MDF 120X60X0,3CM | Madera en plancha 120x60x0,3cm | 1 | 6,30 € | 6,30 € | [Obramat](URL) |
| Hardware | Hilo elástico 0,5mm | Hilo elástico 0,5mm | 1 | 0,94 € | 0,94 € | [Amazon](URL) |
| **Subtotal Hardware** | | | | | **33,61 €** | |
| **Coste Total de fabricación** | | | | | **89,54 €** | |

</div>
