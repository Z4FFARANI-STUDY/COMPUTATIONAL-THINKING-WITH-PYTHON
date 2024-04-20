# Encontrar números pares entre um intervalo de números decretado pelo usuário

n1 = int(input('Número inicial: '))
n2 = int(input('Número final: '))
soma = 0

while n1 <= n2:
    if n1 % 2 == 0:
        soma = soma + n1
        print(n1)
    n1 = n1 + 1

print(soma)






