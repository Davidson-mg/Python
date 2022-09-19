def divisao(n1, n2):
    return n1 / n2

resultado = divisao(4, 2)

print(resultado)

print()
print('----------------')
print()

def divisao2(n1, n2):
    return n1/n2

#resultado = divisao2(8, 0) #Vai da erro pq o python não permiti dividir um numero por zero. Corrigimos isso abaixo

print(resultado)

print()
print('----------------')
print()

def divisao3(n1, n2):
    if(n2>0): #se n2 for maior que zero, retorna a divisão, senão, neste caso vai retorno 'none'
     return n1/n2


resultado = divisao3(8, 0)

if resultado: # O valor de 'none' é considerado falso. Se resultado é True ...
    print(resultado)
else: # Se resultado é false ...
    print('Numero invalido')


print()
print('----------------')
print()

#outra forma de fazer para ter o mesmo resultado do exemplo acima
def divisao4(n1, n2):
    if(n2 == 0): #se n2 for igual a zero, vai retornar none, senão, fora do if, retorna a divisão de n1 por n2. Lembrando que em funções, quando o python vê um return, ele não executa nada que tiver depois disso
     return

    return n1/n2


resultado = divisao4(8, 0)

if resultado: # O valor de 'none' é considerado falso. Se resultado é True ...
    print(resultado)
else: # Se resultado é false ...
    print('Numero invalido')


print()
print('----------------')
print()


def f (var):
    print(var)

def dumb():
    return f

var = dumb() #Neste caso, dumb vai retorno a função f, logo, a variavel var passa a ser do tipo (type) function, pq está recebendo uma função como retorno


if var == f:
    print('Var é igual a F') # conforme dito acima, var está recebendo uma função que vai retornar a função f como parametro, logo var passa a ser igual f. Por isso, essa condição será satisfeita
else:
    print('Var não é igual a F')


var2 = dumb()('E colocar esse segundo parentese') #Como estou chamando uma função que vai retornar uma segunda função como parametro, posso passar um segundo parentese com um valor que será executado na segunda função




print()
print('----------------')
print()


def text ():
    return ('Davidson', 'Marcos') #Quando colocamos entre parentese, ser torna uma variavel do tipo tupla
    #Até esse ponto ele apenas disse que tuplas são parecidos com listas mas não podem ser alterados. Creio que seja mais parecido com vetor

v = text()

print(type(v), v) #Vai retornar: <class 'tuple'> ('Davidson', 'Marcos')

print(v[1]) #Vai imprimir: Marcos. Tuplas podem ser acessadas como vetor, passando o indice entre couchetes 