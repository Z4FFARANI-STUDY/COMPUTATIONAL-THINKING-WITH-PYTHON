p = int(input('Sua idade: '))
c = str(input('Você tem carteira de estudante (SIM ou NÃO)? ')).upper()

if p >= 65 or p <= 21:
    print('Você tem direito a meia-entrada.')

elif c == "SIM" or c == "S":
    print('Você tem direito a meia-entrada')

else:
    print('Você pagará inteira.')