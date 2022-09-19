def funcao(arg, arg2): #Exepressao comum que recebe dois valores e retorna o resultado da multiplicação dos dois
    return  arg * arg2

var = funcao(2,2)
print(var)

print()


a = lambda x, y: x * y #Expressao lambida que possui exatamente o mesmo resultado da função acima
print(a(2,2))

print()
print("------------------------------------")
print()

lista = [

    ['p1', 13],
    ['p2', 3],
    ['p3', 7],
    ['p4', 50],
    ['p5', 51]

]

#Tentando ordernar a lista acima pelo valor numerico (posição 1)
lista.sort()# a função sort() teria o obj de ordernar minha lista pelo primeiro item (p1, p2...), porém, neste caso não vai funcionar pois queremos ordenar pelo segundo intem (posição 1), e por padrão sort() considera a primeira posição 0
print(lista)

def func(item): #Essa função vai retornar um item na posição 1, ou seja, os valores numericos
    return item[1]

#pegando o valor de 1 que é referente a segunda posição da lista afim de ordena-la de forma crescente
lista.sort(key=func)#Key é uma palavra reservada da função sort que possibilita eu definir uma posição. Será igual a 'func' que vai armazenar o valor de 1.
print(lista)

lista.sort(key=func, reverse=True) #Mesma coisa do exemplo acima, porém, com 'reverse=True' estou dizendo que deve ordenar de forma decrescente
print(lista)

#O problema dos dois exemplos de lista.sort acima, é que precisamos de uma função comum para retornar a posição da lista.
# No exemplo abaixo usaremos uma exmpressão lambda e não será necessario a função comum func
lista.sort(key = lambda item: item[1]) #Repare que com uma expressão lambda não precisei usar a função 'func' acima
print(lista)

lista.sort(key = lambda item: item[1], reverse=True)
print(lista)

#OBS IMPORTANTE: a função sort() altera de fato a lista original como pode ver ao imprimir a lista após os comandos.
#Caso queira apenas exibir de forma ordenada sem altera a lista, pode usar a função sorted() abaixo

print(sorted(lista, key=lambda i: i[1]))


print()
print("------------------------------------")
print()