c = 3
l = 2

def cria_matriz(c, l):
    matriz = []
    for j in range(l): #Passa pela quantidade de linhas da variável "l", que no caso são linhas de uma matriz
        linha = []
        for i in range(c): #Passa pela quantidade de colunas da variável "c", que no caso são colunas de uma matriz
            linha.append(int(input(":")))
        matriz.append(linha)
    return matriz
