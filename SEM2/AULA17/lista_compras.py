supermercado = {
    'amaciante': 4.99,
    'arroz': 10.90,
    'biscoito': 1.69,
    'cafe': 6.98,
    'chocolate': 3.79,
    'farinha': 2.99
}

lista_compras = ['biscoito', 'chocolate', 'farinha']

valor = 0
for i in lista_compras:
    # Se o título, pois o i já está em uma camada
    if i in supermercado:
        valor += supermercado[i]

print(valor)
