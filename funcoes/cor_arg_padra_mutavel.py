def fibonacci(sequencia=None):
    # Se tiver algum valor ele vai considera-lo, se não, vai ser 0 e 1
    sequencia = sequencia or [0,1]
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


inicio = fibonacci()
print(inicio, id(inicio))
print(fibonacci(inicio))
restart = fibonacci()
print(restart, id(restart))

# Agora indicando o valor None, a cada vez que a função for executada 
# a variável irá mudar pois uma nova lista será criada