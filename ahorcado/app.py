'''
Programa principal del juego ahorcado
'''
import funciones as fn
from random import choice
import string

def main(archivo_texto:str,nombre_plantilla='plantilla'):
    '''
    Progama principal
    '''
    # cargamos las plantillas
    plantillas = fn.carga_plantillas('plantilla')
    lista_oraciones = fn.carga_archivo_texto(archivo_texto)
    palabras = fn.obten_palabras(lista_oraciones)
    o = 0 # oportunidadep 
    p = choice(palabras)
    abcdario = {letra:letra for letra in string.ascii_lowercase}
    adivinadas = set()
    while o > 1:
        fn.despliega_plantilla(plantillas, o)
        fn.adivina_letra(abcdario, p, adivinadas, o)
        if p == ''.join([letra if letra in adivinadas else'_' for letra in p]):
            print('Ganaste')
            break
        o -= 1

if __name__ == '__main__':
    archivo = './datos/pg15532.txt'