conta = int (input ("Valor da conta: "))
pgto = int (input ("Valor do pagamento: "))
troco = pgto - conta
print ("O troco é: ", troco)    

cedulas = [200, 100, 50, 20, 10, 5, 2, 1 ]

for cedula in cedulas:
    qtde_cedulas = troco // cedula
    print ("# de cedulas", cedula, ":", qtde_cedulas)
    troco = troco % cedula
