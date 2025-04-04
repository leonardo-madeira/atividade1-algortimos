import numpy as np

raio = float(input("Insira o raio da circunferencia (cm): "))

perimetro= 2 * np.pi * raio

area = np.pi * (pow(raio,2))

print(f"Perimetro: {perimetro}cm")
print(f"Area: {area}cm")
