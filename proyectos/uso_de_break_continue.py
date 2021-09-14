# programa para buscar letras de una oracion 
def run():
    oracion = input('Escribe tu oracion: ')
    letra_buscar = input('Que letras desea buscar: ')
    contador = 0
    for letras in oracion:
        if letras != letra_buscar:
            continue
        contador +=1
        
    print('hay ' + str(contador) + ' letras ' +"'"+str(letra_buscar + "'" + ' en la oracion') )
    print(oracion.replace(letra_buscar, letra_buscar.upper()))


if __name__ == '__main__':
    run()
