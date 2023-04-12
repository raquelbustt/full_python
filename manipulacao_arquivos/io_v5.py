with open('manipulacao_arquivos/pessoas.csv') as arquivo:
    with open('manipulacao_arquivos/pessoas2.csv', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome: {}, Idade: {}'.format(*pessoa), file=saida)

if arquivo.closed:
    print('Arquivo fechado')

if saida.closed:
    print('Arquivo de escrita foi fechado')