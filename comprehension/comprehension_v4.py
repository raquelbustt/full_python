# dicionario = {i: i ** 2 for i in range(11)}
dicionario = {i: i ** 2 for i in range(11)}
print(dicionario)

for numero, dobro in dicionario.items():
    print(f'{numero} x 2 = {dobro}')