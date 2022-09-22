def faixa_idade (idade):
    if idade <= 12:
        return('Criança')
    elif idade <= 18:
        return('Adolescente')
    elif idade <= 50:
        return('Adulto')
    else:
        return ('Idoso')


print(faixa_idade(60))