def soma_3(a,b,c):
    return a + b + c

def soma_n(*numeros):
    print(type(numeros))
    soma = 0
    for n in numeros:
        soma += n
    return soma

if __name__ == "__main__":
    # packing
    print(soma_n(1,1,1,1,1,2))
    
    # unpacking
    nums = (1, 2, 3)
    print(soma_3(*nums))

    lista_nums = [1, 2, 5]
    print(soma_3(*lista_nums))