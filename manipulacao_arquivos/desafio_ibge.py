import codecs
import csv
from email.encoders import encode_noop

def read_files(filename):
    with open(filename, encoding='latin1') as arquivo:
        for registro in csv.reader(arquivo):
            print(f'{registro[8]}: {registro[3]}')
    # with codecs.open(filename, 'r', encoding='latin1') as arquivo:
    #     for cidade in csv.reader(arquivo):
    #         print(f'{cidade[8]}: {cidade[3]}')

read_files('manipulacao_arquivos/desafio-ibge.csv')