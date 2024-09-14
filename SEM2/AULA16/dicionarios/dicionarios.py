# dict = {
#     'Carro': 'BMW',
#     'Propriedade': {'Motor': '300cv',
#                     'Valor': 100000,
#                     'Ar': True
#                     }
# }
# dict['Carro'] = 'Ferrari'
# print(dict.get('Modelo'))
# print('Modelo' in dict)


dictA = {
    'Carro': 'BMW',
    'Propriedade': 'Porta',
    'Ar': False,
    (1,0,1): (3.5)
}

# print(dictA.pop('Carro'))
# # print(list(dictA.items()))
# dictA['Carro'] = 'Ferrari'
# # print(dictA)

# for i in dictA.values():
#     print(i)

# for i, j in dictA.items():
#     print(f'Chave {i}; Valor {j}')


dictB = {
    'Propriedade': 'Janela',
    'Ar': True
}

# Subscreve os elementos / adiciona em outro dicionário
dictA.update(dictB)
print(dictA)