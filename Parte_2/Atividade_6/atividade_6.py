salario = float(input("Insira o salário: "))

if salario < 800:
    salario_ajustado = salario * 1.15
elif salario >= 800 and salario <= 1500:
    salario_ajustado = salario * 1.10
else:
    salario_ajustado = salario * 1.05

print(f"Salário ajustado: ", "{:.2f}".format(salario))


 
