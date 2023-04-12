# 0, 1, 2, 3, 5, 8 ...

from unittest import result


def fibonacci(limite):
    resultado = [0,1]

    for i in range(2, limite):
        resultado.append(sum(resultado[-2:]))
        
    return resultado

if __name__ == "__main__":

    for fib in fibonacci(10):
        print(fib)