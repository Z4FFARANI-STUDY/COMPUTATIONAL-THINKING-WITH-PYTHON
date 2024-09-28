a = [1,2,3,4,5]
b = [3,4,5,6,7]

# Definindo lista como conjunto
a = set(a)
b = set(b)

# Valores comum às duas listas
c = a & b
print(list(c))

# Valores que só existem na primeira
c = a - b
print(list(c))

# Valores que existem apenas na segunda
c = b - a
print(list(c))

# Uma lista com os elementos não repetidos das duas listas
c = (a | b) - (a & b)
# ou c = a ^ b

print(list(c))