from cgitb import text
from http.client import FOUND


PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'política')

texto = ['João gosta de futebol e política',
        'A praia foi divertida'   
]

for texto in texto:
    found = False
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print(f'Texto a palavra proibida: {palavra}')
            found = True

            break
    
    if not found:
        print('Texto autorizado:', texto)