def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿cuantos pesos " + tipo_pesos +  " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("tienes: $" + dolares + " dolares") 

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
    conversor("colombianos", 3875)
elif opcion == 2:
    conversor("Argentinos", 75)
elif opcion == 3:
    conversor("Mexicanos", 20)
else:
    print('Ingresa una opcion del menu!!!')