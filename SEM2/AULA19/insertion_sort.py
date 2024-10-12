a = [10, 12, 41, 68, 95, 21]

def insertion_sort(lista):
    for j in range(len(lista)):
        for i in range(len(lista) - 1):
            # Alternando entre índices: o anterior e o a frente. Para inverter em ordem decrescente, alterar o menor que (<) e maior que (>)
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                if a[i + 1] < a[i - 1]:
                    a[i + 1], a[i - 1] = a[i - 1], a[i + 1]
    return lista
    
print(insertion_sort(a))