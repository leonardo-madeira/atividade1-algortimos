nota = float(input("Insira a nota: "))

if nota >= 0 and nota < 2:
    print("Sem rendimento")
elif nota> 2 and nota < 4:
    print("Mau")
elif nota >= 4 and nota < 6:
    print("Regular")
elif nota >= 6 and nota < 8.5:
    print("Bom")
elif nota >= 8.5 and nota < 10:
    print("Excelente")
else:
    print("Não foi possível classificar")