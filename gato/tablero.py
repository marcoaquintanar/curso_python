'''
tablero.py: Dibuja el tablero del juego de el gato
'''

def dibuja_tablero(simbolos:dict):
    '''
    Dibuja el tablero del juego de el gato 
    Recibe: nafa
    Regresa: nada
    '''

    print(f'''
        {simbolos['1']} | {simbolos['2']} | {simbolos['3']}
        ---------
        {simbolos['4']} | {simbolos['5']} | {simbolos['6']}
        ---------
        {simbolos['7']} | {simbolos['8']} | {simbolos['9']}
        ''' )
    
def ia(simbolos:dict):
    ''' Juega la maquina'''
    ocupado = True
    while ocupado == True:
        x = random.choice(list(simbolos.keys()))
        if simbolos[x] not in ['X','O']:
            simbolos[x] = 'O'
            ocupado = False
    
def usuario(simbolos:dict):
    ''' Juega el usuario'''
    ocupado = True
    while ocupado == True:
        numeros = [str(i) for i in range(1,10)]
        x = input('Ingresa el el numero de la casilla: ')
        if(x in numeros):
            if simbolos[x] not in ['X','O']:
                simbolos[x] = 'X'
                ocupado = False
        else:
            print('Numero no valido')
    
import random    
if __name__ == '__main__':

    numeros = [str(i) for i in range(1, 10)]
    dsimbolos = {x:x for x in numeros}
    dibuja_tablero(dsimbolos)
    ia(dsimbolos)
    #x = random.choice(numeros)
    #numeros.remove(x)
    #dsimbolos[x] = 'X'
    dibuja_tablero(dsimbolos)
    usuario(dsimbolos)
    dibuja_tablero(dsimbolos)
    #o = random.choice(numeros)
    #numeros.remove(o)
    #simbolos[o] = 'O'
    #dibuja_tablero(dsimbolos)
    #print(numeros)