from vendas89.formata import preco #estou importando o arquivo preco da pasta pasta formata que fica dentro da pasta vendas89

def aumento(valor, porcentagem, formata=False): #Esse terceiro parametro colocamos como false pq se eu não enviar este parametro
    #não quero que formate o preco, seu eu enviar, deve formatar
    r = valor + (valor * (porcentagem/100))
    if formata:
        return preco.real(r)
    else:
        return r


def reducao(valor, porcentagem, formata=False):
    r = valor - (valor * (porcentagem/100))
    if formata:
        return preco.real(r)
    else:
        return r