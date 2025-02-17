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
    while o > 0:
        fn.despliega_plantilla(plantillas, o)
        o = fn.adivina_letra(abcdario, p, adivinadas, o)
        if p == ''.join([letra if letra in adivinadas else'_' for letra in p]):
            print('Ganaste')
            break
    print(f"La palabra era {p}")

print("Antes del main")
print(__name__)

if __name__ == '__main__':
    # archivo = './datos/pg15532.txt'
    parser.add_argument('archivo', help='Archivo de texto con palabras', default='./datos/pg15532.txt')
    args = parser.parse_args()
    archivo = args.archivo
    if os.stat(archivo).st_size == False:
        print('El archivo no existe')
        exit()
    main(archivo)