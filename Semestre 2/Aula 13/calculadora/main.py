import somaSubtracao
import multiplicacaoDivisao

def calculadora():
    operacao = str(input("Escolha a operação [+] [-] [*] [/]: "))

    n1 = float(input("Primeiro número: "))
    n2 = float(input("Segundo número: "))

    match operacao:
        case "+":
            return somaSubtracao.soma(n1, n2)
        case "-":
            return somaSubtracao.subtracao(n1, n2)
        case "*":
            return multiplicacaoDivisao.multiplicacao(n1, n2)
        case "/":
            return multiplicacaoDivisao.divisao(n1, n2)
        case other:
            print("Operação inválida.")
            print(operacao)

print(calculadora())