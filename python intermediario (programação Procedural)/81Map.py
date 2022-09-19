from dadosAula81Map import produtos, pessoas, lista #estou importando as listas do arquivo dadosAula81Map

print(lista) #Dando um print na lista 'lista' do arquivo 'dadosAula81Map'
#lista = [1,2,3,4,5,6,7,8,9,10]

print()
print('----------------------------------------------')
print()

novaLista = map(lambda x: x*2, lista) #usando map para salvar na variavel novaLista uma lista com os valores de lista multiplicados por 2
#print(novaLista) #Vai imprimi <map object at 0x01E52FD0>. Retorna um iterador
print(list(novaLista)) #Vai imprimir [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


nova_lista = [x*2 for x in lista] #fazendo a mesma coisa acima só que com 'list comprehension'
print(list(nova_lista)) #Vai imprimir [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

print()
print('----------------------------------------------')
print()


for produto in produtos: #Dando um print na lista 'produto' do arquivo 'dadosAula81Map'
    print(produto)

#Vai imprimir
# {'nome': 'p1', 'preco': 50}
# {'nome': 'p1', 'preco': 55.55}
# {'nome': 'p1', 'preco': 35}
# {'nome': 'p1', 'preco': 5.1}
# {'nome': 'p1', 'preco': 4.99}
# {'nome': 'p1', 'preco': 2}
# {'nome': 'p1', 'preco': 122.5}
# {'nome': 'p1', 'preco': 27}
# {'nome': 'p1', 'preco': 99.99}
# {'nome': 'p1', 'preco': 10}

print()
print('----------------------------------------------')
print()

precos = map(lambda p: p['preco'], produtos) #Estou criando um dicionario com apenas os preços da minha lista 'produtos
for preco in precos: #for para imprimir os valores de precos
    print(preco)
#Vai imprimir
# 50
# 55.55
# 35
# 5.1
# 4.99
# 2
# 122.5
# 27
# 99.99
# 10

print()
print('----------------------------------------------')
print()


def aumenta_preco(p): #Digamos que eu queira soma 5% nos valores dos preços sem alterar minha lista. Seria necessario criar uma função
    p['preco'] = round(p['preco'] * 1.05, 2) #Multiplicar por 1.05 é o mesmo que somar 5%. Lembrando que o round serve para arredondar com duas casas decimais.
    return p

precos = map(aumenta_preco, produtos) #Estou criando um dicionario com apenas os preços da minha lista 'produtos
for preco in precos: #for para imprimir os valores de precos
    print(preco)

print()
print('----------------------------------------------')
print()

# pessoas = [
#
#     {'nome':'Davidson', 'idade':31},
#     {'nome':'Maria', 'idade':25},
#     {'nome':'Debora', 'idade':30},
#     {'nome':'Tais', 'idade':34},
#     {'nome':'José', 'idade':85},
#     {'nome':'Mario', 'idade':25},
#     {'nome':'Goku', 'idade':32},
#     {'nome':'Vegeta', 'idade':35},
#     {'nome':'Picolo', 'idade':35},
#     {'nome':'Kuririn', 'idade':31},
#
# ]
def aumenta_idade(p): #Essa função vai adicionar uma nova idade e, essa nova idade terá o valor de 20% a mais em relação a idade original
    p['nova_idade'] =  p['idade'] * 1.20
    return p

nomes = map(aumenta_idade, pessoas)

for pessoa in nomes:
    print(pessoa)

#Vai imprimir
# {'nome': 'Davidson', 'idade': 31, 'nova_idade': 37.199999999999996}
# {'nome': 'Maria', 'idade': 25, 'nova_idade': 30.0}
# {'nome': 'Debora', 'idade': 30, 'nova_idade': 36.0}
# {'nome': 'Tais', 'idade': 34, 'nova_idade': 40.8}
# {'nome': 'José', 'idade': 85, 'nova_idade': 102.0}
# {'nome': 'Mario', 'idade': 25, 'nova_idade': 30.0}
# {'nome': 'Goku', 'idade': 32, 'nova_idade': 38.4}
# {'nome': 'Vegeta', 'idade': 35, 'nova_idade': 42.0}
# {'nome': 'Picolo', 'idade': 35, 'nova_idade': 42.0}
# {'nome': 'Kuririn', 'idade': 31, 'nova_idade': 37.199999999999996}