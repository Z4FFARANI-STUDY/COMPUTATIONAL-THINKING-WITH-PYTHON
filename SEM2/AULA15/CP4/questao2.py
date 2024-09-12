def le_matriz(l, c):
    matriz = []
    for j in range(l):
        linha = []
        for i in range(c):
            linha.append(int(input(f'Matriz[{j}][{i}]: ')))
        matriz.append(linha)
    return matriz

print(le_matriz(3,3))