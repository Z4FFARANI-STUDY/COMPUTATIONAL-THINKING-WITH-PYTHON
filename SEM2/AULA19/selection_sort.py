a = [12, 68, 95, 41, 10, 71]

def menor_index(index, a):
    menor = index
    for i in range(index + 1, len(a)):
        if a[menor] > a[i]:
            menor = i
    return menor

for i in range(len(a) - 1):
    menos = menor_index(i, a)
    aux = a[menos]
    a[menos] = a[i]
    a[i] = aux
    print(a)