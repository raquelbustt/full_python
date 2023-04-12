def fibonacci(sequencia=[0,1]):
    # Uso de muáveis como valor default (armadilha)
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia

inicio = fibonacci()
print(inicio, id(inicio))
print(fibonacci(inicio))
restart = fibonacci()
print(restart, id(restart))

# Os objetos possuem o mesmo id porque se tratam do mesmo objeto
# Isso porque não é ideal usar objetos mutáveis como parametro padrão de uma função
# já que no momento que começamos a mexer nesses parametros esse efeito vai ser 
# propagado para as demais funções