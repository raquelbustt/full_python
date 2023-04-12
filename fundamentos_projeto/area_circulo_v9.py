from math import pi

def circulo(raio):
    return pi * float(raio) ** 2

if __name__ == '__main__':

    raio = float(input("Digite o raio:\n"))
    area = circulo(raio)
    print(f'A área do círculo é {area:.2f}')