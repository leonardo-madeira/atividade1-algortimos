sexo = input("Insira o sexo(homem ou mulher): ")
idade = int(input("Insira a idade: "))

if (sexo == "mulher" and idade > 60) or (sexo == "homem" and idade > 65):
    print("Pode aposentar")
else:
    print("Não pode aposentar")

