altura = int(input("Insira a altura: "))
sexo = input("Insira o sexo(homem ou mulher): ")

if sexo=="homem":
    peso_ideal = (72.7*altura)-58
elif sexo=="mulher":
    peso_ideal = (62.1*altura)-44.7
else:
    print("Erro ao reconhecer sexo")

print(f"Peso ideal: {peso_ideal/1000}")
