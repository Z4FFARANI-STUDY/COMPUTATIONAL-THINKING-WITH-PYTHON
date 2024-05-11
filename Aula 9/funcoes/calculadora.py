continuar = "S"

while continuar == "S":
    operacao = input("Escolha a operação (+) (-) (/) (*): ")
    n1 = int(input("Número 1: "))
    n2 = int(input("Número 2: "))

    def somar(n1, n2):
        return n1 + n2

    def subtrair(n1, n2):
        return n1 - n2

    def dividir(n1, n2):
        return n1 / n2

    def multiplicar(n1, n2):
        return n1 * n2

    if operacao == "+":
        print("Soma: ")
        print(somar(n1, n2))

    elif operacao == "-":
        print("Subtração: ")
        print(subtrair(n1, n2))

    elif operacao == "/":
        print("Divisão: ")
        print(dividir(n1, n2))

    elif operacao == "*":
        print("Multiplicar: ")
        print(multiplicar(n1, n2))
    
    else:
        print("Operação inválida, tente novamente.")

    continuar = input("Continuar? SIM <S>, NÃO <N>: ").upper()


