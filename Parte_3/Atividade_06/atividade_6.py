contador = 1

while contador <= 10:
        nome = input("Insira o nome: ")
        idade = int(input("Insira a idade: "))
        sexo = input("Insira o sexo (masculino ou feminino): ")

        if sexo == "masculino" and idade > 21:
            print(nome)
            contador +=1
        else:
              contador += 1