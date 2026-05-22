cpf = int(input("Digite o CPF: "))
dv1 = int(input("Digite o primeiro dv: ")) 
soma = dv1 * 2
for m in range(3, 12):
    n =  cpf % 10
    soma += n * m
    cpf = cpf // 10

dv2 = soma % 11
if dv2 >= 2:
    dv2 = 11 - dv2
else:
    dv2 = 0
print ("Primeiro digito verificador: ", dv2)