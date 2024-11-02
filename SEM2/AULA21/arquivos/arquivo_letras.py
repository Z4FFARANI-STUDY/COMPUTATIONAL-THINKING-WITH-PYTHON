arquivo = open('COMPUTATIONAL-THINKING-WITH-PYTHON/SEM2/AULA21/arquivos/arquivo_letras.txt', 'r+', encoding='UTF-8')

texto = ''

while True:
    carac = arquivo.read(1)
    if carac == 'a':
        texto += 'A'
    else:
        texto += carac
    if carac == '':
        break

arquivo.seek(0, 0)
arquivo.write(texto)




