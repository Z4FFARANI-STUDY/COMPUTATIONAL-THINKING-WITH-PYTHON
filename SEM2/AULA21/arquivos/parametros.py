# Para chamar os parâmetros, utilizar o código python .\nomedoarquivo.py parametros
# escreva em um arquivo cujo o nome do arquivo é passado como parâmetro

import sys

# Endereço do arquivo.py + parâmetro da lista
print(sys.argv[1])
arquivo = open(sys.argv[1], 'w')
