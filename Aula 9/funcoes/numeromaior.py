n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))

def retornar(n1, n2):
    if n1 > n2:
        print("n1 é maior que n2")
        return n1
    else:
        print("n2 é maior que n1")
        return n2

y = retornar(n1, n2)
print(y)
    

