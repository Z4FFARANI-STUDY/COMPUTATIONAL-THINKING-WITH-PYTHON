nome = 'Maria'
idade = 25
salario = 4650.37

msg = '%s tem %d anos e ganha R$%.2f' % (nome, idade, salario)
#print(msg)

msg2 = '{:-^20s} tem {} anos e ganha R${:.2f}'.format(nome, idade, salario)

print(msg2)
