# O asterisco considera todos os parâmetros. Basicamente, movendo para uma tupla. 

def soma(*params):
    res = 0
    for i in params:
        res += i
    return res


quantidade = int(input("Quantidade de parâmetros: "))
limite = 0
lista = []

while limite < quantidade:
    valores = int(input("Digite os valores: "))
    lista.append(valores)
    limite += 1
    if limite == quantidade:
        print(soma(*lista))
        


qtde = int(input("Digite a quantidade de valores que deseja somar: "))

valores = []
for i in range(qtde):
    valores.append(float(input("Digite o valor: ")))

print(soma(*valores))
        

        


    
