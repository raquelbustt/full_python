from app.utils.gerador import novo_nome
from app.negocio import nome_existe
from app.negocio.backend import add_nome

def name():
    while True:
        nome = novo_nome()
        print(nome)
        if not nome_existe(nome):
            add_nome(nome)
            break
    
    print(f'Criado novo nome: {nome}')

def teste():
    return "Oi!"
    
if __name__ == '__main__':
    name()