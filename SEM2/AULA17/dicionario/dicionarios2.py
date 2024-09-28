loja = {
    'banana': 'amarelo',
    'uva': 'verde',
    'laranja': 'laranja'
}

# lojaB = loja
# print(loja)
# print(lojaB)
# loja['banana']  = 'verde'
# print(loja)
# # print(lojaB)

# Cria um novo dicionário, não sendo afetando pelas alterações da loja
lojaB = loja.copy()
loja['banana'] = 'mudou!'
print(lojaB)
print(loja)