n = int(input("Digite o número: "))

a = 0
b = 0

while a < n:
    a += 1
    while b < n:
        b += 1
        if a**2 + b**2 == n:
            print(a, b)
            break
    b = 1
