# nomes = ['Joao', 'Henrique', 'Julia']
# idade = [10, 11, 12]
# print(dict(zip(nomes, idade)))

cadastro = {}
qtde = int(input('Digite a qtde de nomes para cadastro: '))

for i in range(qtde):
    nome = input('Digite o nome: ')
    idade = input("Digite sua idade: ")
    sexo = input('Digite F/M: ')

    cadastro[nome] = {'idade': idade, 'sexo': sexo}

print(cadastro)