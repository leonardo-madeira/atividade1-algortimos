limite_superior = int(input("Insira o limite superior: "))
numero = 1

while numero < limite_superior:
    if numero % 2 != 0:
        print(numero)
        numero += 1
    else:
        numero += 1