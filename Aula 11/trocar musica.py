musica = "O SAPO NAO LAVA O PE NAO LAVA PORQUE NAO QUER ELE MORA LA NA LAGOA NAO LAVA O PE PORQUE NAO QUER MAS QUE CHULE!"
vogal = "A"
lismus = list(musica)
texto_final = ""

for i in range(len(lismus)):
    if lismus[i] == "A" or lismus[i] == "E" or lismus[i] == "I" or lismus[i] == "O" or lismus[i] == "U":
        texto_final += vogal
    else:
        texto_final += lismus[i]
print(texto_final)

