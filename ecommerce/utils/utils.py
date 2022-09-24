#Este arquivo contem algumas funções que podem ser utilizadas em mais de um lugar.

def formata_preco(val): #Essa função está sendo chamada por exemplo em produto/templatestags/dafilters.py
    return f'R$ {val:.2f}'.replace('.', ',')



def cart_total_qtd(carrinho): #Esta sendo chamada em produto/templatestags/dafilters.py. Estamos recebendo o
    # carrinho completo, com todos o seus atributos

    return sum([ #somando a quantidade de todos os produtos, incluindo os que são da mesma variação e têm mais de uma
    #unidade
            item['quantidade'] for item in carrinho.values() #o item pega a quantidade percorrendo cada item do arrinho.
        #lembrando que o carrinho é um dicionario, por isso usamos a chave 'quantidade'
    ])


def cart_totals(carrinho): #Essa função vai somar os valores de todos o itens no carrinho, considerando os valores
    #normais, em promoção e etc. Essa função vai ser chamada em produto/templatestags/dafilters.py
    return sum (
        [
            item.get('preco_quantitativo_promocional') #obtem o item preco_quantitativo_promocional
            if item.get('preco_quantitivo_promocional') #se o preco_quantitivo_promocional estiver preenchido
            else item.get('preco_quantitativo') #o contrario disso, obtem o preco_quantitativo
            for item #para cada item
            in carrinho.values() #no carrinho
        ]
    )