def subtracao(a, b):
    if len(a) == len(b) and len(a[0]) == len(b[0])
    c = []
    for j in range(len(a)):
        linha = []
        for i in range(len(a[0])):
            linha.append(a[0][i] - b[0][i])
        c.append(linha)
    return c

a = [
    [5,3],
    [2,1]
]

b = [
    [1,1],
    [1,1]
]

print(subtracao(a,b))
