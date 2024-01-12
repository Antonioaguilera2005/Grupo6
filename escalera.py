def staircase(n):
    for i in range(1, n +1):
        spaces = ' ' * (n - i)
        hashtags = '#' * i 
        print(spaces + hashtags)
        
if __name__ == '__main__':
    n = int(input("Ingrese el tamaño de la escalera: ").strip())
    staircase(n)