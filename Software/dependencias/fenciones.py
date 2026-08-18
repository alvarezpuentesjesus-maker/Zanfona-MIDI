"""
Módulo de Funciones Auxiliares
==============================

Proporciona funciones para el procesamiento numérico y de sensores:
- Conversión de notas musicales en notación anglosajona a números MIDI.
- Asignación de rango de tensión de las teclas a notas analógicas.
- Comunicación I2C con el sensor magnético AS5600 para la lectura de la manivela.
- Corrección de discontinuidad angular y cálculo de media móvil para velocidad.

Información del archivo:
- Archivo: dependencias/fenciones.py
- Autor: Jesús Álvarez Puentes
- Fecha: 2026-07-28
- Versión: 0.1
- Licencia: MIT
- Dependencias:
    * CircuitPython (busio)
    * dependencias.variables
"""



from dependencias.variables import *

# -------- Teclas y notas MIDI --------

def nota2MIDI(nota):
    """
    Se le pasa una nota en notación anglosajona a MIDI
    
    ejemplo: C4 -> 60
    """
    # Se coge todo menos el número de octava como nombre de la nota y el último como octava
    nombre = nota[:-1]
    octava = int(nota[-1])

    # nombre = nombre.upper()

    if nombre not in NOTAS:
        raise ValueError(f"No se ha encontrado la nota: {nombre}")

    # Las octavas se separan por 12 notas, con lo que se multiplica
    # el valor de la octava +1 para ubucarse y luego se gestiona la propia nota

    return 12*(octava + 1) + NOTAS[nombre]

# Busca la relación entre el valor de tesnión actual y la nota numérica MIDI
def rango2Teclas(tension):
    for media, std, tecla in TECLAS:
        Vmin = media - std*tolerancia_teclas
        Vmax = media + std*tolerancia_teclas
        if Vmin <= tension <= Vmax:
            return tecla
    return None

# ---------------- MANIVELA ----------------

def lectura_angulo():
    while not i2c.try_lock():
        pass
    try:
        data = bytearray(2)
        i2c.writeto_then_readfrom(AS5600_ADDR, bytes([ANGLE_REG]), data)
        raw = (data[0] << 8) | data[1]
        return raw & 0x0FFF
    finally:
        i2c.unlock()

def correcion_angulo(angulo, angulo_ant):
    delta = angulo - angulo_ant
    if delta > 180:
        delta -= 360
    elif delta < -180:
        delta += 360
    return delta

def media_movil_velocidad(v):
    global vel_sum, vel_idx
    vel_sum -= vel_buffer[vel_idx]
    vel_buffer[vel_idx] = v
    vel_sum += v
    vel_idx = (vel_idx + 1) % N
    return vel_sum / N
