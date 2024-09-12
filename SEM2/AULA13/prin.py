# Importação de todas as funções do arquivo soma.py
from soma import *
res = sum(1, 2)
print(res)

# Importação do arquivo soma.py + nomeação do arquivo para saber a função
import soma
res = soma.sum(1, 2)
print(res)

