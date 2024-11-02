try:
    10/0
# catch
except:
    print('Tenho uma exceção!')
else:
    print('Comando executou com sucesso.')
finally:
    print('Será executado sempre.')

print('Continuação do programa.')