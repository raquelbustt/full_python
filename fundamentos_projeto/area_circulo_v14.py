from math import pi
import sys
import errno

def circulo(raio):
    return pi * float(raio) ** 2

def func_help():
    print("É necessário informar o raio do ")
    print(f'Sintaxe: {sys.argv[0]} <raio>')

if __name__ == '__main__':

    if len(sys.argv) < 2:
        func_help()
        # finalizar o script que terminou com erro
        sys.exit(1)
    
    if not sys.argv[1].isnumeric():
        help()
        print("Necessário que o raio seja um valor numérico")
        sys.exit(errno.EINVAL)

    raio = sys.argv[1]
    # raio = float(input("Digite o raio:\n"))
    area = circulo(raio)
    print(f'A área do círculo é {area:.2f}')