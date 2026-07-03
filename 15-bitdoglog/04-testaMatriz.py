from machine import Pin
import neopixel
import time

# Número de LEDs na sua matriz 5x5
NUM_LEDS = 25

# Inicializar a matriz de NeoPixels no GPIO7
np = neopixel.NeoPixel(Pin(7), NUM_LEDS)

# Definindo a matriz de LEDs para formar um coração
coracao = [
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 1, 0, 1, 0],
 
]

# Função para acender a matriz de LEDs com base no padrão do coração
def testa_matriz():
    for i in range(5):
        for j in range(5):
            index = i * 5 + j
            np[index] = (255, 0, 0)
            np.write()
            time.sleep(1)
            np[index] = (0, 0, 0)
            np.write()
            

# Acender a matriz ponto a ponto
testa_matriz()

# Desligar todos os LEDs
for i in range(NUM_LEDS):
    np[i] = (0, 0, 0)

np.write()