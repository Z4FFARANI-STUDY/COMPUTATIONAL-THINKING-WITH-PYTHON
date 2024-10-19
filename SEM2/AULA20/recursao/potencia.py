def potencia(n, p):
    if p == 1:
        return n
    elif p == 0:
        return 1
    # p é uma espécie de contador
    return n * potencia(n, p - 1)

print(potencia(3, 3))