# Função com return embutido
dobro = lambda x: x*2
dobro_dobro = lambda x: dobro(x)*2
print(dobro_dobro(2))

a = [5, 5]
result = list(filter(lambda x: x * 2, a))
print(result)
