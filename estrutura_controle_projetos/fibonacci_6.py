# 0, 1, 2, 3, 5, 8 ...

from unittest import result


def fibonacci(limite):
    resultado = [0,1]

    while True:
        resultado.append(sum(resultado[-2:]))
        if len(resultado) == limite:
            break
    
    return resultado

if __name__ == "__main__":

    # Condição de parada é o tamanho do array inputado
    # Definindo a qtde de sequencia que quero:

    for fib in fibonacci(5):
        print(fib)