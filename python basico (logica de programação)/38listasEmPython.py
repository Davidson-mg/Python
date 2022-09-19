

#indices+ 0    1    2    3    4
lista = ['a', 'b', 'c', 'd', 'e'];
#indices- 5    4    3    2    1      lembrando que de trás pra frente os indicies devem ser negativs

print()
print('------------------------------------------------')
print()

lista = ['a', 'bacana', 'c', 'd', 'e', 10.5, 150];

print(lista[-1]) #Vai imprimir 150

lista[5] = 'alterando o 150'

print(lista[5])


print()
print('------------------------------------------------')
print()

lista = ['a', 'b', 'c', 'd', 'e', 10.5, 150];

print (lista[0:3]) #Vai imprimir ['a', 'b', 'c']
print (lista[:3]) # Também vai imprimir ['a', 'b', 'c']
print (lista[2:]) # Vai imprimir tudo a partir do indice 2 ['c', 'd', 'e', 10.5, 150]
print (lista[::2]) #vai imprimir do inicio ao fim pulando de dois em dois ['a', 'c', 'e', 150]
print (lista[::-1]) #Vai imprimir de forma invertida do final ao inicio pulando de dois em dois [150, 10.5, 'e', 'd', 'c', 'b', 'a']



print()
print('------------------------------------------------')
print()

l1 = [1,2,3]
l2 = ['a','b','c']
l3 = l1 + l2 #vai formar uma nova lista com a junção de l1 e l2 [1, 2, 3, 'a', 'b', 'c']
print(l3)

l1.extend(l2) #vai juntar a lista l1 com a lista l2
print(l1) #vai imprimir [1, 2, 3, 'a', 'b', 'c']

l1 = [1,2,3]
l1.extend('x') #Acrescentando evalor 'x' a lista l1. Porém, neste caso só funciona com um valor. Se eu tivesse feito por exemplo l1.extend('x', 'y'), nada aconteceria
print(l1) #vai imprimir [1, 2, 3,'x']

l1 = [1,2,3]
l1.append('y') #terá o mesmo efeito do extend acima e também só funciona acrescendo um valor de cada vez
print(l1) #vai imprimir [1, 2, 3,'y']

l1 = [1,2,3]
l1.insert(0, 'banana'); #vai acrescentar a string 'banana' no primeiro indice
print(l1) #vai imprimir ['banana', 1, 2, 3]


l1 = [1,2,3, 'banana']
l1.pop() #vai remover o ultimo elemento da lista, neste caso, a string banana
print(l1) #vai imprimir [1, 2, 3]


l1 = [1,2,3,4,5,6,7,8,9]
del(l1[3:5]) #vai remover todos os elementos a partir indice 3 até o indice 5
print(l1) #vai imprimir [1, 2, 3, 6, 7, 8, 9]

l1 = [1, 'banana', 2, 3]
del(l1[1]); #Vai remover o elemento do indice 1 da lista, neste caso, a string 'banana'
print(l1) #vai imprimir [1, 2, 3]


l1 = [40,2,1,4,50,6,7,8,9]
print(max(l1)) #Vai imprimir o maior valor da lista, neste caso 50
print(min(l1)) #Vai imprimir o menor valor da lista, neste caso 1

print()
print('-----------------------------------------')
print()

r = range(1,10)
print(r) #vai imprimir apenas 'range(1, 10)', porém...
l1 = list(range(1,10)) #range usado numa função list, gera uma lista com numero dentro do range
print(l1) #vai imprimir [1, 2, 3, 4, 5, 6, 7, 8, 9]

print()
print('-----------------------------------------')
print()

l1 = list(range(0,100,8)) #dessa forma, no primeiro parametro (0), estou dizendo de qual valor vai iniciar a contagem, neste caso, vai começar do zero. O segundo numero é até quanto devo contar. O terceiro numero é de quanto em quanto devo contar
print(l1) #vai imprimir [0, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96]

print()
print('-----------------------------------------')
print()

l1 = [1,2,3,4,5]
for valor in l1: #usando um for para percorrer a lista gerada acima
    print(valor)

print()
print('-----------------------------------------')
print()

l1 = [1,2,3,4,5]
soma = 0
for valor in l1: #usando um for para percorrer a lista gerada acima
    soma = soma + valor
print(soma) #vai imprimir a soma de todos os valores da lista, será igual 15


print()
print('-----------------------------------------')
print()

l1 = ['String', True, 10, -20.5]
for elem in l1:
    print(f'O tipo do elemento é {type(elem)} e seu valor é: {elem}') #Vai percorrer a lista e imprimir o tipo de cada elemento e seu valor

print()
print('-----------------------------------------')
print()


variavel = ['Davidson Marcos', 'João Pereira', 'Maria']

for indice in variavel:
    if indice.lower().startswith('d'): #Essa função "startswith" Vai verificar se o conteudo no indice atual começa com a letra j
        print(f'{indice} começa com D')
    else:
        print(f'{indice} não começa com D')


print()
print('-----------------------------------------')
print()



variavel = ['João Pereira','Davidson Marcos', 'Maria']

comeca_com_d = False

for indice in variavel:
    if indice.lower().startswith('d'): #Ele vai converter a letra em minuscula e depois comparar com letra minuscula. Isso resovel o problema de não considerar a letra minuscula caso a letra seja maiuscula.
        comeca_com_d = True

if comeca_com_d:
    print('Existe uma palavra que começa com d')

else:
    print('Não existe uma palavra que começa com d')




print()
print('-----------------------------------------')
print()





secreta = 'Perfume'
digitadas = []
chances = 3

while True:
    print(f'Você têm {chances} chances')
    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Digite apenas uma letra animal.')
        continue

    digitadas.append(letra)


    if letra in secreta: #Vai transformar a letra em minuscula. Evita ter o problema de fazer distinção entre letra maiuscula e minuscula
        print(f'Isso ai! A letra {letra} existe na palavra secreta')
    else:
        print(f'Que pena! A letra {letra} não existe na palavra secreta')
        chances -= 1

        digitadas.pop()

    if chances == 0:
        print('Game over')
        break

    resultado = ''
    for letra_secreta in secreta:
        if letra_secreta in digitadas:
            resultado += letra_secreta
        else:
            resultado += '*'

    print(resultado)

    if resultado == secreta:
        print(f'Muito Bem! Você acertou a palavra secreta')
        break