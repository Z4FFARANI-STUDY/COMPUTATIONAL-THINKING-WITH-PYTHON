dict = {
    'Carro': 'BMW',
    'Propriedade': {'Motor': '300cv',
                    'Valor': 100000,
                    'Ar': True
                    }
}
# Troca de elemento a partir da chave 'Carro'
dict['Carro'] = 'Ferrari'

# Busca por uma chave
print(dict.get('Modelo'))
print('Modelo' in dict)


# dictA = {
#     'Carro': 'BMW',
#     'Propriedade': 'Porta',
#     'Ar': False,
#     (1,0,1): (3.5)
# }

# # remove a chave 'Carro' do dicionário
# print(dictA.pop('Carro'))
# # print(list(dictA.items()))
# dictA['Carro'] = 'Ferrari'
# # print(dictA)

# for i in dictA.values():
#     print(i)

# for i, j in dictA.items():
#     print(f'Chave {i}; Valor {j}')


# dictB = {
#     'Propriedade': 'Janela',
#     'Ar': True
# }

# # Subscreve os elementos / adiciona em outro dicionário
# dictA.update(dictB)
# print(dictA)
