import matplotlib.pyplot as plt

# Criação de tabuleiro com list comprehension
linha = 8
coluna = 8
xadrez = [[[255 * ((i+j) % 2), 255 * ((i+j) % 2), 255 * ((i+j) % 2)] for i in range(coluna)] for j in range(linha)]

plt.imshow(xadrez)
plt.axis('off')
plt.show()


# Caixa gradiente utilizando laço de repetição
# linha = 8
# coluna = 8
# matriz =[]
# condicao = True

# for j in range(linha):
#     linha = []
#     for i in range(coluna):
#         cor = []
#         for k in range(3):
#             if condicao:
#                 elemento = 0
#             else:
#                 elemento = 255
#             cor.append(elemento)
#         condicao = not condicao
#         linha.append(cor)
#     condicao = not condicao
#     matriz.append(linha)
# print(matriz)

# plt.imshow(matriz)
# plt.axis('off')
# plt.show()
