# Faça um programa que leia uma quantidade x de valores, em que x é um número que o usuário irá digitar

x = int(input("Defina quantidade de valores desejados: "))
numeros = x
qtd = 0
soma = 0

while qtd < x:
    valor = float(input("Digite um valor: "))
    x = x - 1
    soma = soma + valor
    
media = soma / numeros
print(f"A média das notas é {media:.2f}")
   
