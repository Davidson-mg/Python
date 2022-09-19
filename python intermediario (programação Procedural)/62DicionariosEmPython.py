#Dicionario é parecido com listas. A maior diferença é que as listas geram indicies (tb chamadas de chaves) pra vc.
#Em um Dicionario, nós controlamos os indices (tb chamadas de chaves)

print()

d1 = {'chave1':'Davidson'} #O primeiro valor antes de ':' é o nome da chave (nome do indice)

print(d1) #vai imprimir: {'chave1': 'valor da chave'}

d1['nova_chave'] = 'Valor da nova chave' #adicionando um novo elemento ao meu dicionario com o nome de sua segunda chave

print(d1) #vai imprimir: {'chave1': 'valor da chave', 'nova_chave': 'Valor da nova chave'}

print(d1['chave1']) #Imprimindo ou acessando o elemento da chave com nome de 'chave1'

print()
print("--------------------------------------------")
print()


d1 = dict(chave1='Davidson') #outra forma de criar um dicionario
d1['chave2'] = 'Marcos' #criando uma segunda chave (chave2) no dicionario 'd1' e informando o seu valor

print(d1) #vai imprimir: {'chave1': 'Davidson', 'chave2': 'Marcos'}


print()
print("--------------------------------------------")
print()



d1 = {'chave1':'Davidson', 'chave1':'Davidson', 'chave1':'Valor real da chave'} #aqui, eu estou criando um dicionario com 3 chaves mas todas elas com o mesmo nome. Quando eu imprimir, será considerado apenas o valor da ultima vez que essa chave aparecer
print(d1) #vai imprimi: {'chave1': 'Valor real da chave'}


d1 = {'chave1':'Davidson', 'chave2':'Marcos', 'chave3':'Valor real da chave'}
print(d1) # vai imprimir: {'chave1': 'Davidson', 'chave2': 'Davidson', 'chave3': 'Valor real da chave'}
print(d1['chave2']) #vai imprimir: 'Marcos'





print()
print("--------------------------------------------")
print()


d1 = {'str':'valor', 10:'outro valor', (1,'b',3): 'Mah ooeeeee'} #criando um dicionario com nomes chaves de tipos imutaveis e de diferentes tipos.
# Neste caso, a primeira chave cujo nome é do tipo string, outra cujo nome é do tipo inteira e, por fim, uma com nome cujo tipo é uma tupla

print(d1[(1,'b',3)]) #Vai imprimir o valor da terceira chave, neste caso, vai imprimir: 'Mah ooeeeee'


#print(d1['naoExiste']) #Vai da erro, por isso está comentado. Tentando acessar uma chave que não existe. Caso a chave não exista, podemos resolver conforme abaixo

if 'naoExiste' not in d1: #se a chave 'naoExiste' não está em meu dicionario 'd1' ...
    print('Chave não existe mas vamos cria-la')
    d1['naoExiste'] = 'Agora existe' #criando uma chave com nome de 'naoExiste' dentro de minha tupla d1
else:
    print('Executando qualquer coisa')


print()
print("--------------------------------------------")
print()


d1 = {'str':'valor', 10:'outro valor', (1,'b',3): 'Tupla'}

#Outra forma de executar e verificar uma chave que não existe em meu dicionario
print(d1.get('NomeDaChave')) #A usar o .get, caso a chave não exista, ele apenas mostra 'None' e não para o resto do codigo por conta de um erro

if d1.get('NomeDaChave') is not None: #se 'NomeDaChave' em relação ao dicionario d1 é 'None' (não existe)...
    print(d1.get('NomeDaChave')) #neste caso isso não será executado pois a chave 'NomeDaChave' não existe
else:
    print('Olá, Mundo!')



print()
print("--------------------------------------------")
print()



d1 = {'nome':'Deivison', 'Idade':60, 'Sexo':'M', 'corPreferida':'Azul escuro'}
print(d1)

d1['Idade'] = 31 #Alterando um valor de uma das chaves, neste caso 'idade' de meu dicionario
print(d1)

d1.update({'nome':'Davidson'}) #Outra forma de alterar um valor de uma das chaves. Neste caso estou corrigindo meu nome
print(d1)

del d1['corPreferida'] #apagando uma chave e seu conteudo
print(d1)



print()
print("--------------------------------------------")
print()

