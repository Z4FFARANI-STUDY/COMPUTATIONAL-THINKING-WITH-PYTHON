# matriz = [[i + j * 2 + 1 for i in range(2)] for j in range(3)]
# print(matriz)


# contador = 0
# matriz = []
# for l in range(3):
#     lista = []
#     for c in range(2):
#         contador += 1
#         lista.append(contador)
#     matriz.append(lista)
# print(matriz)


obj = [
    [1,2,3],
    [2,1,3],
    [3,1,2]    
]
matriz = []
for l in obj:
    lista = []
    for c in l:
        if c % 2 == 0:
            lista.append(c)
    matriz.append(lista)
print(matriz)
