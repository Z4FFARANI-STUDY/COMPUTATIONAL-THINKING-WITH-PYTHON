def cria_matriz():
    c = 3
    l = 2

    matriz = []
    for j in range(l):
        linha = []
        for i in range(c): 
            linha.append(i + 1 + j * c)
        matriz.append(linha)
    return matriz

print(cria_matriz())
