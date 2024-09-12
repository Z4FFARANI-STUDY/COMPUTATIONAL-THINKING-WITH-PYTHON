# obj1 = [
#     [1,2,3],        
#     [1,2,3],        
#     [1,2,3]        
# ]

# obj2 = [
#     [1,2,3],        
#     [2,2,3],        
#     [1,2,3]        
# ]

# matriz1 = []
# matriz2 = []

# for i in obj1:
#     soma1= sum(i)
#     matriz1.append(soma1)
#     t1 = sum(matriz1)

# for j in obj2:
#     soma2 = sum(j)
#     matriz2.append(soma2)
#     t2 = sum(matriz2)
    
# multi = t1 * t2

# print(multi)


obj1 = [
    [1, 2, 3],        
    [1, 2, 3],        
    [1, 2, 3]        
]

obj2 = [
    [1, 2, 3],        
    [2, 2, 3],        
    [1, 2, 3]        
]

def soma_matriz(matriz):
    return sum(sum(linha) for linha in matriz)

t1 = soma_matriz(obj1)
t2 = soma_matriz(obj2)

multi = t1 * t2
print(multi)

