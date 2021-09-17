# ADIVINA EL NUMERO
# hacer un programa que el usuario tenga que adivinar el numero que el programa penso
import random

def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input('Elige un numero del 1 al 100: '))
    contador = 0
    limite = 10
    print('Intentos resantes: ' + str(limite))
    while numero_elegido != numero_aleatorio and contador != 10:
        contador +=1
        if numero_elegido < numero_aleatorio:
            print('Busca un numero mas grande')
        else:
            print('Busca un numero mas pequeño')
        numero_elegido = int(input('Elige otro numero: '))
        limite -= 1
        print('Intentos resantes: ' + str(limite))
        print(contador)
    
    if limite != 0:
        print('GANASTE!!! si pense en el numero... '+ str(numero_aleatorio) + ' 😎')
    else:
        print('PERDISTEEE!!! JAJA 🤣')




if __name__ == '__main__':
    run()