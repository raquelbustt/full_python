try:
    arquivo = open('manipulacao_arquivos/pessoas.csv')

    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
# except IndexError:
#     pass
finally:
    print('Finaly!')
    arquivo.close()

if arquivo.close:
    print('Arquivo fechado')