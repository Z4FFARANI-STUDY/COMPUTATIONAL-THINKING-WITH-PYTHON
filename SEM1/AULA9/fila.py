fila = []
while True:
    acao = input("Digite A para adicionar na fila ou R para remover da fila: ")
    if acao == "A":
        nome = input("Digite o nome da pessoa: ")
        fila.append(nome)
    elif acao == "R":
        rem = fila.pop(0)
        print(f"{rem} foi atendido!")
        print(f"O tamanho da fila é de {len(fila)} pessoas.")
    else:
        print("Comando inválido.")
    
    print(fila)
    
    enc = input("Deseja encerrar a fila? (S para encerrar): ").upper()
    
    if enc == "S":
        break 

print(fila)

