contador = 25
soma = 0 

while contador <=201:
    if contador % 2 == 0:
        soma += contador
        contador += 1
    else:
        contador += 1
print(soma)