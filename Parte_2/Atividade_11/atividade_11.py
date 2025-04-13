a = float(input("Insira o valor de a: "))
b = float(input("Insira o valor de b: "))
c = float(input("Insira o valor de c: "))

delta = (b**2) - (4*a*c)

if delta >0:
    raiz1= ((-1*b) + (delta**1/2) ) / 2*a
    raiz2= ((-1*b) - (delta**1/2) ) / 2*a
    print(f"Delta: {delta}, Raiz 1: {raiz1}, Raiz 2: {raiz2}")
else:
    print("Não possui raiz real")