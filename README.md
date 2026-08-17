# Zanfona-MIDI

En este repositorio se recogen tanto los archivos de fabricación mecánica como el software y los esquemas electrónicos para la fabricación de un prototipo funcional de una zanfona MIDI. Este proyecto ha sido desarrollado como TFG para el grado en Robótica en la Universidad de Santiago de Compostela.

## [Electrónica](Electrónica) 

En esta carpeta están contenidos los diferentes esquemáticos utilizados en este proyecto. Además, se ha añadido el archivo de simulación empleado para la placa Resitor_Ladder, llamdo [Simulación_Resistor_Ladder.txt](Electrónica/Simulación_Resistor_Ladder.txt).
Para emplear este archivo correctamente es necesario cargarlo en el simulador de circuitos de [MasterPLC](https://masterplc.com/simulador/).

Se adjunta aquí mismo una tabla con las conexiones de la placa principal para mayor facilidad de lectura:

<img width="304" height="821" alt="imagen" src="https://github.com/user-attachments/assets/8b911803-9cb9-429d-8de5-2577b932e673" />


## [Hardware](Hardware)

Aquí se ven contenidos los archivos de fabricación mecánica. Como archivo principal [Archivo_Corte.CDR](Hardware/Archivo_Corte.CDR), permite el uso de una cortadora láser para fabricar todas las piezas necesarias en MDF de 3mm. se facilitan también los archivos individuales de cada pieza en la carpeta [Piezas_individuales](Hardware/Piezas_individuales)

## [Software](Software)

Este proyecto se ha desarrollado utilizando una Raspberry Pi Pico como microcontrolador principal. A su vez, se ha necesitado el firmware de [CircuitPython](https://circuitpython.org/board/raspberry_pi_pico/) para poder utilizarla como USB nativo, además de poder cargarle las librerías necesarias de [Adafruit_MIDI](https://github.com/adafruit/Adafruit_CircuitPython_MIDI).

Una vez configurada la Raspberry, es necesario copiar en el interior de su carpeta el archivo [code.py](Software/code.py) y la carpeta [dependencias](Software/dependencias), para el correcto funcionamiento de la zanfona.

Por otra parte, se facilita un archivo llamado [MEDIAS.py](Software/MEDIAS.py), que se utiliza para medir el rango de tensión de cada tecla pulsada y completar la tabla contenida en el archivo [variables.py](Software/dependencias/variables.py).
