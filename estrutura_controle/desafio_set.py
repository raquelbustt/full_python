from cgitb import text


PALAVRAS_PROIBIDAS = {'futebol', 'religião', 'política'}

textos = ['João gosta de futebol e política',
        'A praia foi divertida'   
]

for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print('Texto possui palavras proibidas: ', intersecao)
    else:
        print('O texto não possui palavras proibidas. Segue o texto: ', texto)