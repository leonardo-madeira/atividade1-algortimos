angulo1 = int(input("Insira o angulo 1: "))
angulo2 = int(input("Insira o angulo 2: "))
angulo3 = int(input("Insira o angulo 3: "))

if angulo1 < 90 and angulo2 < 90 and angulo3 < 90:
    print("O triângulo é acutãngulo")
elif angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
    print("O triângulo é retêngulo")
elif angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
    print("O triângulo é retângulo")
else:
    print("Não foi possível Classificar")
    