"""

Zip - Unindo Iteraveis
Zip_longest - Itertools

"""
print()
print('-----------------------------------------Zip--------------------------------------')
print()

#                                                             Zip - Unindo Iteraveis




### Codigo
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Rio de Janeiro']

# codigo
estados = ['sp', 'mg', 'ba']

cidades_estados = zip(cidades, estados) #O zip vai unir as listas cidades e estados. Será uma lista com tuplas dentro. Cada tupla terá seu estado,cidade.
#Repare que temos quartro cidades e 3 estados. Ele vai unir considerando apenas até o menor valor na sequencia
#O zip vai gerar um gerador, possibilitando a gente usar o next, conforme feito abaixo, para ir chamando elemento por elementa.
# Sobre isso, reveja a aula do arquivo 71GeradoresIteradoresEIteraveisEmPython



# Só usei o next abaixo como exemplo do que poderiamos fazer, por está comentado
# print(next(cidades_estados))
# print(next(cidades_estados))
# print(next(cidades_estados)) #o next é um metodo iterador e mostra um elemento de cada vez em sequencia a medida que lhe utilizamos.
# # Vai imprimir na sequencia

# for valor in cidades_estados: #se eu não comento esse for, o for abaixo não imprimiria nada pois o gerador seria utilizado neste for
#     print(valor[0], valor[1])



for valor in cidades_estados:
    print(valor)
# Vai imprimir dessa forma
# ('São Paulo', 'sp')
# ('Belo Horizonte', 'mg')
# ('Salvador', 'ba')

print()
print('-----------------------------------------------------------')
print()


### Codigo
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Rio de Janeiro']

# codigo
estados = ['sp', 'mg', 'ba']

cidades_estados = zip(cidades, estados) #O zip vai unir as listas cidades e estados. Será uma lista com tuplas dentro. Cada tupla terá seu estado,cidade.
#Repare que temos quartro cidades e 3 estados. Ele vai unir considerando apenas até o menor valor na sequencia
#O zip vai gerar um gerador, possibilitando a gente usar o next, conforme feito abaixo, para ir chamando elemento por elementa.
# Sobre isso, reveja a aula do arquivo 71GeradoresIteradoresEIteraveisEmPython
#Se eu quiser que estado seja a chave e cidades sejam os elementos, basta eu inverter a ordem dos dois no parentese do zip

print(cidades_estados) #Como o zip gera um gerador, vai imprimir assim <zip object at 0x021677A8>. Para corrigir isso,

#basta converter em lista conform print abaixo
print(list(cidades_estados))# Vai imprimir: [('São Paulo', 'sp'), ('Belo Horizonte', 'mg'), ('Salvador', 'ba')]

#print(dict(cidades_estados))#Transformado cidades_estados que até aqui é um alista com tuplas dentro, em um dicionario com chaves e elementos. Mas nesse caso vai ser uma dicionario
#vazio, pois o gerador já foi utilizado acima. É só pra falar que é possivel mesmo

print()
print('-----------------------------------------------------------')
print()


from itertools import count # PARA USAR O count VOCÊ É OBRIGADO A FAZER ESTE IMPORT.

indice = count() #Vai contando infinitamente

cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Rio de Janeiro']

estados = ['sp', 'mg', 'ba']

cidades_estados = zip(indice, estados, cidades) #O zip vai unir as listas cidades e estados. Será uma lista com tuplas dentro. Cada tupla terá seu estado,cidade.
#Repare que temos quartro cidades e 3 estados. Ele vai unir considerando apenas até o menor valor na sequencia
#O zip vai gerar um gerador, possibilitando a gente usar o next, conforme feito abaixo, para ir chamando elemento por elementa.
# Sobre isso, reveja a aula do arquivo 71GeradoresIteradoresEIteraveisEmPython


print(cidades_estados) #Como o zip gera um gerador, vai imprimir assim <zip object at 0x021677A8>. Para corrigir isso,
#basta converter em lista conform print abaixo
print(list(cidades_estados))# Vai imprimir: [('sp', 'São Paulo'), ('mg', 'Belo Horizonte'), ('ba', 'Salvador'), (None, 'Rio de Janeiro')]



print()
print('-----------------------------------------Zip_longest-------------------------------------')
print()


#                                                            Zip_longest - Itertools

from itertools import zip_longest # PARA USAR O Zip_longest VOCÊ É OBRIGADO A FAZER ESTE IMPORT

### Codigo
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Rio de Janeiro']

# codigo
estados = ['sp', 'mg', 'ba']

cidades_estados = zip_longest(estados, cidades) #O zip_longest vai unir as listas cidades e estados. Será uma lista com tuplas dentro. Cada tupla terá seu estado,cidade.
#Repare que temos quartro cidades e 3 estados. Diferente de zip que uni considerando apenas até o menor valor na sequencia, zip_longest vai unir todas coloca 'None' onde não possui valor equivalente.
#Eu consigo trocar a palavra None acrescentando entre parentese a palavra 'fillvalue=novoNome'. Ficaria assim:  cidades_estados = zip_longest(estados, cidades)
#O zip vai gerar um gerador, possibilitando a gente usar o next, conforme feito abaixo, para ir chamando elemento por elementa.
# Sobre isso, reveja a aula do arquivo 71GeradoresIteradoresEIteraveisEmPython


print(cidades_estados) #Como o zip gera um gerador, vai imprimir assim <zip object at 0x021677A8>. Para corrigir isso,
#basta converter em lista conform print abaixo
print(list(cidades_estados))# Vai imprimir: [('sp', 'São Paulo'), ('mg', 'Belo Horizonte'), ('ba', 'Salvador'), (None, 'Rio de Janeiro')]



