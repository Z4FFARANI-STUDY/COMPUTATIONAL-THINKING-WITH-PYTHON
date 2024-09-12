# Exercicio 1
def maior_elemento(a, b, c):
    maior = a
    if b > maior:
        maior = b
    if c > maior:
        maior = c
    return maior


# Exercicio 2
def fat(n):
    fat = 1
    for i in range(1, n + 1):
        fat *= i
    return fat


# Exercicio 3
def calculadora(x, y, op):
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*":                                
        return x * y
    elif op == "/":
        return x / y


# Exercicio 4
def pitagorico(a, b, n):
    return a**2 + b**2 == n
