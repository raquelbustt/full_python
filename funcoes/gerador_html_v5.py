from webbrowser import get

bloco_arts = ('bloco_acesskey', 'bloco_id')
ul_atrs = ('ul_id', 'ul_style')

def get_atrs(informados, suportados):
    return ' '.join(f'{k.split("_")[-1]} = "{v}"'
                    for k, v in informados.items() if k in suportados)

def tag_bloco(conteudo, *args, classe='success', inline=False, **novos_atrs):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable (conteudo) else conteudo(*args, **novos_atrs)
    atributos = get_atrs(novos_atrs, bloco_arts)
    return f'<{tag} {atributos} class="{classe}">{conteudo}</{tag}>'

def tag_lista(*itens, **novos_atrs):
    lista = ''.join((f'<li>{item}</li>' for item in itens))
    return f'<ul {get_atrs(novos_atrs, ul_atrs)}>{lista}</ul>'

if __name__ == '__main__':
    # print(tag_bloco('bloco'))
    # print(tag_bloco('inline', inline=True))
    # print(tag_bloco(tag_lista('Raquel', 'Felipe', 'Ana'), classe = "info"))
    # print(tag_bloco(tag_lista, 'Sábado', 'Domingo', classe='info', inline=True))
    # print(tag_bloco(tag_lista, 'Sábado', 'Domingo', classe='info_1', inline=False))
    print(tag_bloco(tag_lista, 'Item 1', 'Item 2', classe='info',
                    bloco_acesskey='m', bloco_id='conteudo', ul_id='lista'))
