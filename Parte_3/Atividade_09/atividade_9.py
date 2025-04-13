numero = int(input("Insira o numero: "))

contador = 1
fatorial = 1

while contador <= numero:
    if contador != numero:
        print(f"{contador} X ", end="")
    else:
        print(f"{contador} = ", end="")
    fatorial *= contador
    contador += 1

print(fatorial)
