file = open('abc.txt', 'w+') #estou abrindo um arquivo. Entre parentese, em 'abc.txt' estou informando o nome do arquivo para leitura
#ao acresncetar 'w+', estou dizendo que quero leitura e escrita. O w+ tamém sobrescreve o arquivo caso eu o abra dessa forma em outros momento

file.write('Linha1\n') #estou escrevendo 'linha1' dentro do meu arquivo
file.write('Linha2\n')
file.write('Linha3\n')

file.seek(0,0)#ABAIXO, VAMOS USAR O COMANDO file.read() PARA LER O ARQUIVO, PORÉM, O COMANDO READ() faz a leitura do arquivo por meio do cursor,
#e eu estou abrindo depois de inserir novas linhas. Isso quer dizer que meu cursor dentro do arquivo estará depois de ter inserido a 'linha3'
# consequentemente, neste caso não vai imprimir nada. POR ISSO É NECESSARIO O COMANDO FILE.SEEK() ANTES DO COMANDO READ. O comando
#file.seek vai colocar o curso no inicio. O primeiro zero entre parentese se refere a posição do curso, e o segundo se refere a relatividade que está buscando.

print('Lendo Linhas')
print(file.read()) #Vai imprimir no console o conteudo do arquivo, porém, vale dizer que ele faz a leitura do arquivo por meio do cursor,
# eu estou abrindo depois de inserir novas linhas. Isso quer dizer que meu curso dentro do arquivo estará depois ter inserido a 'linha3',
# consequentemente, neste caso não vai imprimir nada.

file.seek(0,0) #Lenvando o cursor para o topo do arquivo novamente, conforme explicado acima.

print(file.readline(), end='') #Vamos ler apenas uma linha considerando o local onde está o cursor.
print(file.readline(), end='') #Novamente lendo mais uma linha. Neste caso, como jé tinhamos lido uma linha acima, ele vai continuar
#de onde parou. Ou seja, na primeira vez que executamos o comando, ele leu a linha 1, já na segunda vez, vai ler a linha 2.
#Esse 'end' no final serve apenas para impedir que ele dê quebra de linha, pois quando escrevemos as linhas no arquivo nos comandos
#file.write, nós usamos o '\n' para quebra de linha.

file.close() #terminei de escrever/usar o arquivo, agora estou fechando. Ao rodar a aplicação, neste ponto o arquivo será criado
#na mesma pasta do deste arquivo python e vai aparecer no arquivo do PyCharm no lado esquerdo.


print()
print('-----------------------')
print()

#lendo o arquivo já existente
file = open('abc.txt') #Abro o arquivo

print(file.readlines()) #Vai imprimir linha por linha num formato de lista. Vai imprimir assim: ['Linha1\n', 'Linha2\n', 'Linha3\n']

file.seek(0,0) #Lenvando o cursor para o topo do arquivo novamente, conforme explicado acima.

print()
for linha in file.readlines(): #Lendo as linhas do arquivo como se fosse uma lista
    print(linha, end='') #Esse 'end' no final serve apenas para impedir que ele dê quebra de linha, pois quando escrevemos as linhas no arquivo nos comandos
print()
file.seek(0,0) #Lenvando o cursor para o topo do arquivo novamente, conforme explicado acima.

for linha in file: #Também posso percorrer e imprimir as linhas do arquivo usando apenas file
    print(linha, end='')

file.close()#fechando o arquivo


print()
print('-----------------------')
print()

try: #Alguns programadores, ao abrir e manipular um arquivo, fazem dentro de um blco try, pois como vc precisa fechar, o 'finally' cae bem nessa situação
    file = open('abc.txt', 'a+') #Quando usamos o 'a+', estamos dizendo que o cursor inicia após a ultima linha, possibilitando acrescentarmos conteudo ao arquivo
    #sem apagar/sobrescrever o conteudo atual
    file.write(f'linha4\n')
    file.seek(0)
    print(file.read())
    file.close()
finally:
    file.close() #fechando o arquivo


print()
print('-----------------------')
print()

with open ('abc.txt', 'a+') as file:#Forma mais Pythonica é usar esse gerenciador de contexto. Ele fecha sozinho seu arquivo depois de executar tudo que têm dentro dele
    file.write(f'linha5\n')


    file.seek(0)
    print(file.read())

print()
print('-----------------------')
print()

with open ('abc.txt', 'a+') as file:#Forma mais Pythonica é usar esse gerenciador de contexto. Ele fecha sozinho seu arquivo depois de executar tudo que têm dentro dele
    file.write(f'linha6\n')
    file.write(f'linha7\n')
    file.write(f'linha8\n')

    file.seek(0)
    print(file.read())

print()
print('-----------------------')
print()

import os
os.remove('abc.txt') #Removendo meu arquivo






print()
print('-----------------------')
print()

#convertendo para json

import json

lista = { #criando uma lista de pessoas

    'pessoa 1':{'nome':'Davidson', 'idade':187},
    'pessoa 2':{'nome':'Maria','idade':57}

}

print(lista) #apenas dando um print. Vai imprimir: {"pessoa 1": {"nome": "Davidson", "idade": 187}, "pessoa 2": {"nome": "Maria", "idade": 57}}

# d1_json = json.dumps(lista) #convertendo minha lista 'lista' para json. Comentei pois vou usar o exemplo abaixo com indent=True
# print(d1_json) #vai imprimir: {"pessoa 1": {"nome": "Davidson", "idade": 187}, "pessoa 2": {"nome": "Maria", "idade": 57}}

d1_json = json.dumps(lista, indent=True) #convertendo minha lista 'lista' para json. A palavra indent serve para ele converter com identação, ao inves de ser tudo reto



with open('abc.json','w+') as file: #Criando e abrindo um arquivo do tipo json chamado abc e dentro dele estamos escrevendo o conteudo de nosso d1_json
    file.write(d1_json)

#Essa aula continua no arquivo ler_json90