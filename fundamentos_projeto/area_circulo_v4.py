from math import pi

def circulo(raio):
    print(f'Area do círculo {pi * float(raio) ** 2:.2f}')

if __name__ == '__main__':

    raio = float(input("Digite o raio:\n"))
    circulo(raio)