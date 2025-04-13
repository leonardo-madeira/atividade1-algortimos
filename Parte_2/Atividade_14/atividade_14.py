num_lados = int(input("Insira a quantidade de lados: "))

if num_lados < 3:
    print("Não é um polígono")
elif num_lados == 3:
    print("É Triângulo")
elif num_lados == 4:
    print("É Quadrado")
elif num_lados == 5:
    print("É Pentagono")
else:
    print("Polígono não identificado")
