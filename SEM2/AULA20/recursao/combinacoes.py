# Número de combinações de m objetos n a n

def combinacoes(m, n):
    if n == 0:
        return 1
    elif m == n:
        return 1
    elif m < n:
        return 0
    elif m > n and m > 0 and n > 0:
        return combinacoes(m - 1, n) + combinacoes(m - 1, n - 1)

print(combinacoes(10, 5))