ponto_x = float(input("Inserir ponto x: "))
ponto_y = float(input("Inserir ponto y: "))

if ponto_x > 0 and ponto_y > 0:
    print("Primeiro Quadrante")
elif ponto_x < 0 and ponto_y > 0:
    print("Segundo Quadrante")
elif ponto_x < 0 and ponto_y < 0:
    print("Terceiro Quadrante")
else:
    print("Quarto Quadrante")



    