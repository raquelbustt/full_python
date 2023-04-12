def calcula_preco_final(preco_bruto, calc_imposto, *params):
    return preco_bruto + preco_bruto * calc_imposto(*params)

def imposto_x(importado):
    return 0.22 if importado else 0.13

def imposto_y(explosivo, fator_mult=1):
    return 0.11 * fator_mult if explosivo else 0

if __name__ == '__main__':
    preco_bruto = 334.98
    preco_final = calcula_preco_final(preco_bruto, imposto_x, True)
    preco_final = calcula_preco_final(preco_final, import_y, True, 2)

    print(f'{preco_final:.2f}')