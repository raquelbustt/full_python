palavra = 'paralelepipedo'

for letra in palavra:
    print(letra, end='\n')

aprovados = ['Raquel', 'Felipe']

for nome in aprovados:
    print(nome)

for posicao, nome in enumerate(aprovados):
    print(f'{posicao + 1} - {nome}')