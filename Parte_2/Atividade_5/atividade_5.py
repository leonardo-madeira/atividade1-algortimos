v1 = int(input("Primeiro numero: "))
operador = input("Operador: ")
v2 = int(input("Segundo numero: "))

if operador == "+":
    conta = v1 + v2
elif operador == "-":
    conta = v1 - v2
elif operador == "*":
    conta = v1  * v2
elif operador == "/":
    conta = v1/v2
else:
    print("Nenhum operador válido")

print(conta)

