# lista = []
# continuar = "S"
# add = 0
# while continuar == "S":
#     n = int(input("Número: "))
#     add += n
#     lista.append(n)
#     continuar = str(input("Continuar <S> Parar <P>: ")).upper()
# media = add / len(lista)
# print(media)

n = int(input("Digite a quantidade de números: "))
lista = []
for i in range(n):
    lista.append(float(input("Digite a nota: ")))
print(lista)

soma = 0
for j in lista:
    soma += j
print(soma / len(lista))
