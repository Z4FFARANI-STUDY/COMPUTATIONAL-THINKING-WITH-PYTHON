n = int(input("Digite o valor do fatorial desejado: "))
i = 1
fat = 1

while i <= n:
    fat *= i
    i += 1

print(fat)