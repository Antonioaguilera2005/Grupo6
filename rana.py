import random

def main():
    filas = random.randint(5, 20) 
    columnas = random.randint(5, 20) 
    matriz = generar_laberinto(filas, columnas)
    print_laberinto(matriz)
    print("Probabilidad de escape: ", calcular_probabilidad_de_escape(matriz))

def generar_laberinto(filas, columnas):
    matriz = [[0] * columnas for _ in range(filas)]

    
    inicio = (random.randint(0, filas-1), random.randint(0, columnas-1))
    matriz[inicio[0]][inicio[1]] = 1

    
    fin = (random.randint(0, filas-1), random.randint(0, columnas-1))
    matriz[fin[0]][fin[1]] = 2

    return matriz

def print_laberinto(matriz):
    for fila in matriz:
        for celda in fila:
            if celda == 0:
                print("X", end=" ")
            elif celda == 1:
                print("I", end=" ")
            elif celda == 2:
                print("F", end=" ")
        print()

def calcular_probabilidad_de_escape(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    rana = {"x": -1, "y": -1}

    
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] == 1:
                rana["x"] = i
                rana["y"] = j
                break

    
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            nx, ny = rana["x"] + x, rana["y"] + y
            if 0 <= nx < filas and 0 <= ny < columnas and matriz[nx][ny] != 0:
                matriz[nx][ny] = -1

    
    adyacentes = 0
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            nx, ny = rana["x"] + x, rana["y"] + y
            if 0 <= nx < filas and 0 <= ny < columnas and matriz[nx][ny] == -1:
                adyacentes += 1

    
    return adyacentes / (filas * columnas)

main()