d1 = {'nome':'Davidson', 'Idade':60, 'Sexo':'M', 'corPreferida':'Azul escuro'}

print('Idade' in d1) #Vai verificar se existe uma chave com nome de 'idade' no dicionario d1. Vai imprimir True
print('CorCabelo' in d1.keys())# Outra forma de verificar se existe uma chave com nome informado. Vai imprimir False
print(80 in d1.values()) #Vai verificar se existe algum valor no meu do tipo inteiro 80 no meu dicionario d1. Vai imprimir False

print(len(d1)) #Vai imprimir quantos pares(indices) temos em nosso dicionario


print()
print("--------------------------------------------")
print()
#       0       1             0          1            0             1
d1 = {'nome':'Davidson', 'Idade':60, 'Sexo':'M', 'corPreferida':'Azul escuro'}

print()
for v in d1: #Dessa forma, vai imprimir o nome da chave apenas
    print(v)

print()
for v in d1.values(): #Dessa forma, vai imprimir os valores
    print(v)


print()
for v in d1.items(): #Dessa forma, vai imprimir as chaves e os valores do dicionario no formato de tuplas. Como eu defini apenas uma variavel (v) no for,
    #Ele vai automaticamente entender que essa variavel engloba tudo, tanto chave quato valores, por isso mostra no formato de tuplas
    print(v)


print()
for v in d1.items(): #Dessa forma, vai imprimir chaves e os valores sem ser no formato de tuplas.
    print(v[0], v[1])

print()
for f, v in d1.items(): #Dessa forma, vai ter o mesmo resultado do exemplo acima, imprimindo chaves e os valores sem ser no formato de tuplas, porém, não precisa eu passar os indices.Como eu defini
    # duas variaveis nesse for, ele vai entender automaticamente que essas duas variaveis correspondem a dois indices do dicionario 'd1'. Por isso, se eu chamasse apenas uma das variaveis
    # dentro do for, ele entenderoa que se refere apenas ao primeiro indice.
    print(f, v)

print()
print("--------------------------------------------")
print()

clientes = {
    'cliente1':{
        'nome': 'Davidson',
        'Sobrenome':'Marcos',
    },
    'cliente2' : {
        'nome' : 'Maria',
        'Sobrenome':'Madalena'
    }
}


print()

for clientes_k, clientes_v in clientes.items(): #Como eu defini duas variaveis nesse for, ele vai entender automaticamente que essas duas variaveis correspondem
    # a dois indices do dicionario 'clientes'. Por isso, se eu chamo apenas uma das variaveis dentro do for, ele entende que se refere apenas ao primeiro indice.
    #Se no for eu tivesse defindo apenas uma variavel, semelhante aos exemplos acima, ele entenderia automaticamente que essa unica variavel corresponde ao
    #obj completo e mostraria numa unica variavel tanto o nome da chave quanto os valores no formato de tupla

    #Ou seja, clientes_k corresponde a chaves e clientes_v corresponde a aos elementos/dados da respectiva chave
    print(f'Exibindo {clientes_k}') #Aqui estou printando apenas a primeira variavel, então ele entende automaticamente que se refere a chave apenas

    for dados_k, dados_v in clientes_v.items(): #Dentro deste for eu estou verificando o segundo indice (clientes_v) do for externo, que corresponde as dados e não as
        # chaves. Como estou dizendo que esse for verifica os dados e usamos duas variaveis dados_k e dados_v, automaticamente serão entendidas como indices 0 e 1 respectivamente
        print(f'\t{dados_k} = {dados_v}')

print()

#Mesma coisa do exemplo acima. Estava apanas refazendo pra praticar
for i, j in clientes.items():
    print(f'Exibindo {i}')
    for i, j, in j.items():
        print(f'\t{i} = {j}')



print()
print("--------------------------------------------")
print()

# #possibilitar copiar dicionarios e listas. Só não é necessario para tuplas pois tuplas não podem ser alteradas, são imutaveis
# import copy #inserir este comando no topo do arquivo possibilita usar o comando abaixo
#
# d1 = {'chave1':'Davidson', 'chave2':57, 'chave3':25.45}
#
# d2 = copy.deepcopy() #Para copiar um dicionario para outra variavel. Se eu usasse apenas o igual, ele copiaria apenas a referencia
