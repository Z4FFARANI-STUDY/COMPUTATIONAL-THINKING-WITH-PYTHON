arquivo = open('COMPUTATIONAL-THINKING-WITH-PYTHON/SEM2/AULA20/exercicio_arquivos/alterar_texto.txt', 'r+', encoding='UTF-8')

for i in arquivo:
    # não esquecer de reposicionar até o início do arquivo
    arquivo.seek(0)
    for j in i:
        if j == 'a':
            j = 'A'
        arquivo.write(j)
