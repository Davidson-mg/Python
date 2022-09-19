
print()
print('----------------------')
print()

def func(a1, a2, a3, a4, a5, a6=None): #No caso do a6, não sou obrigado a passa-lo como parametro quando chamar esta função
    print(a1, a2, a3, a4, a5)

func(1,2,3,4,5)#Conforme dito acima, não sou abrigado a passar o a6 por telo-lo definido como none na função.

func(1,2,3,4,5, a6='Davidson') #Conforme dito acima, não sou abrigado a passar o a6 por telo-lo definido como none nda função, mas posso passar se eu quiser, sendo necessario informar o valor da variavel



print()
print('----------------------')
print()


# def func2 (a1, a2, a3, a4, a5, a6=None, a7): Nesse caso daria erro (por isso coloquei como comentario), pois uma vez que vc têm um argumento None, todos os outros após ele devem seguir o mesmo padrão conforme mostrado abaixo
#     print(a1, a2, a3, a4, a5)

def func2 (a1, a2, a3, a4, a5, a6=None, a7=None):
    print(a1, a2, a3, a4, a5, a6, a7)

func2(1,2,3,4,5, a6='Davidson', a7='5')

var = func2(10,20,30,40,55, a6='Davidson Marcos', a7='50')

print(var) #Vai retorna None pq a func2 não é uma função que retorna valores, mas sim uma função que executa, neste caso, vai imprimir diretamente


print()
print('----------------------')
print()


def func3 (a1, a2, a3, a4, a5, a6=None, a7=None):
    print(a1, a2, a3, a4, a5, a6, a7)
    return a6, a4

func3(1,2,3,4,5, a6='Davidson', a7='5')

var = func3(10,20,30,40,55, a6='Davidson Marcos', a7='50')

print(type(var), var) #Vai retorna uma tupla e o valor da variavel: <class 'tuple'> ('Davidson Marcos', 40)
print(var[1]) #como é uma tupla, para acessar os elementos, precisa informar o indice, semelhante a um vetor.



print()
print('----------------------')
print()



#Abrindo parenteses afim de relembrar alguns detalhes sobre desempacotamento de lista explicado na aula 43DesempacotamentoDeListasEmPython

lista = [1,2,3,4,5]
n1, n2, *n3 = lista #Lembrando que neste caso n1 e n2 vai receber os respectivos dois primeiros valores da lista e a variavel com * n* vai receber uma lista com os demais valores. Foi explicado na aula 43DesempacotamentoDeListasEmPython

print(lista) #Estou imprimindo a lista como ela é. vai imprimir: [1,2,3,4,5]
print(*lista) #Com o * na chamada da variavel lista, estou desempacotando a lista pra depois imprimir. Vai imprimir: 1 2 3 4 5
print(*lista, sep='-')#Com o * na chamada da variavel lista, estou desempacotando a lista pra depois imprimir. O "sep='-'" é um elemento da função print que ser apenas para adicionar o separador na exibição dos elementos. Vai imprimir: 1-2-3-4-5

#fechando parentese



def func4(*args): #Usamos o *args quando não sabemos quantos parametros vamos passar ao chamar a função

    print(args) #Vai imprimir uma tupla com os valores passados como parametro na chamada da função: Vai imprimir: (1, 2, 3, 4, 5)
    print(args[3]) #Como em listas, se eu quiser acessar um elemento especifico da tupla, vou precisar informar o indice entre couchetes: Vai imprimir 4
    print(args[-1]) #Com -1 entre couchetes, estou pegando o ultimo elemento da tupla. Vai imprimir 5
    print(len(args)) #Vai imprimir o tamanho do meu args, que neste caso será 5

    for v in args: #Posso também trabalhar tuplas com for ou while semelhante a listas
        print(v)

    #args[0] = 20 #Vai da erro, por isso está comentado. Não posso alterar o indice de uma tupla dessa forma, eu teria que converter em uma lista primeiro, conforme abaixo

    args = list(args) #convertendo minha tupla args em list
    args[0] = 20 #Agora sim posso alterar qualquer indice do meu args
    print(args)



func4(1,2,3,4,5)


