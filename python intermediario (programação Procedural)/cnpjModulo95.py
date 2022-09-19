#Esse arquivo faz parte da aula 95DesafioValideUmCnpj

import re

def remover_caracteres(stringCnpj):

    stringCnpj = re.sub(r'[^0-9]','',stringCnpj) #Expressao regular que remove os caracteres do cnpj. Dentro de [], estou
    #dizendo que tudo que for diferente entre 0 e 9, vc troca por vazio no segundo parametro ''

    lista = list(map(int, stringCnpj))

    return lista

    #Daria para remover os caracteres usando o replace, mas daria mais trabalho, conforme exemplo abaixo
    #cnpj = cnpj.replace('/','')
    #cnpj = cnpj.replace('.','')
    #cnpj = cnpj.replace('-','')
    #return cnpj



def verifica (ListaNumeros):

    lista = multiplicadores(ListaNumeros)
    calc = calculo(ListaNumeros, lista)
    resultado = 11 - (calc % 11)

    return resultado




def multiplicadores (ListaNumeros): #Essa função vai gerar a lista [5   4   3   2   9   8   7   6   5   4   3   2]

    lista = []
    x = False

    if len(ListaNumeros) == 12:
        contador = 5
    else:
        contador = 6

    for i in ListaNumeros:
        if contador < 2 and x == False:
            contador = 9
            x = True
        lista.append(contador)
        contador = contador - 1
    #print(f'lista: {lista}')
    return lista





def calculo(ListaNumeros, lista):

    # print(f'listaNumeros: {ListaNumeros}')
    # print(f'lista:        {lista}')
    mult = []

    for i, j in zip(ListaNumeros, lista):
        mult.append(i*j)

    soma = 0
    for i in mult:
        soma = soma + i
    return soma;




