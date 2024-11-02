arquivo = open('COMPUTATIONAL-THINKING-WITH-PYTHON/SEM2/AULA21/arquivos/arquivo_binario/arquivo_notas.txt', 'r')

arq = arquivo.read()
b = arq.split('\n')

def nome_notas(d):
    c = d.split(' ')
    nome = c[0]

    maior = 0
    menor = 10

    for i in c[1: ]:
        if int(i) > maior:
            maior = int(i)
        if int(i) < menor:
            menor = int(i)

    return nome, maior, menor

for j in b:
    print(nome_notas(j))

arquivo.close()
