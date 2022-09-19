from dadosAula81Map import produtos, pessoas, lista #estou importando as listas do arquivo dadosAula81Map

novaLista = filter(lambda x: x > 5, lista)#A função filter vai retornar verdadeiro ou falso para a expressão lambda. Neste caso
#vai retornar verdadeiro para todos os elementos maiores que 5

# print(novaLista) #Vai imprimi <filter object at 0x021A2FE8>. Retorna um iterador. É necessario converter pra list
print(list(novaLista)) #Vai imprimir [6, 7, 8, 9, 10]

nova_lista = [x for x in lista if x > 5] #Como seria o exemplo acima feito com list comprehension
print(nova_lista) #Vai imprimir [6, 7, 8, 9, 10]

print()
print('--------------------------------')
print()


novaLista = filter(lambda p: p['preco'] > 50, produtos) #Gerando uma lista que contenha os produtos maiores que 50 reais da lista produtos
for produto in novaLista:
    print(produto)


print()
print('--------------------------------')
print()

#Refazendo o exemplo acima, porém, usando uma função no lugar de uma expressao lambda

def filtra(produto): #Essa função retorna verdadeiro se o preco do produto for maior que 50 reais
    if produto['preco'] > 50:
        produto['e_caro'] = True #adicionando uma novo elemento e_caro na lista caso seja cima de 50
    return True

nova_lista = filter (filtra, produtos)

for produto in nova_lista:
    print(produto)

#Vai imprimir assim:
# {'nome': 'p1', 'preco': 50}
# {'nome': 'p1', 'preco': 55.55, 'e_caro': True}
# {'nome': 'p1', 'preco': 35}
# {'nome': 'p1', 'preco': 5.1}
# {'nome': 'p1', 'preco': 4.99}
# {'nome': 'p1', 'preco': 2}
# {'nome': 'p1', 'preco': 122.5, 'e_caro': True}
# {'nome': 'p1', 'preco': 27}
# {'nome': 'p1', 'preco': 99.99, 'e_caro': True}
# {'nome': 'p1', 'preco': 10}

