def todos_params(*args, **kwargs):
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')

todos_params('a', 'b', 'c')
todos_params('Raquel', 'Felipe', [1,2,3], tamanho='M', fragil=False)
# Se vc passar parametro nomeado antes de um parametro nomeado e não nomea-lo
# isso dará erro, ex:
# todos_params(nome='Raquel', [1,2,3])
todos_params(primeiro='Joao', segundo='Maria')