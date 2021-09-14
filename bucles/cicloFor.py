# Escribir numeros del 1 al 1000

# con while
# contador = 1
# print(contador)
# while contador < 1000:
#     contador+=1
#     print(contador)

# for contador in range(1, 1001):
#     print(contador)

# for i in range(10):
#     print(11 * i)

# Tablas de multiplicar
tabla = int(input('Que tabla ocupa: '))
for i in range(1, 11):
    print(str(tabla) + '*' + str(i) + '=' + str(tabla * i))