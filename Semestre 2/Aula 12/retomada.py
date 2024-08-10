n = int(input("Digite o número de linhas para a árvore: "))
vezes = 0
asterisco = "*"
espaco = " " * n
vao = n

while vezes != n:
    print(espaco + asterisco)
    asterisco += "**"
    vao -= 1
    espaco = " " * vao
    vezes += 1


# n = 3
# for i in range(n):
#     print(f"{' ' * (n - i - 1)}{'*' * (2 * i + 1)}")

    