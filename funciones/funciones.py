# asi se declara un funcion en Python
# se usa la misma logica de los dos puntos ':'
# def nombre_funcion() :
#   bloque de codigo

# def imprimir_mensaje():
#     print('Mensaje especial: ')
#     print('Estoy aprendiendo a usar funciones!')

# # mandar llamar la funcion | invocar funcion 
# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()


# def conversacion(mensaje):
#     print('Hola')
#     print('Como estas')
#     print(mensaje)
#     print('aidos')

# opcion = int(input('Elige un opcion (1, 2, 3): '))
# if opcion == 1:
#     conversacion('Elegiste la opcion 1')
# elif opcion == 2:
#     conversacion('Elegiste la opcion 2')
# elif opcion == 3:
#     conversacion('Elegiste la opcion 3')
# else:
#     print('Eligue una opcion correcta')

def suma(a, b):
    print('Se suman dos numeros')
    resultado = a + b
    return resultado

sumatoria = suma(1, 4)
print(sumatoria)