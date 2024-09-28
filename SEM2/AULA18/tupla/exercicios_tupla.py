# Adicionar elementos de uma tupla
# tupla1 = (1, 2, 3)
# a = input('Digite o elemento a ser adicionado na tupla: ')
# a = tuple([a])
# tupla1 += a
# print(tupla1)


# Remover elementos de uma tupla. Função tuple transforma em tupla
tupla2 = (1, 2, 3, 4, 5)
rem = 4
tupla2 = list(tupla2)

# Laço que passa por índice e valor da lista. Passa enumerando porque números estão em tupla
for i, j in enumerate(tupla2):
    if j == rem:
        tupla2.pop(i)
print(tuple(tupla2))
