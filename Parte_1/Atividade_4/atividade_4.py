cateto1 = float(input("Insira o valor do primeiro cateto (cm): "))
cateto2 = float(input("Insira o valor do segundo cateto (cm): "))

h = pow(pow(cateto1, 2) + pow(cateto2, 2), 1/2)

print(f"A hipotenusa é de {h}cm")
