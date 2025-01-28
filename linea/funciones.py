#Archivo con todas las funciones necesarias para la aplcacion linea
import matplotlib.pyplot as plt
def calcular_y(x:float,m:float,b:float)->float:
    return m*x +b

def test_lineas():
    assert calcular_y(0,2,3) == 3

def grafica_lineas(X: list, Y: list, m, b):
    plt.plot(X,Y)
    plt.title(f'Linea con pendiente {m} y ordenada en el origen {b}')
    plt.xlabel('X')
    plt.xlabel('Y')
    plt.show()

if __name__ == '__main__':
    if test_lineas():
        print('Todo bien')
    else:
        print("Todo mal :(")
