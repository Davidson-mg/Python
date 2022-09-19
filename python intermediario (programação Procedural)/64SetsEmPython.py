#Sets(CONJUNTOS) são parecidos com com listas, tuplas e, especialmente dicionarios. Porém, a diferença maior é que só suportam elementos unicos.
#Sets não recebem chaves e valores, recebem apenas valores

s1 = {1, 'a', 45.5} #criando um set que possui numeros inteiros, string, numeros flutuantes
print(s1)
#Como Sets(CONJUNTOS) não possuem indices, não é possivel acessar os elementos pasando entre chaves o valor que corresponde ao indice desejado

for v in s1: #percorrendo meu set e imprimindo cada valor
    print(v)

print()
print('-------------------------------')
print()


# se = {} # Comentei para não criar. Se eu tento criar um set com abre e fecha chaves vazio, vai criar na verdade um dicionario
se = set() #Para eu criar um set vazio, precisa ser dessa forma
se.add(1) #Adicionando um elemento com valor 1 no meu set
se.add(2) #Adicionando mais um elemento mas com valor 2 no meu set
print(se) #vai imprimir: {1, 2}

se.add(2) #Neste caso, se eu tento adicionar um elemento que já existe no meu set, ele não cria mais uma posição com mais um elemento
print(se) #vai continuar imprimindo: {1, 2}

se.discard(2)#Vai remover a posição do elemento que possui valor 2
print(se) #vai imprimir: {1}

se.discard('a')

se.update('a')#Na função update, quando eu adicionando apenas um caracter, ele funciona como a função add...
se.update('Davidson')#... porém, se eu coloco um elemento com mais caracteres, ele vai desmembrar esse elemento, colocando cada caracter em uma posição. OBS IMPORTANTE: Essa função update não
# respeira ordem então, cada vez que inserir usando o uptate, vai inserir de forma aleatorio os caracteres
print(se) #Como o update insere os caracteres de forma aleatorio, no momento do teste imprimiu assim: {1, 'a', 'v', 'i', 'D', 's', 'o', 'd', 'n'}

se.update([1,2,3,4,5], (5,6,7)) #Inserindo uma lista e uma tupla usando o update. Lembrando, confome explicado acima, o update insere os caracteres de forma aleatoria
print(se) #Como o update insere os caracteres de forma aleatorio, no momento do teste imprimiu assim: {'d', 1, 'o', 2, 'i', 'v', 3, 4, 'D', 5, 'a', 6, 7, 'n', 's'}.
#Repare que neste ultimo print, o numero 5 aparece duas vezes, uma lista e outra na tupla, mesmo assim o set não aceita valores iguais repetidos.

#Usando um set para remover elementos duplicados de uma lista
li = [1,1,2,3,4,5,6,7,6,6,6,7,8,9, 'Davidson', 'Davidson'] #Lista com elementos duplicados
li = set(li) #Conforme dito antes, sets não aceita elementos duplicados, então, basta eu transforma minha lista em um set. #OBS: Vale lembrar que o set pode converter e colocar os elementos fora de ordem
li = list(li) #Transformando novamente minha variavel li em lista
print(li) #Vai imprimir {1, 2, 3, 4, 5, 6, 7, 8, 9, 'Davidson'}

print()
print('-------------------------------')
print()

s1 = {1,2,3,4,5}
s2 = {1,2,3,4,5,6}
s3 = s1 | s2 #unindo s1 com s3. Neste caso apenas o elemento 6 será unificado, pois todos os outros se repetem e, conforme dito antes, sets não aceitam valores duplicados

print(s3) #vai imprimir: {1, 2, 3, 4, 5, 6}


print()
print('-------------------------------')
print()

s1 = {1,2,3,4,5}
s2 = {1,2,3,4,5,6}
s3 = s1 & s2 #Vai considerar apenas os elementos que aparecem em ambos os sets, porém, como não conforme dito antes, sets não aceitam valores duplicados, então, vai salvar apenas uma vezes os elementos
#duplicados e, neste caso, eleminar o elemento de valor 6. Vai imprimir: {1, 2, 3, 4, 5}

print(s3) #vai imprimir: {1, 2, 3, 4, 5, 6}

print()
print('-------------------------------')
print()

s1 = {1,2,3,4,5,7}
s2 = {1,2,3,4,5,6}
s3 = s1 - s2 #Vai salvar em s3 apenas os elementos que existem SOMENTE NO SET A ESQUERDA DO SINAL DE MENOS. Vai imprimir: {7}

print(s3) #Vai imprimir: {7}

print()
print('-------------------------------')
print()

s1 = {1,2,3,4,5,7}
s2 = {1,2,3,4,5,6}
s3 = s1 ^ s2 #Vai salvar em s3 apenas os elementos que existem em s1 e s3, neste caso, 7 e 6

print(s3) #vai imprimir: {6, 7}


print()
print('-------------------------------')
print()


l1 = ['Davidson', 'Marcos', 'Gomes']
l2 = ['Davidson', 'Marcos', 'Gomes', 'Davidson', 'Marcos', 'Gomes']

if set(l1) == set(l2): #Usando o set num if para verificar se as listas acimas são iguais no caso de listas que possuem muitos valores, mas repetidos.
    # Neste caso não vai alterar as listas l1 e l2 originais
    print('L1 é igual a l2')
else:
    print('L1 é diferente de L2')