limite = int(input("Insira o limite: "))
h = 0

for i in range(1, limite + 1):
    h += (1 / i)
print (h)