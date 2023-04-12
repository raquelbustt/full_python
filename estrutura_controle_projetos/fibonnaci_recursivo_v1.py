from numpy import quantile


def fibonacci(qtd, sequencia=(0,1)):
    # Condição de parada
    if len(sequencia) == qtd:
        return sequencia
    return fibonacci(qtd, sequencia + (sum(sequencia[-2:]),))

for fib in fibonacci(5, (2, 3)):
    print(fib)