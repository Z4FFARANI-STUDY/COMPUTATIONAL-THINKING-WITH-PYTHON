# variavel_arquivo = open('nome do arquivo', 'modo')

# Modos e operações:
# r - leitura
# w - escrita, apaga o conteúdo se já existir
# a - escrita, mas preserva o conteúdo se já exisitr
# b - modo binário
# + - atualização (leitura e escrita)
# É possível combinar modos

# Utilizar ou o modo 'r' ou 'w'
arquivo = open('COMPUTATIONAL-THINKING-WITH-PYTHON/SEM2/AULA20/arquivos/aula.txt', 'r', encoding = 'UTF-8')

txt = arquivo.read(3)
print(txt)

# permite mover o cursor dentro do arquivo. Respectivamente, caracteres e posição do arquivo
arquivo.seek(0, 0)
