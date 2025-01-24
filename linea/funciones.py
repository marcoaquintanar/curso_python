# archivo con todas las funciones necesariase para la aplicacion "linea"

def calcular_y(x, m, b):

    return m*x +b

def test_linea():
    '''
    Prueba de funcionamiento de calcular_y
    '''
    assert calcular_y(0, 2, 3) == 3

    if __name__ == '__main__':
        test_linea()
        print('Todo bracamonte')
    else:
        print('Algo salio mal')