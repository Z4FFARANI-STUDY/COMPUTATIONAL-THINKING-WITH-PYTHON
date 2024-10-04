a = [7,3,9,0,1,2]
print(a)

# Ordenação imitando função bubble sort
for iteracao in range(len(a) - 1, 0, -1):
    for i in range(iteracao):
        if a[i] > a[i + 1]:
            aux = a[i]
            a[i] = a[i +1 ]
            a[i + 1] = aux
    print(iteracao)
    print(a)
