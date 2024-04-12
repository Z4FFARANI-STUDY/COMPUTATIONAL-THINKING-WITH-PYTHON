print(52*'*')
print(5*'*', 'Olá, seja muito bem-vindo a Frutaria ES!')
print(52*'*')

nome = input('Para começarmos, por favor, diga o seu nome: ')
endereco = input(f'{nome}, diga o seu endereço: ')
ano = int(input(f'{nome}, diga o ano do seu nascimento: '))
idade = 2024 - ano


msg='''
-----------------------
|Fruta       | R$/kg  |
-----------------------

|Banana       | 10.50 |
|Uva          | 3.50  |
|Maçã         | 8.50  |
|Melancia     | 20.50 |
|Kiwi         | 35.40 |
'''

banana = 10.5
uva = 3.50
maca = 8.50
melancia = 20.50
kiwi = 35.40


print()
print(f'{nome}, As opções de fruta do dia, são: ')


print(41*'-')
print('|Id', '|', f'{"Fruta":14s}', '|', f'{"R$/kg":15s}')
print(41*'-')
print('|', '1', '|', f'{"Banana":15s}', '|', f'{banana:15.2f}', '|')
print('|', '2', '|', f'{"Uva":15s}', '|', f'{uva:15.2f}', '|')
print('|', '3', '|', f'{"Maçã":15s}', '|', f'{maca:15.2f}', '|')
print('|', '4', '|', f'{"Melancia":15s}', '|', f'{melancia:15.2f}', '|')
print('|', '5', '|', f'{"Kiwi":15s}', '|', f'{kiwi:15.2f}', '|')
print(41*'-')


id = input('Escolha o ID da fruta que você deseja: ')
peso = float(input('Qual é a quantidade (em kg) que você deseja? '))


if id == '1':
    valor = peso*banana
elif id == '2':
    valor = peso*uva
elif id == '3':
    valor = peso*maca
elif id == '4':
    valor = peso*melancia
elif id == '5':
    valor = peso*kiwi

else:
    print('Escolha inválida.')


frete = 4
if valor < 15:
    valor = valor + frete
else:
    print(f'{nome}, você está isento(a) do frete!')


if idade > 60:
    print('{nome}, o(a) Sr(a), tem um desconto de 5%.')
    valor = valor * 0.95


print()
print(f'Muito obrigado, {nome}, sua compra ficou no valor de R${valor:.2f} e será entregue no endereço: {endereco}')