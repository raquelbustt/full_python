with open('manipulacao_arquivos/pessoas.csv') as arquivo:
    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

if arquivo.close:
    print('Arquivo fechado')