equipes = [('Equipe A', 85), ('Equipe B', 90), ('Equipe C', 80), ('Equipe D', 95), ('Equipe E', 88)]

def ordena(a):
    for lista in range(len(a) - 1, 0, -1):
        for i in range(lista):
            if a[i][1] > a[i + 1][1]:
                aux = a[i]
                a[i] = a[i + 1]
                a[i + 1] = aux
    return a

print(ordena(equipes))