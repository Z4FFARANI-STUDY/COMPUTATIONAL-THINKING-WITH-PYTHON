# Caso Base: É a condição que para a recursão. Ele determina quando a função deve parar de se chamar. Sem um caso base, a recursão continuaria indefinidamente, levando a um erro de estouro de pilha.

# Caso Recursivo: É a parte da função que chama a si mesma, geralmente reduzindo o problema a um ou mais subproblemas menores. Aqui, a função processa a entrada e faz a chamada recursiva até atingir o caso base.

def soma(lista):
    if len(lista) == 1:
        return lista[0]
    return lista[0] + soma(lista[1:]) 

lista = [1, 3, 5, 7, 9]

print(soma(lista))