# rb = leitura binária
# wb = escrita binária
# r+b = leitura e escrita binária

# import pickle traz a biblioteca que permite manipular arquivos binários
# pickle.dump(objeto, arquivo) escreve no arquivo
# pickle.load(arquivo) lê o arquivo

import pickle
arquivo = open('aula.bin', 'wb')

lista = [5, 10, 'ola', 10.5]

pickle.dump(lista, arquivo)

