li = [1,2,3,'a',4,'c']

l2 = [var for var in li] #Neste caso, criando um nova lista que será armazenada na variavel l2. Ao usar o for dentro de
#couchete para percorrer li, estamos percorrendo a lista acima li, armazenando na variavel var, que por sua vez
#armazena na variavel lista l2

print(li) #vai imprimir: li = [1,2,3,'a',4,'c']
print(l2) #vai imprimir: li = [1,2,3,'a',4,'c']



l2 = [var * 2 for var in li] #Neste caso, estou multiplicando cada elemento da lista li por 2 e armazenando na lista l2
print(l2) #Vai imprimir [2, 4, 6, 'aa', 8, 'cc']


print()
print('----------------------------')
print()


li=[1,2,3]

l2 = [(i, j) for i in li      for j in range(3)] #Estamos armazenando em l3 uma lista e, essa lista será composta de tuplas, por isso parenteses.
#Essas tuplas terão duas variaveis (i, j), onde o primeiro for vai armazenar na primeira variavel (i) e o segundo for na segunda variavel (j).
#O primeiro for (i) vai armazenar os valores de l1 e o segundo for (j) vai armazenar apenas numeros (range) que vão até o 3, como se fossem indices
print(l2) #Vai imprimir assim: [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2)]

print()
print('----------------------------')
print()

l1=['Davidson', 'Marcos', 'Gomes']
l2 = [v.replace('a', '@') for v in l1] #Replace diz que para cada 'a' encontrado, substitua-o por '@'.
print(l2)#Vai imprimir assim: ['D@vidson', 'M@rcos', 'Gomes']

l2 = [v.replace('a', '@').upper() for v in l1] #Replace diz que para cada 'a' encontrado, substitua-o por '@'. Com o .upper() estou tranformando
#todas as letras em maiusculas
print(l2)#Vai imprimir assim: ['D@vidson', 'M@rcos', 'Gomes']


print()
print('----------------------------')
print()

tupla = ( #Tupla com duas tuplas dentro
    ('chave', 'valor'),
    ('chave2', 'valor2')
)

l2 = [(x, y) for x, y in tupla] #As variaveis x e y dentro uma tupla (), vão receber os valores de x e y do for que percorre a tupla acima
# e será armazenado na variavel do tipo tupla l2
print(l2) #Vai imprimir assim: [('chave', 'valor'), ('chave2', 'valor2')]

l2 = [(y, x) for x, y in tupla] #estou fazendo a mesma coisa acima, porém, como inverti a ordem de x e y dentro da tupla () antes do for, vai apenas
#salvar invertido as posições
print(l2) #Vai imprimir assim: [('valor', 'chave'), ('valor2', 'chave2')]

l2 = dict(l2) #apenas transformando minha lista l2 em um dicionario
print(l2) #Vai imprimir assim: {'valor': 'chave', 'valor2': 'chave2'}


print()
print('----------------------------')
print()

l1 = list(range(50)) #Estou criando uma lista com numeros gerados automaticamente (range) que vai até 50
l2 = [v for v in l1 if v % 2 == 0] #A variavel 'V' vai receber do for os valores da lista l1 que vai percorrer. Neste caso,
#ao utilizar o if, estamos dizendo para pegar somente valores divisiveis por 2
print(l2) #Vai imprimir: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]

l2 = [v for v in l1 if v % 3 == 0 if v % 8 == 0] #Estou fazendo a mesma coisa do exemplo acima. A diferença é que adicionei um segundo if
#Ou seja, vai pegar somente os numeros que são divisiveis por 3 e também por 8
print(l2) #Vai imprimir: [0, 24, 48]

l2 = [v if v % 3 else 'Não é' for v in l1] #Aqui estou usando um if com else. Repare que, ao contrario dos exemplos acima que só possuem if sem o else,
#neste caso somos obrigados a colocar o if else antes do for, mas ainda sim, depois da variavel que vai receber os valores. Aqui estou pegando os valores#
#que são divisiveis por 3, caso não seja, salve a string 'não é'
print(l2) #Vai imprimir assim: ['Não é', 1, 2, 'Não é', 4, 5, 'Não é', 7, 8, 'Não é', 10, 11, 'Não é', 13, 14, 'Não é', 16, 17, 'Não é', 19, 20, 'Não é', 22, 23, 'Não é', 25, 26, 'Não é', 28, 29, 'Não é', 31, 32, 'Não é', 34, 35, 'Não é', 37, 38, 'Não é', 40, 41, 'Não é', 43, 44, 'Não é', 46, 47, 'Não é', 49]

l2 = [v if v % 3 and v % 8 else 'Não é' for v in l1] #Estou fazendo a mesma coisa do exemplo acima. A diferença é que adicionei um and
print(l2)


print()
print('----------------------------')
print()

carrinho = []
#                     0        1
carrinho.append(('produto 1', 30)) # 0
carrinho.append(('produto 2', 20)) # 1

produto, preco = carrinho [0] #duas variaveis produto e preco vao receber respectivamentes 'produto 1' e 30 na ordem
print(produto, preco)

#         0                  1         indices
# (       x       )  (       x       ) Uma variavel
# (       x       )  (       y       ) duas ou mais variaveis
# (    x        y )  (    x         y)
#      0        1          0        1  indices
#[('produto 1', 30), ('produto 2', 20)]

total = [(x, y) for x, y in carrinho] #Com duas variaveis x e y, cada variavel corresponde a uma tupla ()
print(total) #Vai imprimir: [('produto 1', 30), ('produto 2', 20)]

print()
#         0   #Esse x corresponde a primeira tupla, que é equivalente ao indice 0 inicialmente, A medida em que o for vai percorrendo a lista, passar a valer 1 ou mais tuplas
total = [float((x[1])) for x in carrinho] #Como eu usei apenas uma variavel x vai receber o indice que corresponde a tupla atual,
# vai entender que essa variavel correponde a tupla como com todos os elementes e, cada elemento da tupla, têm seu indice
print(sum(total))

print()

total = sum([float(y) for x, y in carrinho]) #Dessa forma, como estou usando duas variaveis no for, ao chamar apenas o y, ele entende que o y corresponde ao segundo elemento da tupla
#O sum vai somar tudo
print (total)



