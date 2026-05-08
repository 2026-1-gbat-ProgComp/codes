#Calculadora de raízes
print("Calculadora de raízes de equacao 2o grau")

a = int(input("Informe o valor de a:"))
b = int(input("Informe o valor de b:"))
c = int(input("Informe o valor de c:"))

delta = b ** 2 - 4 * a * c
x1 = (-b + delta**0.5) / (2 * a)
x2 = (-b - delta**0.5) / (2 * a)

print("A equação possui as raízes x1: ", x1,"e x2:", x2)

