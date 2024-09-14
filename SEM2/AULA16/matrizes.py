a = [[1,2,3], [4,5,6], [7,8,9]]
# para copiar e manter os elementos de a igual a b, [:] ou .copy(). Para não manter os elementos iguais, um loop que percorre a matriz de a é necessário:
b = [i.copy() for i in a]
print(a)
print(b)

print()

b[0][0] = 3
print(a)
print(b)
