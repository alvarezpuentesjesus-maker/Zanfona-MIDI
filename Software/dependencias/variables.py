"""
Módulo de Configuración de Hardware y Constantes
================================================

Define la asignación de pines GPIO (encoders, botones, LEDs, I2C, entradas analógicas),
las constantes de calibración del teclado analógico, tablas de frecuencias/notas MIDI
y variables globales de estado del sistema.

Información del archivo:
- Archivo: dependencias/variables.py
- Autor: Jesús Álvarez Puentes
- Fecha: 2026-07-28
- Versión: 0.1
- Licencia: MIT
- Dependencias:
    * CircuitPython (board, digitalio, analogio, busio, usb_midi)
    * adafruit_midi (MIDI, NoteOn, NoteOff, PitchBend)
    * time
"""




import time
import analogio
import digitalio
import board
import busio
import usb_midi
from adafruit_midi import MIDI
from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff
from adafruit_midi.pitch_bend import PitchBend




# Simplemente variables de estado para controlar el perro y el sonido de las cuerdas
ACTUALIZADO = False
PERREANDO = False


# -------------------------- SELECTOR CUERDAS --------------------------
# Pines del encoder
cuerdas_clk = digitalio.DigitalInOut(board.GP12)
cuerdas_clk.direction = digitalio.Direction.INPUT
cuerdas_clk.pull = digitalio.Pull.UP

cuerdas_dt = digitalio.DigitalInOut(board.GP13)
cuerdas_dt.direction = digitalio.Direction.INPUT
cuerdas_dt.pull = digitalio.Pull.UP

# Botón del encoder
cuerdas_sw = digitalio.DigitalInOut(board.GP14)
cuerdas_sw.direction = digitalio.Direction.INPUT
cuerdas_sw.pull = digitalio.Pull.UP


cuerdas_clk_ant = cuerdas_clk.value
cuerdas_boton_ant = cuerdas_sw.value
cuerdas_tiempo_boton_ant = 0

# Pines para leds
leds_pins = [board.GP2, board.GP3, board.GP4, 
             board.GP5, board.GP6, board.GP7, 
             board.GP8, board.GP9, board.GP10, 
             board.GP11]

leds_selector_cuerdas = [] 
for pin in leds_pins: 
    led = digitalio.DigitalInOut(pin) 
    led.direction = digitalio.Direction.OUTPUT 
    leds_selector_cuerdas.append(led)

duracion_selector_cuerdas = 2  # Tiempo que permanece encendido en segundos
tiempo_selector_cuerdas = 0 # Registro de ese tiempo
# --------------------------------------------------



# -------------------------- MANIVELA --------------------------
try:
    i2c = busio.I2C(board.GP1, board.GP0)  # SCL, SDA

except Exception as e:
    print("Error al inicial sensor manivela:",e)
    i2c = None         

AS5600_ADDR = 0x36
ANGLE_REG = 0x0E  # RAW ANGLE (MSB)

# Se utilizará para la media móvil
N = 10
vel_buffer = [0.0] * N
vel_sum = 0.0
vel_idx = 0

angulo_ant = None
t_angulo_ant = None
vel_f = None
velocidad_base_manivela = 10                    # Un valor mínimo para que la manivela considere que se mueve
# --------------------------------------------------



# -------------------------- PERRO --------------------------
umbral_perro = 300                              # Con este valor (debería poder cambiar) se define la sensibilidad del perro 
rango_perro = (velocidad_base_manivela, 1000)   # Como se puede modificar el valor, se define un rango máximo y mínimo
perro_tiempo_boton_ant = 0

# Pines del encoder
perro_clk = digitalio.DigitalInOut(board.GP15)
perro_clk.direction = digitalio.Direction.INPUT
perro_clk.pull = digitalio.Pull.UP

perro_dt = digitalio.DigitalInOut(board.GP16)
perro_dt.direction = digitalio.Direction.INPUT
perro_dt.pull = digitalio.Pull.UP

