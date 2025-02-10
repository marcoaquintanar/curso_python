import random

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

def juego(simbolos:dict,nombres:dict):
    '''juego de gato'''
    lista_combinaciones = [
        ['1','2','3'],
        ['4','5','6'],
        ['7','8','9'],
        ['1','4','7'],
        ['2','5','8'],
        ['3','6','9'],
        ['1','5','9'],
        ['3','5','7']
    ]
    en_juego = True
    gana = None
    movimientos = 0
    dibuja_tablero(simbolos)
    while en_juego:
        usuario(simbolos)
        dibuja_tablero(simbolos)
        movimientos += 1
        gana = checa_winner(simbolos,lista_combinaciones)
        if gana is not None:
            en_juego = False
            continue
        if movimientos >= 9:
            en_juego = False
            continue
        ia(simbolos)
        dibuja_tablero(simbolos)
        movimientos += 1
        gana = checa_winner(simbolos,lista_combinaciones)
        if gana is not None:
            en_juego = False
            continue
        if movimientos >=9:
            en_juego = False
            continue
    return gana


def checa_winner(simbolos:dict, combinaciones: list):
    '''Checa si hay un ganador '''
    for c in combinaciones:
        if simbolos[c[0]] == simbolos[c[1]] == simbolos[c[2]]:
            return simbolos[c[0]]
    return None

def actualiza_score(score:dict,ganador:str,nombres:dict):
    '''Actualiza el score'''
    X = score["X"]
    O = score["O"]
    if ganador is not None:
        print(f'El ganador es {nombres[ganador]}')
        if ganador == 'X':
            X["G"] += 1
            O["P"] += 1
        elif ganador == '0':
            O["G"] += 1
            X["P"] += 1
        else:
            O["E"] += 1
            X["E"] += 1
    else:
        print('Empate')
        O["E"] += 1
        X["E"] += 1

def despliega_tablero(score:dict, nombres:dict):
    ''' Despliega el tablero de score '''
    print(f'''
    {nombres['X']} | G: {score['X']['G']} | P: {score['X']['P']} | E: {score['X']['E']}
    {nombres['O']} | G: {score['O']['G']} | P: {score['O']['P']} | E: {score['O']['E']}
    ''')