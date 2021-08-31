# las triples comillas dobles sirven para hacer comentarios 
# en varias lineas, por ejemplo:
menu = """  
Bienvenido al conversor de monedas 💲🤑

1,- Pesos colombianos 
2.- Pesos argentinos
3.- Pesos mexicanos

Elige una opcion: """

# recibimos el valor del menu y lo convertimos a entero
opcion = int(input(menu))
# checamos que numero ingresa el usuario y convertimos
if opcion == 1:
    pesos = input("¿cuantos pesos Colombianos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 3843
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("tienes: $" + dolares + " dolares") 
elif opcion == 2:
    pesos = input("¿cuantos pesos Argentinos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 97.58
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("tienes: $" + dolares + " dolares") 
elif opcion == 3:
    pesos = input("¿cuantos pesos Mexicanos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 20
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("tienes: $" + dolares + " dolares") 
else:
    print('Ingresa una opcion del menu!!!')