# Botón del encoder
perro_sw = digitalio.DigitalInOut(board.GP17)
perro_sw.direction = digitalio.Direction.INPUT
perro_sw.pull = digitalio.Pull.UP


perro_clk_ant = perro_clk.value
perro_boton_ant = perro_sw.value
# --------------------------------------------------



# -------------------------- TECLADO --------------------------
teclado_in = analogio.AnalogIn(board.A0)

# Se inicializan estas variables para poder usarlas en el debug sin problemas
tension = None
tecla_pulsada = None
tecla_ant = None
anti_bounce = 0.02   # Se utiliza para prevenir los falsos contactos
tiempo_ultima_tecla = 0

tolerancia_teclas = 3.5 # Se define este factor para su uso junto con la desviación estándar

# Se define una lista de tuplas que recoge los márgenes de las teclas
# Se define del siguiente modo (Media, Desviació típica, Número de tecla)
TECLAS = [
    (2.72, 0.003, 0), # Cuerda al Aiure

        (2.703, 0.002, 1),  # 1S

    (2.678, 0.003, 2),  # 1T 

        (2.6589, 0.0030, 3),  # 2S 

    (2.631, 0.0035, 4),  # 2T
    (2.608, 0.0025, 5),  # 3T

        (2.584, 0.0021, 6),  #3S

    (2.549, 0.0035, 7),   # 4T

        (2.5223, 0.0024, 8),  #4S

    (2.491, 0.003, 9),   # 5T
    (2.444, 0.0032, 10),  # 6T

        (2.406, 0.0013, 11),  #5S

    (2.355, 0.0035, 12),  # 7T

        (2.304, 0.0023, 13),  #6S

    (2.242, 0.0030, 14),  # 8T

        (2.177, 0.0023, 15),  #7S

    (2.103, 0.0036, 16),   # 9T
    (2.016, 0.003, 17),   # 10T

        (1.911, 0.0021, 18),  #8S

    (1.830, 0.0040, 19),   # 11T    ## ALGO CHUNGO TIENE, EESTÁ DANDO MEDIDAS QUE NO TIENEN SENTIDO

        (1.639, 0.0021, 20),  #9S

    (1.458, 0.002, 21),   # 12T
    (1.235, 0.002, 22),   # 13T

        (0.947, 0.0021, 23),  #910

    (0.557, 0.003, 24)    # 14T
]

# --------------------------------------------------

# -------- Relación de notas con su valor MIDI ------
NOTAS = {
    "C": 0,
    "C#": 1, "Db": 1,
    "D": 2,
    "D#": 3, "Eb": 3,
    "E": 4,
    "F": 5,
    "F#": 6, "Gb": 6,
    "G": 7,
    "G#": 8, "Ab": 8,
    "A": 9,
    "A#": 10, "Bb": 10,
    "B": 11
}



# -------------------------- TEMA BENDING --------------------------
bending_in = analogio.AnalogIn(board.A2)

umbral_bending = 20000      # Valor por defecto de subida 
rango_bending = (5000, 50000)
media_bending = 0           # Usado para hace rla media inicial de la entrada analógica
bend_val = 8192             # Valor central del bendidn, no variar nada

BENDING = False    # Se usa simplemente para actualizar las cuerdas o no    
BENDING_ACTIVO = True

bending_tiempo_boton_ant = 0

# Pines del encoder
bending_clk = digitalio.DigitalInOut(board.GP18)
bending_clk.direction = digitalio.Direction.INPUT
bending_clk.pull = digitalio.Pull.UP

bending_dt = digitalio.DigitalInOut(board.GP19)
bending_dt.direction = digitalio.Direction.INPUT
bending_dt.pull = digitalio.Pull.UP

# Botón del encoder
bending_sw = digitalio.DigitalInOut(board.GP20)
bending_sw.direction = digitalio.Direction.INPUT
bending_sw.pull = digitalio.Pull.UP


bending_clk_ant = bending_clk.value
bending_boton_ant = bending_sw.value