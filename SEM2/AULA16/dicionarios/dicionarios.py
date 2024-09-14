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

# print(dict.pop('Carro'))
# # print(dict)
# # print(list(dict.items()))
# dict['Carro'] = 'Ferrari'
# # print(dict)

# for i in dict.values():
#     print(i)

# for i, j in dict.items():
#     print(f'Chave {i}; Valor {j}')


dictB = {
    'Propriedade': 'Janela',
    'Ar': True
}

# Subscreve os elementos / adiciona em outro dicionário
dictA.update(dictB)
print(dictA)