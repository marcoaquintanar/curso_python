#Cálculo de coordenadas de líneas
from funciones import calcular_y

def calcular_y(x, m, b):

    return m*x +b

def main():
    m=2
    b=3
    X=[x for x in range(1,11)]
    Y= [funciones.calcular_y(x,m,b) for x in X]
    coordenadas_enteros = list(zip(X,Y))
    print(coordenadas_enteros)
    print(f'Para x = {x}, y = {y}')

if __name__ == '__main__':
    main()