estoque_atual = {'camisa': 5, 'calça': 3, 'sapato': 2}
novos_itens = {'camisa': 2, 'calça': 1, 'boné': 4}

def atual_estoque(estoque_atual, novos_itens):
# Não precisa de keys, mas é certeza
    for i in novos_itens.keys():
        if i in estoque_atual:
            estoque_atual[i] += novos_itens[i]
        else:
            estoque_atual[i] = novos_itens[i]
    return estoque_atual

print(atual_estoque(estoque_atual, novos_itens))