frase = 'Kaique'

contagem = {}
for i in frase:
    print(i)
    # Se o caractere ainda ou não existe no dicionário
    if not i in contagem:
        contagem[i] = 1
    else:
        contagem[i] += 1

print(contagem)