print()
print('----------------------')
print()

def func5(*args):
    print(args)

lista = [1,2,3,4,5]
func5(lista) #Neste caso, vai gerar uma tupla cujo o primeiro elemento será a lista. Vai imprimir assim: ([1, 2, 3, 4, 5],)
func5(lista, 5) #Neste caso, vai gerar uma tupla cujo o primeiro elemento será a lista e o segundo elemento será o valor 5. Vai imprimir assim: ([1, 2, 3, 4, 5], 5)
func5(*lista) #O ideal é enviar a lista desempacotada para a função, usando o *. Dessa forma, teremos uma tupla com os valores da lista separados. Vai imprimir assim: (1, 2, 3, 4, 5)
func5(*lista, 10, 20, 30)##O ideal é enviar a lista desempacotada para a função, usando o *. Dessa forma, teremos uma tupla com os valores da lista separados e podemos ainda adicionar outros valores que serão incluidos numa unica tupla. Vai imprimir assim: (1, 2, 3, 4, 5, 10, 20, 30)

lista2 = [100, 200, 300]
func5(*lista, *lista)#O ideal é enviar a lista desempacotada para a função, usando o *. Dessa forma, teremos uma tupla com os valores da lista separados. Neste caso, estamos enviando duas listas desempacotadas que se tornarão uma unica tupla. Vai imprimir assim: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)


print()
print('----------------------')
print()


def func6(*args, **kwargs): #**kwargs serve para argumentos nomeados
    print(args)
    print(kwargs)




lista = [10,20,30,40,50]
lista2 = [100,200,300]

func6(*lista, *lista2, nome='Davidson', sobrenome='Gomes') #Nesse caso, a duas primeiras variaveis de lista como parametro, serão usadas pelo parametro *args e as variaveis nomeadas pelo parametro **kwargs. Vai imprimir assim:   (10, 20, 30, 40, 50, 100, 200, 300)
#                                                                                                                                                                                                                                    {'nome': 'Davidson', 'sobrenome': 'Gomes'}




print()




def func6(*args, **kwargs): #**kwargs serve para argumentos nomeados
    print(args)
    print(kwargs['nome'], kwargs['sobrenome']) #Umda das formas de imprimir as variaveis nomeadas



lista = [10,20,30,40,50]
lista2 = [100,200,300]

func6(*lista, *lista2, nome='Davidson', sobrenome='Gomes') #Vai imprimir:  (10, 20, 30, 40, 50, 100, 200, 300)
#                                                                           Davidson Gomes



print()







def func6(*args, **kwargs): #**kwargs serve para argumentos nomeados
    print(args)
    nome = kwargs.get('nome') #outra forma de imprimir e melhor algum valor de uma variavel nomeada. Neste caso vamos imprimir apenas uma delas, variavel nome no caso.
    print(nome)



lista = [10,20,30,40,50]
lista2 = [100,200,300]

func6(*lista, *lista2, nome='Davidson', sobrenome='Gomes') #Vai imprimir:  (10, 20, 30, 40, 50, 100, 200, 300)
#                                                                           Davidson





print()






def func6(*args, **kwargs): #**kwargs serve para argumentos nomeados
    print(args)

    idade = kwargs.get('idade') #Idade não existe, então armazena None em idade. Essa é outra forma de imprimir e melhor algum valor de uma variavel nomeada. Neste caso vamos imprimir apenas uma delas, variavel idade.
    if idade is not None: #Estamos verificando se a variavel 'idade' existe. Se não existe, vai armazenar none em idade. Se idade não é None...
        print(f'Idade: {idade}')
    else:
        print('Idade não existe')



lista = [10,20,30,40,50]
lista2 = [100,200,300]

func6(*lista, *lista2, nome='Davidson', sobrenome='Gomes') #Vai imprimir:  (10, 20, 30, 40, 50, 100, 200, 300)
#                                                                           Idade não existe

func6(*lista, *lista2, nome='Davidson', sobrenome='Gomes', idade=66) #Vai imprimir:  (10, 20, 30, 40, 50, 100, 200, 300)
#                                                                                     Idade: 66