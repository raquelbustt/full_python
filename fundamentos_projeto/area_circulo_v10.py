from math import pi
import sys

def circulo(raio):
    return pi * float(raio) ** 2

if __name__ == '__main__':
    #argv = lista de todos os argumentos que serão passados pro meu script 
    # print(sys.argv[1])
    raio = sys.argv[1]
    # raio = float(input("Digite o raio:\n"))
    area = circulo(raio)
    print(f'A área do círculo é {area:.2f}')