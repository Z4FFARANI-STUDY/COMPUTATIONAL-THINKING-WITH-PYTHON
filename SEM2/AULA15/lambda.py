# Função com return embutido
dobro = lambda x: x*2
dobro_dobro = lambda x: dobro(x)*2
print(dobro_dobro(2))


a.filter(lambda x: x*2)