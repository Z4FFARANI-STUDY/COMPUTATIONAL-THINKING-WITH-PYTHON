# Tuplas é uma lista imutável.
# tupla = tuple([1,2,3,4,5])
# print(tupla)

# tupla = (1)
# print(type(tupla))

# # Uma vez criada, os conteúdos dentro dela não podem ser mudados
# tupla = (1,2,3,4,5)
# tupla[0] = 0

# Concatenação de tuplas
# tupla1 = (1,2,3)
# tupla2 = (4,5,6)
# tupla3 = tupla1 + tupla2
# print(tupla3)

# Percorrendo tuplas
# for i in tupla3:
#     print(i)

# Atribuição de variáveis de forma simultânea
# x, y, z = 1, 2, 3
# print(x, y, z)

# Coletar dado de usuário com função split
# nome, sobrenome = input('Digite seu nome e sobrenome: ').split()
# print(nome, sobrenome)

# Enumeração de elementos presentes em uma lista ou tupla
# lista = ['Ronaldo', 10, '1.56', True]
# for i in enumerate(lista):
#     print(f'index + valor: {i}')

# List comprehension
# lista = tuple(i for i in range(10))
# print(lista)