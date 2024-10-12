# Trazendo informações de um JSON

olimpiadas = {...}

def medalhas(olimpiadas, pais):
    for i in olimpiadas['data']:
        if i['name'] == pais:
            return i['name'], i['total_medals'], i['gold_medals'], i['silver_medals'], i['bronze_medals']

print(medalhas(olimpiadas, 'China'))