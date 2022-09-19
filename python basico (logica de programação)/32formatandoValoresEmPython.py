"""

formatando valores com modificadores - aula 5

:s - texto (string)
:d - interiros (int)
:f - numeros de ponto flutuante (float)
:. (numero) f - quantidade de casas decimais (float)
: (caractere) (> ou < ou ^) (quantidade) (tipo - s, d ou f)

> - esquerda
< - direita
^ - centro

"""

num1 = 10
num2 = 3
divisao = num1 / num2
print(divisao) ##Dessa forma vai imprimir com muitas casas decimais depois da virgula
print('{:.2f}'.format(divisao)) ##Dess forma vai imprimir com duas casas decimais depois da virgula
print(f'{divisao:.2f}') ##Outra forma de imprimir mostrando apenas duas casas decimais depois da virgula


##OBS: no exemplo acima, caso eu queira mais casas decimais depois da virgula, basta trocar o 2 por outro numero correspondente

print()
print('-----------------------------------')
print()

n1 = 11
print(f'n1') ##Dessa forma vai imprimir o nome da variavel
print(f'{n1}') ##Dessa forma imprime o valor da variavel
print(f'{n1:0>10}')#Dessa forma, vai imprimir o numero com dez casas na frente, o numero real + qtd de zeros faltantes para chegar em dez casas na frente, ex: 0000000011#
print(f'{n1:0<10}')#Dessa forma terá o mesmo afeito de cima, porém, estou colocando os zeros do lado direito, ex 1100000000
print(f'{n1:0^10}')#Dessa forma terá o mesmo efeito dos exemplos acima, porém, colocando os zeros dos dois lados e o nº da variavel no centro, ex: 0000110000
print(f'{n1:.2f}')#Estou formatando o numero com duas casas decimais depois da virgula, como se fosse float, mas neste caso, o valor da variavel continua sendo int, é apenas um formatação, ex: 11.00
print(f'{n1:0>10.2f}')#Estou imprimindo o valor 11 da variavel n1 com 10 casas decimais, sendo que duas delas ficam depois da virgula, ex: 0000011.00

print()
print('-----------------------------------')
print()

nome = 'Davidson Marcos'
sobrenome = 'Gomes'
print(f'{nome:s}') ##Aqui não estou implementando nenhuma formatação, apenas evidenciando que o valor a ser impresso é uma string
print(50 - len(nome)) #Vai imprimir o valor que corresponde a subtração de 50 pelo numero que corresponde a qtd de caracteres do nome, ou seja, vai imprimir 35
print(f'{nome:#^50}')#Vai colocar a string da variavel nome no centro de de 50 caracteres, contando com os caracteres da propria string, ex: #################Davidson Marcos##################. OBS: eu usei o caracter '#', mas poderia usar qualquer outro
nome_formatado = '{:@>50}'.format(nome); #Outra forma de formatar com os comandos acima porém dentro da função format
print(nome_formatado)
nome_formatado = '{n:#<20}'.format(n=nome) #Outra forma de formatar, mas dessa forma estou dando o nome de 'n' pra variavel na formatação
print(nome_formatado)
nome_formatado = '{1:#<10}'.format(nome, sobrenome) #Dessa foma, considerando que vou formatar o mesmo print com duas variaveis, estou selecionando por indice. Neste exemplo, a variavel sobrenome está no indice 1 e estou acrescentando 10 caracteres a esquerda no conteudo da variavel no indice 0

#Obs: Nos exemplos acima, caso eu tenha string ou valor numerico na variavel com 10 caracteres e pedir pra preencher com 10, ele vai mostrar apenas o valor da varial pois a variavel já possui os 10 caracteres

print(nome.lower()); #Vai imprimir tudo minusculo
print(nome.upper()); #Vai imprimir tudo maiusculo
print(nome.title()); #Vai imprimir primeiras letras maiusculas