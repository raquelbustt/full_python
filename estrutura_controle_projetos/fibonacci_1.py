# 0, 1, 2, 3, 5, 8 ...

def fibonacci():
    penultimo = 0
    ultimo = 1

    print(f'{penultimo}, {ultimo}', end=',')

    while True:
        proximo = penultimo + ultimo

        print(f'{proximo}', end=',')

        penultimo = ultimo
        ultimo = proximo

fibonacci()