


#                                                          ITERAVEIS
lista = [0,1,2,3,4,5] #lista é um iteravel
print(hasattr(lista, '__iter__')) #hasattr que verifica se um obj possui o metodo '__iter__'. Se tiver, retorna true, ou seja, é iteravel

#OBS IMPORTANTE: se um obj é iteravel, podemos usar um for para consultar os elementos

print()
print('----------------------------------')
print()

#                                                           ITERADOR
#Quando um obj é iteravel, podemos usar um for para consultar os elementos e, quando usamos o for, ele transforma o obj num iterador. Por exemplo, exibir cada valor de uma lista

lista = [0,1,2,3,4,5] #lista é um in
print(hasattr(lista, '__next__')) #hasattr que verifica se um obj possui o metodo '__next__'. Se tiver, retorna true. Neste caso, vai retornar false
#pois a lista não é um iterador. Se usarmos um for para percorrer essa lista, ai sim vai ser transformada num iterador ser exibida

lista= iter('__iter__') #Transformando minha lista num iterador ao adicionar o metodo iter
print(hasattr(lista, '__next__')) #Agora vai retornar true

print()
print('----------------------------------')
print()

lista = [0,1,2,3,4,5]
lista = iter(lista) #Transformando minha lista num iterador ao adicionar o metodo iter

print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista)) #o next é um metodo iterador e mostra um elemento de cada vez em sequencia a medida que lhe utilizamos.
# Vai imprimir na sequencia
# 0
# 1
# 2
# 3
# 4
# 5


print()
print('----------------------------------')
print()

#                                                      GERADORES

#Numa função simples, uma lista é gerada primeiro totalmente para só depois ser transformada num iterador e depois ser exibida na chamada da função.
#Se for uma lista muito grande de uma situação real, pode consumir muito da maquina



import sys #é necessario esse import para usar o comando sys.getsizeof abaixo
import time#é necessario esse import para usar o comando time

lista = list(range(10))
print(sys.getsizeof(lista)) #Esse comando sys.getsizeof vai imprimir quanto minha lista está consumindo de memoria


print()
print('----------------------------------')
print()



def gera(): # IMPORTANTE, ESSA FUNÇÃO, É UMA FUNÇÃO SIMPLES QUE USAMOS GERALMENTE PARA GERAR UMA LISTA. Só Estamos criando essa função com elemento time.sleep(0.1)
    # apenas para simular algum programa pesado

    #Numa função comum como esta, a lista é gerada primeiro totalmente para só depois ser transformada num iterador e depois ser exibida na chamada da função.
    #Se for uma lista muito grande de uma situação real, pode consumir muito da maquina

    r = [] #Cria um array
    for n in range(10): #Faz a iteração até 100 (range)
        r.append(n) #vai adicionando os valores de n (range) no array
        time.sleep(0.1) #Faz o interpretador do python 'dormir' por 0.1s. Isso vai fazer ele demorar a gerar a lista para só depois responder ao for
        #do lado de fora na chamada desta função
    return r #retornar o valor de r

g = gera()

for v in g:
    print(v)


print()
print('----------------------------------')
print()


def gera2():
    for n in range(10): #Faz a iteração até 100 (range)

        yield n #Estamos trocando este 'r.append(n)' por este 'yield n'. Com isso ao inves de gerar a lista toda primeiro, para só depois ser transformada num iterador
        # e depois ser exibida na chamada da função conforme uma função de lista comum e conforme exemplo acima, ele vai de cara transformar os elementos em ITERAVEIS, retornando
        #direto na chamada da função um elemento por vez, gerando uma resposta mais rapida na execução dos valores

        time.sleep(0.1) #Faz o interpretador do python 'dormir' por 0.1s. Isso vai fazer ele demorar a gerar a lista para só depois responder ao for
        #do lado de fora na chamada desta função


g2 = gera2()

# for v in g2:
#     print(v)

print(next(g2))
print(next(g2))
print(next(g2))#Dessa forma, posso usar o next(g2) para ir imprimindo na sequencia.
# Vai imprimir na sequencia


print()
print('----------------------------------')
print()


def gerando():
    variavel = 'valor 1'
    yield variavel
    variavel = 'valor 2'
    yield variavel
    variavel = 'valor 3'
    yield variavel

ge = gerando()

print(next(ge)) #Na primeira vez que eu executar, vai retornar 'valor 1'
print(next(ge)) #Na segunda vez que eu executar, vai retornar 'valor 2'
print(next(ge)) #Na terceira vez que eu executar, vai retornar 'valor 3'
#print(next(ge)) #Na quarta vez que eu executa, vai dar erro. Por isso tá comentado


print()
print('----------------------------------')
print()

l1 = [x for x in range(1000)] #Criando uma lista usando listComprehension
print(type(lista)) #Vai imprimir <class 'list'>
l2 = (x for x in range(1000)) #com o parentese, estamos criando um gerador
print(type(lista)) #Vai imprimir <class 'generator'>

print(sys.getsizeof(l1)) #repare que a l1 consume 4508Bytes
print(sys.getsizeof(l2)) #e l2 está consumindo 88. E isso vai se manter mesmo que aumentemos o tamanho das duas

#Isso vai acontecer pelo motivo explicado acima na linha 50. Uma lista comum pega todos os valores e adiciona na memoria, já os geradores, armazenam um de cada vez conforme solicitado