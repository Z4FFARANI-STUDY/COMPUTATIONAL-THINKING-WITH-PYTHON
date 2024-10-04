# DICIONARIO
# dict.copy() só clona, for i[:] in dict_b cria um único
# get('chave')

# chave = ['carlos', 'ana', 'luisa']
# valor = ['masculino', 'feminino', 'feminino']
# dict(zip(chaves, valores)) cria um dicionário a partir de duas listas

# dict.pop('chave')
# del dict['chave']
# dict.popitem() remove a última chave-valor

# dict_a.update(dict_b) puxa as informações do dict_b

# list() 

# dict.keys()
# dict.values()
# dict.items() tudo


# TUPLA são imutáveis
# tuple()
# enumerate(lista ou dict ou tupla)


# CONJUNTOS
# set são conjuntos {} - servem para operações

# adição
# a = set()
# a.add(1)
# a.add(2)
# print(a)

# diferença -
# a = {0,1,2,3,4}
# b = {0,1,2}
# print(a-b)

# intersecção &
# a = {0,1,2,3,4}
# b = {0,1,2}
# print(a & b)

# união (em ordem)
# a = {0,2,4}
# b = {1,3,5}
# print(a | b)
# c = set([6,7,8])
# print(a | b | c)

# elementos não repetidos
# a ^ b


# ORDENAÇÃOO
# BUBBLE SORT trabalha com ordenação de elementos

# sorted(lista)

# comprimento - 1, pois o último já é o maior, indo até o primeiro
    # Pode ser range(len(a) - 1), mas será ineficiente

# def bubble_sort(a):
#     for i in range(len(a) - 1, 0, -1):
#         for j in range(i):
#             if a[j] > a[j+1]:
#                 temp = a[j]
#                 a[j] = a[j+1]
#                 a[j+1] = temp

# lista = [12, 68, 95, 41, 25, 71]

# bubble_sort(lista)
# print(lista)


# LAMBDA
# dobro = lambda x: x**4
# print(dobro(2))


# LISTA

# nome = 'Kaique'
# dict = {}
# for i in nome:
#     if not i in dict:
#         dict[i] = 1
#     else:
#         dict[i] += 1
# print(dict)