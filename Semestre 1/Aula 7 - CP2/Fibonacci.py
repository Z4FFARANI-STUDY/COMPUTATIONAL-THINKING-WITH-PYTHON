n = int(input("Digite quantos termos de Fibonacci você deseja somar: "))

if n == 0 or n == 1:
    print(0)
else:
    a1 = 0
    a2 = 1
    i = 1
    soma = a1 + a2

    while i <= n - 2:
        fibo = a1 + a2
        a1 = a2
        a2 = fibo
        soma += fibo
        i += 1
        
    print(soma)