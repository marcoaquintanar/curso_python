import tablero 
import argparse

def main():
    ''' Funcion principal '''
    parser = argparse.ArgumentParser()
    parser.add_argument("--nombre", type=str, help="Nombre del usuario", default = "Usuario")
    args = parser.parse_args()

    nombre_usuario = args.nombre 
    nombres = {"X": nombre_usuario, "O": "Computadora"}
    X = {"G": 0, "P": 0, "E": 0}
    O = {"G": 0, "P": 0, "E": 0}
    score = {"X":X,"O":O}
    numeros = [str(i) for i in range(1,10)]
    corriendo = True
    while corriendo:
        dsimbolos = {x:x for x in numeros}
        g = tablero.juego(dsimbolos, nombres)
        tablero.actualiza_score(score, g, nombres)
        tablero.despliega_tablero(score, nombres)
        seguir = input('Quieres seguir jugando? (s/n): ')
        if seguir.lower() == 'n':
            corriendo = False

if __name__ == '__main__':
    main()