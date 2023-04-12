from markupsafe import re


def faixa(idade):
    if 0 <= idade < 18:
        return 'Menor de idade'
    elif idade in range(18, 65):
        return 'Adulto'
    elif idade in range(65, 100):
        return 'Idoso'
    elif idade >= 100:
        return 'Centenário'
    else:
        return 'Idade inválida'

if __name__ == '__main__':
    idades = (15, 85, 96, 56)
    
    for idade in idades:
        print(f'{idade}:{faixa(idade)}')