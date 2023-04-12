from http.client import PROXY_AUTHENTICATION_REQUIRED
from subprocess import call


class Potencia:
    def __init__(self, expoente):
        self.expoente = expoente

    def __call__(self, base):
        return base ** self.expoente

if __name__ == '__main__':
    quadrado = Potencia(2)
    cubo =  Potencia(3)

    print(f'3^2 => {quadrado(3)}')

    if callable(quadrado) and callable(cubo):
        print(f'3^2 => {quadrado(3)}')
        print(f'4^2 => {Potencia(4)(2)}')

    # print(quadrado)