import math
import os 

#definimos la funcion de la suma de los elementos de la matriz 
def simpleArraySum(ar):
    suma = sum(ar)
    return suma

#definimos el tamaño y la longitud que es la raiz cuadrada de los elementos de la matriz
tamaño = int(input("\nIntroduzca el tamaño de la matriz: "))
longitud = int(math.sqrt(tamaño))

#input para pedir los elementos 
elementos = input("\nIntroduzca los elementos dentro de la matriz separados por espacios:")
ar = list(map(int, elementos.split())) #hacemos de los elementos una lista 

#verificamos que la matriz es cuadrada
if longitud * longitud == tamaño:
    matriz = [ar[i:i+longitud] for i in range(0, len(ar), longitud)]#creamos una matriz bidimensional usando el indice

    if all(len(fila) == longitud for fila in matriz):
        result = simpleArraySum(ar)
        print("\nLa matriz es:")
        for fila in matriz: #
            print(fila)
        print("\nLa suma de la matriz es:", result)
        nombre_archivo = "resultado.txt"
        with open(nombre_archivo, 'w') as fptr:
            fptr.write(str(result) + '\n')

        print(f"\nEl resultado se ha escrito en '{nombre_archivo}'.")
    else:
        print("\nError, la matriz no es cuadrada.")
else:
    print("\nError, el tamaño no es cuadrado.")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write(str(result) + '\n')
    fptr.close()