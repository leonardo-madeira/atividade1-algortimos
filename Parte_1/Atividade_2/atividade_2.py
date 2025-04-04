import numpy as np

raio = float(input("Insira o raio da circunferencia: "))

A = np.pi * (pow(raio,2))

print(f"Area: {A}")