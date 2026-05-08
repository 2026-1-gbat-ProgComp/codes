print ("Esse programa exibe as cédulas de um troco")
valor_conta = int (input("Valor da conta: "))
valor_pago = int (input("Valor pago: "))
troco = valor_pago - valor_conta
print ("Valor do troco:", troco)

ced200 = troco // 200
print ("#cedulas de 200: ", ced200)
troco = troco % 200

ced100 = troco // 100
print ("#cedulas de 100: ", ced100)
troco = troco % 100

ced50 = troco // 50
print ("#cedulas de 50: ", ced50)
troco = troco % 50

ced20 = troco // 20
print ("#cedulas de 20: ", ced20)
troco = troco % 20

ced10 = troco // 10
print ("#cedulas de 10: ", ced10)
troco = troco % 10

ced50 = troco // 5
print ("#cedulas de 5: ", ced5)
troco = troco % 5

ced2 = troco // 2
print ("#cedulas de 2: ", ced2)

moedas1 = troco % 2
print ("#moedas de 1: ", moedas1)

