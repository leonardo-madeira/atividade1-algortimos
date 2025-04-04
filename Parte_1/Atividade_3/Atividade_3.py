import numpy as np

raio_lata = float(input("Insira o raio da lata (cm): "))
altura_lata = float(input("Insira a altura da lata (cm): "))

volume = np.pi * pow(raio_lata,2) * altura_lata

print(f"O volume da lata é: {volume} cm3")
