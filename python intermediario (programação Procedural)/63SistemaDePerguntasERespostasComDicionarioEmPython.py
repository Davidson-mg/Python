perguntas = {
#        pk     :                                              pv
#                             pv["Pergunta"]                 pv["Respostas"]                               pv["respostaCerta"]
#                                                                rk:rv    rk:rv     rk:rv    rk:rv
    'pergunta 1': { 'Pergunta':'Quanto é 2 + 2?' , 'Respostas':{'a':'1', 'b':'10', 'c':'4', 'd':'5.3',} , 'respostaCerta':'c', },




    'pergunta 2': {'Pergunta': 'Quem descobriu o Brasil?','Respostas': {'a': 'Pedro A. Cabral', 'b': 'Moises', 'c': 'Donald Trump', 'd': 'kuririm',},'respostaCerta': 'd',},





    'pergunta 3': {'Pergunta': 'Qual é o maior time de futebou de Minas Gerais','Respostas': {'a': 'Cruzeiro', 'b': 'Fanfarrões Futebol Clube', 'c': 'America', 'd': 'Atletico-MG',},'respostaCerta': 'b',},

}

# for i,j in perguntas.items():
#
#     print(f'Qual a resposta da {i}')
#     for l, m in j.items():
#         resposta = ''
#
#         print(f'\t{l} : {m}')
#         if l == 'Respostas':
#             resposta = input('Informe a resposta: ')

respostas_certas = 0
for pk, pv in perguntas.items(): #Lembrando que se eu coloco apenas uma variavel no for, Ele vai automaticamente entender que essa variavel engloba tudo, tanto chave quato valores, mostrando tudo como tupla.
    #Como eu defini duas variaveis nesse for, ele vai entender automaticamente que essas duas variaveis correspondem a dois indices do dicionario 'perguntas.'
    # pk corresponde a: 'pergunta 1'
    # pv corresponde a: '{ 'Pergunta':'Quanto é 2 + 2?' , 'Respostas':{'a':'1', 'b':'10', 'c':'4', 'd':'5.3',} , 'respostaCerta':'c', }'

    print(f'{pk} : {pv["Pergunta"]}') #como pv corresponde a tudo que está entre {}, estou selecionado neste caso o valor contido no indice (chave) que possui o nome de 'Respostas'.
    #Este primeiro print vai mostrar: 'pergunta 1 : Quanto é 2 + 2?'

    print('Respostas: ')

    for rk, rv in pv["Respostas"].items(): #dentro de pv["Respostas"] temos: {'a': 'Pedro A. Cabral', 'b': 'Moises', 'c': 'Donald Trump', 'd': 'kuririm',}
        print(f'{rk} - {rv}') #rk vai mostrar os nomes dos indicies/chaves e rv vai mostrar os valores das chaves
        #Vai imprimir assim: a - 1

    resposta = input('Qual a sua resposta? ')
    if(resposta == pv["respostaCerta"]):
        print(f'A resposta certa é ... : letra - {pv["respostaCerta"]}. Parabens, você acertou :)! ')
        respostas_certas += 1
        print()
    else:
        print(f'A resposta certa é ... : letra - {pv["respostaCerta"]}. Que pena, você errou :(! ')
        print()

qtd_perguntas = len(perguntas)
procentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Você acertou {procentagem_acerto}% das perguntas')














