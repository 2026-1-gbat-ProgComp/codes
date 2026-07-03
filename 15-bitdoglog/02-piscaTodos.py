from machine import Pin
import time

verde = Pin(11, Pin.OUT)
azul = Pin(12, Pin.OUT)
vermelho = Pin(13, Pin.OUT)

def acender_led(pino, segundos):
    pino.value(True)
    time.sleep(segundos)
    pino.value(False)

while True:
    for pino in (verde, azul, vermelho):
        acender_led(pino, 1)
        time.sleep(1)

