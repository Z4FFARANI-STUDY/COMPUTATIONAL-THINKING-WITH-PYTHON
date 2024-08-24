c = 3
l = 2

def cria_matriz(c, l):
    matriz = []
    for j in range(l): #Passa pela quantidade de linhas da variável "l"
        linha = []
        for i in range(c): #Passa pela quantidade de colunas da variável "c"
            linha.append(int(input(":")))
        matriz.append(linha)
    return matriz
