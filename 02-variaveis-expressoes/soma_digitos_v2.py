print ("Esse programa a soma dos digitos de um numero")
num = int (input("Digite o numero (ate 4 digitos): "))

soma = 0 

soma = soma + num % 10
num = num // 10

soma = soma + num % 10
num = num // 10

soma = soma + num % 10
num = num // 10

soma = soma + num % 10

print ("A soma dos digitos é:", soma)