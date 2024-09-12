valor = 0

while True:
    escolha = input("Digite o código da fruta desejada (ou 0 para sair): ")
    if escolha != "0":
        kg = float(input("Qual o peso desejado? "))

    if escolha == "1":
        valor += 12.90 * kg
    elif escolha == "2":
        valor += 9.30 * kg
    elif escolha == "3":
        valor += 3.50 * kg
    elif escolha == "4":
        valor += 7.00 * kg
    elif escolha == "5":
        valor += 37.50 * kg
    elif escolha == "0":
        print("Sair do loop")
        break
    else:
        print("Código inválido")
    
print(f"O valor total da compra é R${valor:.2f}")
