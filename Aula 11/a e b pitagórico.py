n = int(input("Digite o número: "))
a = 0
b = 0

while True:
    a += 1
    b += 1

    if a**2 + b**2 == n:
        print(a, b)
        break

        