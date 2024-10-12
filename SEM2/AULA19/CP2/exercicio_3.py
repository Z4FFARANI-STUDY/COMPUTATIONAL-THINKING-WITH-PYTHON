lista = [1, 2, 3, 50, 100, 'maria', 'joao']
aux = 50

def busca(lista, aux):
    # Trazendo o elemento e o índice
    for i, j in enumerate(lista):
        if j == aux:
            return i
    return -1

print(busca(lista, 'maria'))
