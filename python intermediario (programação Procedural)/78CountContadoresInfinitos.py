"""
count - tertools
"""

from itertools import count

contador = count() #A função count retorna um itereador. Ela gera um contador que é um iterador
#possibilitando usarmos a função next, conforme mostrado por exemplo na aula 71

print(next(contador)) #o next é um metodo iterador e mostra um elemento de cada vez em sequencia a medida que lhe utilizamos, como se fosse um for. Vai imprimir na sequencia
print(next(contador))
print(next(contador))
# ... Como o count gerar numeros infinitos e gerar um iterador, podemos usar o next infinitamente

#OBS IMPORTANTE
# for valor in contador: #Cuidado ao utilizar o count pois ele pois como ele gera infinitamente, gerar tb um loop infinito como neste caso.
# #Por isso coloquei comentado
#     print(valor)

print()
print('--------------------------------')
print()

contador = count(start=5, step=2) #A função count retorna um itereador. Ela gera um contador que é um iterador possibilitando usarmos a função next, conforme mostrado
# por exemplo na aula 71. Com a palavra start=5 estou dizendo que vai começar a contar a partir de 5. A palavra step=5 diz de quanto em quanto deve contar. O step aceita numeros
# do tipo flout também.

for valor in contador: #Cuidado ao utilizar o count pois ele pois como ele gera infinitamente, gerar tb um loop infinito.
#Neste caso não será infinito pois colocamos um break
    print(valor)
    if valor >= 10:
        break

print()
print('--------------------------------')
print()

contador = count(start=5, step=0.1) #A função count retorna um itereador. Ela gera um contador que é um iterador possibilitando usarmos a função next, conforme mostrado
# por exemplo na aula 71. Com a palavra start=5 estou dizendo que vai começar a contar a partir de 5. A palavra step=5 diz de quanto em quanto deve contar. O step aceita numeros
# do tipo flout também.

for valor in contador: #Cuidado ao utilizar o count pois ele pois como ele gera infinitamente, gerar tb um loop infinito.
#Neste caso não será infinito pois colocamos um break
    print(valor, round(2))
    if valor >= 7:
        break


print()
print('--------------------------------')
print()

contador = count(start=5, step=-1) #A função count retorna um itereador. Ela gera um contador que é um iterador possibilitando usarmos a função next, conforme mostrado
# por exemplo na aula 71. Com a palavra start=5 estou dizendo que vai começar a contar a partir de 5. A palavra step=-1 diz que vai contar de trás pra frente e de quanto em quanto.
# O step aceita numeros do tipo flout também.

for valor in contador: #Cuidado ao utilizar o count pois ele pois como ele gera infinitamente, gerar tb um loop infinito.
#Neste caso não será infinito pois colocamos um break
    print(valor)
    if valor == 0:
        break


print()
print('--------------------------------')
print()

contador = count()
lista = ['Davidson', 'Maria', 'Neide'] #Lista com alguns nomes
lista = zip(contador, lista) #O zip vai unir a lista 'lista' com a variave contador. A função count retorna um itereador. Ela gera um contador que é um iterador.
# Será uma lista com tuplas dentro. Cada tupla terá seu 'numero do contador',nome da lista. Foi falado sobre zip na aula 75
print(list(lista)) #Vai imprimir: [(0, 'Davidson'), (1, 'Maria'), (2, 'Neide')]