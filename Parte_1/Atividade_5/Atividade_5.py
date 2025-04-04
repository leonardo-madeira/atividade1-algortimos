valor = float(input("Digite o valor da prestacao: "))
taxa = float(input("Digite a taxa de juros: "))
tempo = float(input("Digite o tempo de atraso (dias): "))

prestacao = valor + (valor*(taxa/100)*tempo)

print(f"O valor da pestracao é de: {prestacao}")