import oper1, oper2

o = input("Digite +, -, *, / para a operação desejada: ")
val = []

while True:
    num = input("Digite o valor ou s para finalizar a operação: ")
    if num != "s":
        val.append(float(num))
    else:
        break

if o == "+":
    resultado = oper1.soma(*val)
elif o == "-":
    resultado = oper1.sub(*val)
elif o == "*":
    resultado = oper2.mult(*val)
elif o == "/":
    resultado = oper2.div(*val)
else:
    print("Operação inválida.")

print(f"O resultado da {o} é: {resultado}")