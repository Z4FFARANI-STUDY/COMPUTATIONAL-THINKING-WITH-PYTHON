# Operação para encontrar um número amigo:
def divisores(n):
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma += i
    return soma

# a e b substituem n:
def amigos(a, b):
    if divisores(b) == a and divisores(a) == b:
        return "Números amigos"
    else:
        return "Números não amigos"

print(divisores(220))
print(amigos(284, 220))