opcao = 0
while opcao != 5:
    print ("Opções:")
    print ("1 - somar")
    print ("2 - subtrair")
    print ("3 - multiplicar")
    print ("4 - dividir")
    print ("5 - sair")

    opcao = int (input("Qual a sua opção:"))
    if 1 <= opcao <= 4: 
        num1 = int (input("Numero 1: "))
        num2 = int (input("Numero 2: "))
        if opcao == 1:
            resultado = num1 + num2
        if opcao == 2:
            resultado = num1 - num2
        if opcao == 3:
            resultado = num1 * num2
        if opcao == 4:
            resultado = num1 / num2

        print ("O resultado é: ", resultado)
