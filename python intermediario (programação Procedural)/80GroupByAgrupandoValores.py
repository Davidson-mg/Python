alunos = [ #Criando uma lista alunos com dicionarios

    {'Nome':'Davidson', 'Nota': 'A'}, #dicionario
    {'Nome':'Josefina', 'Nota': 'B'},
    {'Nome':'Geraldina', 'Nota': 'A'},
    {'Nome':'Cludino', 'Nota': 'F'},
    {'Nome':'Maurino', 'Nota': 'D'},
    {'Nome':'Craconeia', 'Nota': 'A'},
    {'Nome':'Cracrocuda', 'Nota': 'B'},
    {'Nome':'Craginaldelina', 'Nota': 'D'},

]

from itertools import groupby

#OBS IMPORTANTE: groupby precisa que minha lista/dicionario esteja ordenada. Digamos que eu queira agrupar pela nota, os dicionarios precisam estar ordenados pela nota

#O nosso obj abaixo será agrupar os alunos pelas notas

alunos.sort(key=lambda item: item['Nota']) # a função sort() teria o obj de ordernar minha lista. Usando uma expressão lambda para dizer que deve ser ordanado por nota.
#Sem a expressão lambda, por padrão sort() ordenaria pela primeira posição 0

# print(alunos) eu poderia imprimir direto, mas ficaria os alunos um do lado do outro. Por isso vamos usar o for abaixo
# for a in alunos: #Imprimindo apenas para mostrar que os valores estão ordenados
#     print(a)

alunosAgrupados = groupby(alunos, lambda item: item['Nota']) #Uma vez ordenados, basta agrupar com o groupby. Assim como sort, precisamos usar uma lambda
# para dizer que deve ser ordanado por nota. Sem a expressão lambda, por padrão groupby() ordenaria pela primeira posição 0

#Como eu usei a mesma expressão duas vezes, em sort e groupby, para não ficar repetindo codigo, eu poderia salvar essa expressão numa variavel e chamar a variavel conforme a necessidade
#dentro do parentese de sort e groupby
#Ficaria assim, mas eu optei por não fazer pra ficar bem claro
#ordena = lambda item: item['Nota']
#alunosAgrupados = groupby (ordena)

# print(alunosAgrupados) #eu poderia imprimir direto, mas ficaria os alunos um do lado do outro. Por isso vamos usar o for abaixo

# for agrupados in alunosAgrupados:
#     print(agrupados)

#vai imprimir assim:
# ('A', <itertools._grouper object at 0x01372FD0>) # dentro de 'A' vai ter todos alunos agrupados dentro de um ojb, e assim por diante
# ('B', <itertools._grouper object at 0x01372FE8>)
# ('D', <itertools._grouper object at 0x01372FD0>)
# ('F', <itertools._grouper object at 0x01372FE8>) #Para imprimir os grupos com os alunos dentro, considere o exemplo abaixo

for agrupamento, valores_agrupados in alunosAgrupados:
    print(f'agrupamento: {agrupamento}')
    for alunos in valores_agrupados:
        print(alunos)
    print()

#Vai imprimir assim
# agrupamento: A
# {'Nome': 'Davidson', 'Nota': 'A'}
# {'Nome': 'Geraldina', 'Nota': 'A'}
# {'Nome': 'Craconeia', 'Nota': 'A'}
#
# agrupamento: B
# {'Nome': 'Josefina', 'Nota': 'B'}
# {'Nome': 'Cracrocuda', 'Nota': 'B'}
#
# agrupamento: D
# {'Nome': 'Maurino', 'Nota': 'D'}
# {'Nome': 'Craginaldelina', 'Nota': 'D'}
#
# agrupamento: F
# {'Nome': 'Cludino', 'Nota': 'F'}

print()
print('-------------------------------------------------------------')
print()

#Este exemplo é igual o de cima, só mudei no final a forma de imprimir. Tive que copiar tudo por conta do iterador que atingiu o limite

alunos = [ #Criando uma lista alunos com dicionarios

    {'Nome':'Davidson', 'Nota': 'A'}, #dicionario
    {'Nome':'Josefina', 'Nota': 'B'},
    {'Nome':'Geraldina', 'Nota': 'A'},
    {'Nome':'Cludino', 'Nota': 'F'},
    {'Nome':'Maurino', 'Nota': 'D'},
    {'Nome':'Craconeia', 'Nota': 'A'},
    {'Nome':'Cracrocuda', 'Nota': 'B'},
    {'Nome':'Craginaldelina', 'Nota': 'D'},

]

from itertools import groupby


alunos.sort(key=lambda item: item['Nota']) # a função sort() teria o obj de ordernar minha lista. Usando uma expressão lambda para dizer que deve ser ordanado por nota.
#Sem a expressão lambda, por padrão sort() ordenaria pela primeira posição 0


alunosAgrupados = groupby(alunos, lambda item: item['Nota']) #Uma vez ordenados, basta agrupar com o groupby. Assim como sort, precisamos usar uma lambda
# para dizer que deve ser ordanado por nota. Sem a expressão lambda, por padrão groupby() ordenaria pela primeira posição 0


for agrupamento, valores_agrupados in alunosAgrupados:
    print(f'agrupamento: {agrupamento}')
    quantidade = len(list(valores_agrupados))
    print(f'{quantidade} alunos tiraram a nota {agrupamento}')