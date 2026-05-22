opcao = 0
while opcao != 5:
    print ("1. Números multiplos de 3 ou 5")
    print ("2. Soma de números")
    print ("3. Divisíveis por 3")
    print ("4. Área de triângulo")
    print ("5. Sair")
    opcao = int(input("Qual a sua opção? "))

    if opcao == 1:        
        inferior = int(input("Limite inferior do intervalo: ")) 
        superior = int(input("Limite superior do intervalo: "))
        for n in range(inferior, superior):
            if (n % 3 == 0) or (n % 5 == 0):
                print (n)
    if opcao == 2:
        inferior = int(input("Limite inferior do intervalo: ")) 
        superior = int(input("Limite superior do intervalo: "))
        soma = 0
        for n in range(inferior, superior):
            soma = soma + n
        print ("A soma é: ", soma)
    if opcao == 3:
        inferior = int(input("Limite inferior do intervalo: ")) 
        superior = int(input("Limite superior do intervalo: "))
        for n in range(inferior, superior):
            if (n % 3 == 0):
                print (n)
    if opcao == 4:
        base = int(input("Base: ")) 
        altura = int(input("Altura: "))
        area = (base * altura) / 2
        print ("A área é: ", area)    

    
