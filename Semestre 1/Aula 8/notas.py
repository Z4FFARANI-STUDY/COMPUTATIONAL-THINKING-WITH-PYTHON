notas = []
continuar = "S"
media = 0
soma = 0

while continuar == "S":
    add = int(input("Nota: "))
    notas.append(add)
    soma = soma + add
    media += 1
    continuar = str(input("Continuar <S>: ")).upper()

print(f"Notas: {notas}")
print(f"Média: {soma / media}")