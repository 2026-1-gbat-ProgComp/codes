from machine import Pin

# Configuração dos botões
button_a = Pin(5, Pin.IN, Pin.PULL_UP)
button_b = Pin(6, Pin.IN, Pin.PULL_UP)

# Configuração do LED RGB
green_led = Pin(11, Pin.OUT)
blue_led = Pin(12, Pin.OUT)
red_led = Pin(13, Pin.OUT)

# Desligando o LED RGB inicialmente
red_led.value(0)
green_led.value(0)
blue_led.value(0)

while True:
    # Se o ambos os botões estão pressionados
    if button_b.value() == 0 and button_a.value() == 0:
        red_led.value(1)
        green_led.value(0)
        blue_led.value(0)
    # Se o Botão A for pressionado
    elif button_a.value() == 0:
        red_led.value(0)
        green_led.value(1)
        blue_led.value(0)
    # Se o Botão B for pressionado
    elif button_b.value() == 0:
        red_led.value(0)
        green_led.value(0)
        blue_led.value(1)
