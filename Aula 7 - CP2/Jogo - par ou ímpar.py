while True:
    # Paridade do jogador 1
    while True:
        p1p = input("Escolha <P> para par ou <I> para ímpar : ").upper()
        if p1p == "P" or p1p == "I":
            break

    # Paridade do jogador 2
    if p1p == "P":
        p2p = "I"
    else:
        p2p = "P"

    # Escolha dos números dos jogadores
    p1 = int(input("Digite seu número (jogador 1): "))
    p2 = int(input("Digite seu número (jogador 2): "))
    soma = p1 + p2

    # Resultados
    print(f"A soma dos número é {soma}.")

    if soma % 2 == 0:
        resultado = "P"
        print("O resultado é par.")
    else:
        resultado = "I"
        print("O resultado é ímpar.")

    if p1p == resultado:
        print("O jogador 1 é o vencedor!")
    else:
        print("O jogador 2 é o vencedor!")
    
    cod = input("Digite <S> para sair ou qualquer tecla para jogar novamente: ").upper()
    if cod == "S":
        break