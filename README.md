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
