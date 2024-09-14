linha = 3
coluna = 2
# Criação de uma matriz com 2 linhas e três colunas através dos parâmetros da lambda:
matriz = lambda linha, coluna: [[int(input(': ')) for i in range(coluna)] for i in range(linha)]
# Chamada da matriz + parâmetros da lambda:
print(matriz(2, 3))

