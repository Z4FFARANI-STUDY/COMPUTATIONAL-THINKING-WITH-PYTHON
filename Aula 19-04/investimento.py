# Escreva um programa que pergunte o depósito inicial, a taxa de juros mensal, o depósito mensal e o período. Mostre a evolução do saldo mês a mês.

aporte_i = float(input("Digite o depósito inicial: "))
aporte_m = float(input("Digite o depósito mensal: "))
taxa = float(input("Qaul a taxa de juros a.m? "))
meses = int(input("Digite o período do investimento: "))

a = 1
saldo = aporte_i

while a <= meses:
    saldo = (saldo + aporte_m)*(1 + taxa)
    print(f"Mês {a} - Saldo: {saldo}")
    a = a + 1