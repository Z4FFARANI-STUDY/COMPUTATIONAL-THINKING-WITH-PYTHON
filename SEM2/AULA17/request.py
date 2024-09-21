# Importação da biblioteca requests
import requests

url = 'https://viacep.com.br/ws/37044150/json/'

r = requests.get(url)

# Tranformação de conteúdo em json, para estar como dicionário
cep = r.json()
print(cep)

# Busca como dicionário
print(cep['bairro'])