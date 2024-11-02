try:
    lista = [1, 2, 3]
    a = 0
    for i in range(5):
        a += lista[i]
except IndexError as e:
    print(e)