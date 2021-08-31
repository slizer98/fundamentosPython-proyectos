dolares = input("¿Cuantos dolares tienes?: ")
dolares = float(dolares)
valor_dolar = 20
pesos = valor_dolar * dolares
pesos = round(pesos, 2)
pesos = str(pesos)
print("tienes $" + pesos +" pesos Mexicanos")