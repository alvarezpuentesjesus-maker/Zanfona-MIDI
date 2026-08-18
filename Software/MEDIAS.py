"""
Script de Calibración: Medida de Tensión y Desviación Estándar
==============================================================

Realiza el muestreo masivo de la entrada analógica A0 para calcular
el valor medio de tensión y su desviación estándar. Utilizado para la
calibración y caracterización estadística de los rangos de las teclas.

Información del archivo:
- Archivo: MEDIAS.py
- Autor: Jesús Álvarez Puentes
- Fecha: 2026-07-28
- Versión: 0.1
- Licencia: MIT
- Dependencias:
    * CircuitPython (board, analogio, time)
    * math (Librería estándar)
"""

import analogio
import board
import time
import math

teclado_in = analogio.AnalogIn(board.A0)

print("EMPEZANDO MEDIDAS")
time.sleep(2)

medidas = 15000
samples = []
for i in range(medidas):
    lectura = teclado_in.value
    tension = (lectura/65535)*3.3   
    samples.append(tension)  
    # print(f"Tension: {tension}V")   
media = sum(samples)/len(samples)
temp =  0
for x in samples:
    temp += (x - media)**2
std = math.sqrt(temp/medidas)
    
print(f"\n\nMEDIA: {media} ")
print(f"Desviación estándar: {std} ") 
