from math import prod


produto = {'nome' : 'Caneta', 'preco' : 1.49, 'estoque' : 54}

for chave in produto:
    print(f'Chave: {chave}')

for valor in produto.values():
    print(f'Valor: {valor}')

for chave, valor in produto.items():
    print(chave, ':', valor)

print(chave, valor)