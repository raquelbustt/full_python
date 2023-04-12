from numpy import quantile


def fibonacci(qtd, sequencia=(0,1)):
    # Condição de parada
    
    return sequencia if len(sequencia) == qtd \
        else fibonacci(qtd, sequencia + (sum(sequencia[-2:]),))

for fib in fibonacci(5, (2, 3)):
    print(fib)