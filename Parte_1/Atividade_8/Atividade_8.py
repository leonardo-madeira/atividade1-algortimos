quant_hamburguer = int(input("Insrira quantos hamburgueres foram pedidos: "))
quant_cheeseburguer = int(input("Insrira quantos cheeseburguers foram pedidos: "))
quant_milkShake = int(input("Insrira quantos milkshakes foram pedidos: "))
quant_cocaCola = int(input("Insrira quantas coca-colas foram pedidas: "))

preco_hamburguer = 3.50
preco_cheeseburguer = 4.10
preco_milkShake = 6.00
preco_cocaCola = 2.50

conta_final = ( (preco_hamburguer * quant_hamburguer) + (preco_cheeseburguer * quant_cheeseburguer) +
(preco_milkShake * quant_milkShake) + (preco_cocaCola * quant_cocaCola) )

print(f"Conta final: R${conta_final}")
