print ("Esse programa a soma dos digitos de um numero")
num = int (input("Digite o numero (ate 4 digitos): "))

soma = 0 

soma = soma + num // 1000
num = num % 1000

soma = soma + num // 100
num = num % 100

soma = soma + num // 10
num = num % 10

soma = soma + num

print ("A soma dos digitos é:", soma)