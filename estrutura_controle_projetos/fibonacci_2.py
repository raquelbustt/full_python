# 0, 1, 2, 3, 5, 8 ...

def fibonacci(limite):
    penultimo = 0
    ultimo = 1

    print(f'{penultimo}, {ultimo}', end=',')

    while ultimo < limite:
        proximo = penultimo + ultimo

        print(f'{proximo}', end=',')

        penultimo = ultimo
        ultimo = proximo

fibonacci(22)