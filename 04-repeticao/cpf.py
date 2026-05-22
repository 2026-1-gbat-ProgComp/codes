cpf = int (input("Digite o CPF: "))
soma = 0
for m in range(2, 11):
    n =  cpf % 10
    soma += n * m
    cpf = cpf // 10

dv1 = soma % 11
if dv1 >= 2:
    dv1 = 11 - dv1
else:
    dv1 = 0

print ("Primeiro digito verificador: ", dv1)