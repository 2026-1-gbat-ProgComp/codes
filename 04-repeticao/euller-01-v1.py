# Projeto Euler - Programa 01

soma = 0

num = 1
if num % 3 == 0:
    soma = soma + num
else:
    if num % 5 == 0:
        soma = soma + num

num = 2
if num % 3 == 0:
    soma = soma + num
else:
    if num % 5 == 0:
        soma = soma + num

# ... Copie ate que num seja 999

print ("A soma é: ", soma)