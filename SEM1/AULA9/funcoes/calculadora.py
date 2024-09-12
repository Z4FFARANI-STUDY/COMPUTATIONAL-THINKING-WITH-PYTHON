continuar = "C"

while continuar == "C":
    n1 = int(input("Número 1: "))
    n2 = int(input("Número 2: "))
    pergunta = input("Escolha a operação (+) (-) (/) (*): ")
 
    def operacao(n1, n2):
        if pergunta == "+":
            return n1 + n2
        elif pergunta == "-":
            return n1 - n2
        elif pergunta == "/":
            return n1 / n2
        elif pergunta == "*":
            return n1 * n2
        else:
            print("Operação inválida, tente novamente.")
    
    if operacao(n1, n2) == None:
        continuar = str(input("Continuar <C>, Parar <P>: ")).upper()
    else:
        print(f"Resposta: {operacao(n1, n2)}")
        continuar = str(input("Continuar <C>, Parar <P>: ")).upper()    

    

        
    

    



