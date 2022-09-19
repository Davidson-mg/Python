"""Split, joi, Enumerate em Python
*split - Dividir uma string # str
*Join - Juntar uma lista # str
*Enumerate - Enumerar elementos da lista # list / iteraveis
"""

string = "O Brasil é um país lindo, muito belo"
lista = string.split(' ') #Vai armazenar na variavel lista os elementos da string separados por espaço ' '
print(lista) #Vai imprimir ['O', 'Brasil', 'é', 'um', 'país', 'lindo,', 'muito', 'belo']

string = "O Brasil é um país lindo, muito belo"
lista = string.split(',') #Vai armazenar na variavel lista os elementos da string separados por virgula
print(lista) #Vai imprimir ['O Brasil é um país lindo', ' muito belo']


print()
print('-----------------------------------')
print()



frase = "Jesus é o Rei dos Reis"
lista_frase = frase.split(' ')
lista_palavras = []

for palavra in lista_frase:

    if palavra in lista_palavras: #se tiver uma palavra igual a palavra atual dentro da lista 'lista_palavras', é pq já fez a contagem dessa palavra, então, da um continue para volta o loop para o inicio
        continue

    lista_palavras.append(palavra)

    print(f'A palavra {palavra} apareceu na lista {lista_frase.count(palavra)} vezes na frase')




print()
print('-----------------------------------')
print()

string2 = 'Jesus é o supremo Rei, Jesus é Santo e é poderoso'
lista2 = string2.split(' ') #Vai armazenar na variavel lista os elementos da string separados por espaço ' '

palavra = ''
ultima_repete_mais = 0

for valor in lista2:

    atual_repeticoes = lista2.count(valor) #vai contar quantas vezes a palavra atual (valor) se repete e armazenar na variavel atual_repeticoes

    if atual_repeticoes > ultima_repete_mais: #se o valor da variavel "atual_repeticoes" for maior que o valor da variavel "ultima_repete_mais"
        ultima_repete_mais = atual_repeticoes #"ultima_repete_mais" recebe o valor da variavel "atual_repeticoes"
        palavra = valor

print(f'A palavra que aparece mais vezes é "{palavra}", {ultima_repete_mais} vezes')




print()
print('-----------------------------------')
print()




string3 = 'O Brasil, é o país de Jesus!'
lista3 = string3.split(',')
for valor in lista3:
    print(valor.strip().capitalize()) #a função "strip" vai remover os espaços e a função "capitalize" vai colocar letra maiuscula no inicio de cada frase.
#sem as funções strip e capitalize, seria impresso assim:
#O brasil
# é o país de Jesus!


print()
print('-----------------------------------')
print()


string = 'O Brasil é penta'
lista = string.split(' ') #vai gerar uma lista com as palavras da string acima separando por espaço
string2 = ','.join(lista) #vai gerar uma string com as palavras da lista acima, colocando uma virgula entre cada palavra

print(string)
print(lista)
print(string2)

#Vai imprimir assim
# O Brasil é penta
# ['O', 'Brasil', 'é', 'penta']
# O, Brasil, é, penta


print()
print('-----------------------------------')
print()




lista = [ ['0','Luiz'], ['1', 'João'], ['2', 'Maria'] ] #Para termos o resultado do enumerate sem usar o enumerate, teriamos que fazer dessa forma, criando lista dentro de lista

for indice, nome in lista:
    print(indice, nome);

# vai imprimir assim
# 0 Luiz
# 1 João
# 2 Maria



print()

lista = ['Luiz', 'João', 'Maria'] #Com a função enumerate, eu tenho exatamente o mesmo resultado do exemplo acima criando uma lista normal, sem precisar criar lista dentro de lista
for indice, nome in enumerate(lista): #O enumerate serve apenas para enumerar uma lista
    print(indice, nome)

# vai imprimir assim
# 1 Luiz
# 2 João
# 3 Maria

print()

for indice, nome in enumerate(lista, 10): #O enumerate serve apenas para enumerar uma lista. O numero 10 dentro de parenteses serve para dizer qual será o numero inicial da enumeração
    print(indice, nome)

# vai imprimir assim
# 10 Luiz
# 11 João
# 12 Maria




print()
print('-----------------------------------')
print()


# string = 'O Brasil é penta'
# lista = string.split(' ')
# for indice, valor in enumerate(lista):









