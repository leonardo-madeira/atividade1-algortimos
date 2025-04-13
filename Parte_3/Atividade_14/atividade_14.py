controle= 1 
homem_olho_castanho= 0
mulher_menor_160= 0 
total_mulher= 0

while  controle<= 15:
    nome = input("Insira o nome: ")
    altura = float(input("Insira a altura (cm): "))
    sexo = input("Insira o sexo (M ou F): ").upper()
    cor_olho = input("Insira a cor do olho (A - azuis, V - verdes, C - castanhos): ").upper()

    if sexo == "M" and cor_olho == "C":
        homem_olho_castanho += 1
        controle += 1
    elif sexo == "F" and altura < 160:
        mulher_menor_160 += 1
        total_mulher += 1
        controle += 1
    elif sexo == "F":
        total_mulher += 1
        controle += 1

print(f"Total de homens de olho castanho = {homem_olho_castanho}")
print(f"Total de mulheres menor de 1.60m = {mulher_menor_160}")
print(f"Total de mulheres = {total_mulher}")
