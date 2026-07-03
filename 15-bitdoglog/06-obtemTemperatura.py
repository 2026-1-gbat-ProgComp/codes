import machine
        
def obtem_temperatura():
    valor_adc = sensor_temp.read_u16() * fator_conversao
    temperatura = 27 - (valor_adc - 0.706) / 0.001721
    return temperatura

while True:
    temperatura = obtem_temperatura()
    print (temperatura)
    time.sleep(2)
