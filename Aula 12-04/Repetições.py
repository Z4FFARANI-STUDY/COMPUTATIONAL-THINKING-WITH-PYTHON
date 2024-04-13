a = int(input('Número 1 crescente: '))
b = int(input('Número 2 final crescente: '))

while a < b + 1:
    print(a)
    a = a + 1

#ou, em ordem decrescente

a1 = int(input('Número 1 decrescente: '))
b2 = int(input('Número 2 final decrescente: '))

while a > b - 1:
    print(a)
    a = a - 1

#ou, printar os pares, ou ímpares
    
a = 0

while a < b + 2:
    print(a)
    a = a + 2

#ou, printar e dizer que é par

a = 1
while a < 101:
    if a%2 == 0:
        print(f'{a} é par')
    else:
        print(f'{a} é ímpar')
    a = a + 1