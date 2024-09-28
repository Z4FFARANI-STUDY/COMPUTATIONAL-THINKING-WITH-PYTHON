# Tipo e o id do Pokémon na pokedex consumindo uma API
# https://pokeapi.co/api/v2/pokemon/

import requests

pokemon = 'pikachu'
url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
r = requests.get(url)
lista = r.json()

print(lista['id'], lista['types'][0]['type']['name'])

pokemon = 'pikachu'

print(f'O id do {pokemon} é {lista['id']}.')
print(f'{pokemon} é do tipo {lista['types'][0]['type']['name']}!')