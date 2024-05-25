# def calcular_pi(numero_de_termos):
#     soma = 0
#     for n in range(numero_de_termos):
#         termo = ((-1) ** n)/(2 * n + 1)
#         soma += termo
#     pi = 4 * soma
#     return pi

# numero_de_termos = 1000000
# pi_aproximado = calcular_pi(numero_de_termos)
# print(pi_aproximado)


def pi(loop):
    sum = 0
    for n in range(loop):
        sum += 2*3**(0.5)*(-1)**n / (3**n*(2*n+1))
    return sum


def fat(n):
    fat = 1
    for i in range(1, n + 1):
        fat *= i
    return fat


def sin(x, loop):
    sum = 0
    for n in range(loop):
        sum += (-1)**n*x**(2*n+1) / fat(2*n+1)
    return sum


def cos(x, loop):
    sum = 0
    for n in range(loop):
        sum += (-1)**n*x**(2*n) / fat(2*n)
    return sum


def tan(x, loop):
    return sin(x, loop) / cos(x, loop)


print(tan(pi(50)/4, 50))