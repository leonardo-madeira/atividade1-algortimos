nota1 = int(input("Insira a primeira nota: "))
nota2 = int(input("Insira a segunda nota: "))

media = (nota1 + nota2) / 2

print(f"Media: {media}")

if media <= 3:
    print("Reprovado sem rendimento")
elif media > 3 and media <=6:
    print("Reprovado com Insuficiente")
elif media > 6 and media <=7:
    print("Aprovado com Regular")
elif media > 7 and media <=9:
    print("Aprovado com Bom")
elif media > 9 and media <=10:
    print("Aprovado com Excelente")
else:
    print("Erro ao classificar")
