import machine
        
def obtem_temperatura():
    valor_adc = sensor_temp.read_u16() * fator_conversao
    temperatura = 27 - (valor_adc - 0.706) / 0.001721
    return temperatura

sensor_temp = machine.ADC(4)
fator_conversao = 3.3 / 65535

while True:
    temperatura = obtem_temperatura()
    print (temperatura)
    time.sleep(2)
