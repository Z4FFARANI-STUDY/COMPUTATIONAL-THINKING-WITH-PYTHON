# Faça um exercício que o usuário vai digitar o cep dele para entrega e o programa irá escrever em tela a rua, bairo e cidade da entrega.

import requests

def correio(endereco):
    if len(endereco) < 8:
        return 'CEP inválido. Tente novamente.'
    else: 
        url = f'https://viacep.com.br/ws/{endereco}/json/'
        r = requests.get(url)
        cep = r.json()

        return f'''
Rua: {cep['logradouro']}
Bairro: {cep['bairro']}
Cidade: {cep['localidade']}
'''

print(correio('37044150'))
