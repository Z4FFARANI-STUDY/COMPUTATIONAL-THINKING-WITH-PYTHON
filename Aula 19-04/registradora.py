msg = '''
Código: | Preço:
  1     | 0,50
  2     | 1,00
  3     | 4,00
  5     | 7,00
  9     | 8,00
'''

print(msg)
c = 2

while c != 0:
  a = int(input("Código: "))
  b = int(input("Quantidade: "))
  c = int(input("Adicionar (1), parar (0): "))
  d = 0
  e = a + d
    
  if a == 1:
    d = b * 0.5
  elif a == 2:
    d = b * 1
  elif a == 3:
    d = b * 4
  elif a == 5:
    d = b * 7
  elif a == 9:
    d = b * 8
  else:
    int(input("Código inválido."))
    break
    
print(f"Você pagará por R${e}")

