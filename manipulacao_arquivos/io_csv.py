import csv

with open ('manipulacao_arquivos/pessoas.csv', 'r', encoding='latin1') as entrada:
    for pessoa in csv.reader(entrada):
        # Funciona melhor pois ele já sabe que isso é um csv, então ele olha os argumentos sem precisar quebrar os parametros
        # com split() ou strip()
        print('Nome {}, Idade: {}'.format(*pessoa))