# lista = [1, 2, "A1", 0, True, ["A2", 0, 2.4]]
# print(lista[5][0])

# obj = [
#     [3,7,1],
#     [0,9,2],
#     [2,1,1]
# ]
# print(f"{obj[0]}\n{obj[1]}\n{obj[2]}")

obj = [
    [3,7,1], [0,9,2], [2,1,1]
]

def printa(matriz):
    for linha in matriz:
        for elemento in linha:
            print(f"{elemento}", end=' ')
        print()

print(printa(obj))