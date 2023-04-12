from random import randint

def sortear_dado():
    numero = randint(1, 6)
    return numero

for i in range (1,7):
    if i % 2 == 1:
        continue

    if sortear_dado() == i:
        print('Acertou!')
        print('O numero é:', i)
        break
else:
    print('Não acertou o número!')
    print('O numero é:', i)