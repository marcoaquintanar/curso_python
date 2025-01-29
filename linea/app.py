from funciones import calcular_y
import argparse
<<<<<<< HEAD
import matplotlib.pyplot as plt
 
def main(m,b):
=======
 
def main(m,b):
>>>>>>> 533c5084ed5438540cec236f0a7cbf1fde0e2aff
    #X=[ x for x in range(1,11)]
    #Y=[calcular_y(x,m,b) for x in X]
    #print(f"Enteros:")
    #cordenadas_enteros= list(zip(X,Y))
    #print(cordenadas_enteros)
    XF = [x/10.0 for x in range(10,110,5)]
    YF =[calcular_y(x,m,b) for x in XF]
    coordenadas_flotantes = list(zip(XF,YF))
    print("Flotantes:")
    print(coordenadas_flotantes)
<<<<<<< HEAD
    plt.plot(XF,YF)
   
 
=======
    funciones.grafica_lineas(XF,YF, m, b)
   
 
>>>>>>> 533c5084ed5438540cec236f0a7cbf1fde0e2aff
if __name__ == '__main__':
<<<<<<< HEAD
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", type=float, help='Pendiente De La Linea', default=2.0)
    parser.add_argument('-b', type=float, help='Ordenada al origen', default=3.0)
=======
<<<<<<< HEAD
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", type=float, help='Pendiente De La Linea', default=2.0)
    parser.add_argument('-b', type=float, help='Ordenada al origen', default=3.0)
    args = parser.parse_args()
    main(args.m,args.b)
=======
    parser = args.parser.ArgumentParser()
    parser.add_argument('-m', type=float,
    help='Pendiente de la linea')
    parser.add_argument('-b', type=float,
    help='Ordenada al origen', default=3.0)
>>>>>>> 533c5084ed5438540cec236f0a7cbf1fde0e2aff
    args = parser.parse_args()
<<<<<<< HEAD
    main(args.m,args.b)
=======
    main(args.m, args.b)
    main(m=2.0, b=3.0)
    
>>>>>>> 4b17cfb559f451f2c70f508945d345855d60f61a

>>>>>>> 533c5084ed5438540cec236f0a7cbf1fde0e2aff