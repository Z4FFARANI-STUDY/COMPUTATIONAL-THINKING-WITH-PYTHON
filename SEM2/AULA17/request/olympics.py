# Faça uma função para extrair a quantidade de medalhas total, ouro, prata e bronze do país esolhido

import requests
url = 'https://apis.codante.io/olympic-games/countries/'
r = requests.get(url)
info = r.json()

pais = 'China'
for i in info['data']:
    if i['name'] == pais:
        print('Bronze', i['bronze_medals'])
        print('Prata', i['silver_medals'])
        print('Gold', i['gold_medals'])
