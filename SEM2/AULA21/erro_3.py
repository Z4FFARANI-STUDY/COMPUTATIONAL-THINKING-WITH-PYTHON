while True:
    try:
        a = int(input('Insira um valor: '))
    except Exception as error:
        print('Dado inválido.')
    else:
        print('Comando executou com sucesso.')
        break
    finally:
        print('Será executado sempre.')

    print('Continuação do programa.')