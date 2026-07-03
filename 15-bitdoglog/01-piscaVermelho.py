from machine import Pin
import time

# Na BitdogLab, o LED Vermelho é o GPIO 13
vermelho = Pin(13, Pin.OUT)

def pisca_vermelho(segundos):
    vermelho.value(True)   # Liga o LED
    time.sleep(segundos)
    vermelho.value(False)  # Desliga o LED
    time.sleep(segundos)

while True:
    pisca_vermelho(3)