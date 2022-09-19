

#Nós criamos uma pasta vendas89 que possui um arquivo calculaPreco que faz calculos de soma de porcentagem em valores passados
#Como parametro

#primeiro exemplo

import vendas89.calculaPreco #fazendo import do arquivo caculaPreco que está dentro da pasta vendas89

preco = 49.90
precoComAumento = vendas89.calculaPreco.aumento(preco, 15) #Desta forma, tenho que chamar a pasta (vendas89),
# seguido do arquivo (calculaPreco) e da função (aumento).
print(precoComAumento)

print()
print('-----------------------')
print()

#segundo exemplo

from vendas89 import calculaPreco #Fazendo import do arquivo calculaPreco que está dentro de vendas89

preco = 50
precoComAumento = calculaPreco.aumento(preco, 25) #Com o import sendo feito conforme segundo exemplo, não precisa digitar o nome da basta 'vendas89'
#igual feito no primeiro exemplo acima
print(precoComAumento)


print()
print('-----------------------')
print()

#Terceiro exemplo

from vendas89.calculaPreco import aumento, reducao #Dessa forma eu estou importando informando a basta e o arquivo 'vendas89.calculaPreco' e sem seguida
#o nome das funções 'aumento e reducao'

preco = 50
precoComAumento = aumento(preco, 25) #Com o import sendo feito conforme terceiro exemplo, não precisa digitar o nome da basta 'vendas89'
# e nem o nome do arquivo 'calculaPreco' igual feito no segundo exemplo acima. Posso digitar diretamente o nome da função
print(precoComAumento)



print()
print('-----------------------')
print()


#quarto exemplo

#Neste exemplo, nós criamos uma pasta chamada 'formata' dentro da pasta 'vendas89' que têm um arquivo chamado preco. Nesse arquivo
#temos uma função que forma os valores dos preços

from vendas89.calculaPreco import aumento, reducao #Dessa forma eu estou importando informando a basta e o arquivo 'vendas89.calculaPreco' e sem seguida
#o nome das funções 'aumento e reducao'

from vendas89.formata import preco #estou importando o arquivo preco da pasta pasta formata que fica dentro da pasta vendas89

from vendas89.calculaPreco import aumento, reducao #Dessa forma eu estou importando informando a basta e o arquivo 'vendas89.calculaPreco' e sem seguida
#o nome das funções 'aumento e reducao'

preco = 50
precoComAumento = aumento(preco, 25, formata=True) #Com o import sendo feito conforme terceiro exemplo, não precisa digitar o nome da basta 'vendas89'
# e nem o nome do arquivo 'calculaPreco' igual feito no segundo exemplo acima. Posso digitar diretamente o nome da função.
print(precoComAumento)