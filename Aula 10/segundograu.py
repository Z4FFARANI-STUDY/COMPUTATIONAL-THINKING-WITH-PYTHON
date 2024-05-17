def raiz(a, b, c):
    delta = b**2 - 4 * a *c
    x1 = (-b + delta**(1/2))/(2 * a)
    x2 = (-b - delta**(1/2))/(2 * a)
    return x1, x2

print(raiz(2, -3, 1))
