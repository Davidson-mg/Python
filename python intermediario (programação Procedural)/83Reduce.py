from dadosAula81Map import produtos, pessoas, lista #estou importando as listas do arquivo dadosAula81Map
from _functools import reduce #Para que possamos usar o reduce, somos obrigados a fazer este import


soma_lista = reduce(lambda acumulador, i: i + acumulador, lista, 0) #Vai ir somando numa unica variavel os valores da lista 'lista' começando do indice 0, do arquivo 'dadosAula81Map' feito import acima
print(soma_lista) #vai imprimir: 55

print()
print('----------------------------')
print()

soma_preco = reduce(lambda ac, p: p['preco'] + ac, produtos, 0) #Vai somar numa unica variavel os precos da minha lsta produtos começando do indice 0, do arquivo 'dadosAula81Map' feito import acima
print(soma_preco) #Vai imprimir: 412.13
print(soma_preco/len(produtos)) #obtendo a media. Vai imprimir: 41.213