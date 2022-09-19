"""O arquivo clientes.csv faz parte desta aula"""

import csv

#PRIMEIRO EXEMPLO

#Para mais detalhes sobre abrir, ler e escrever arquivos, procure o arquivo da aula 90
with open('clientes.csv', 'r') as arquivo: #'with' gerenciador de contexto. Ele fecha sozinho seu arquivo depois de executar tudo que têm dentro dele.
#ao acresncetar 'w+', estou dizendo que quero apenas leitura. Estou criando uma variavel 'arquivo' que vai receber
#o conteudo do arquivo que estou abrindo 'clientes.csv'

    dados = csv.DictReader(arquivo) #estou arqmazendo os arquivos que foram armazenados na variavel 'arquivo' do comando with open,
    #dentro de uma nova variavel 'dados'. NO DictReader no lugar de apenas 'reader' vai me dar a lista ordenada
    #EXEMPLO
    #Com DictReader:
    # {'Nome': 'Maria', 'Sobrenome': 'Figueiredo', 'E-mail': 'maria@email.com', 'Telefone': ' 55 21 98789-4875'}
    # {'Nome': 'JoÃ£o', 'Sobrenome': 'Miranda', 'E-mail': 'jm@mail.com', 'Telefone': ' 55 11 985787887'}
    #Sem o DictReader:
    # ['Davidsom', 'Marcos', 'davidson@email.com', ' 55 31 99578-7847']
    # ['Maria', 'Figueiredo', 'maria@email.com', ' 55 21 98789-4875']
    # ['JoÃ£o', 'Miranda', 'jm@mail.com', ' 55 11 985787887']

    #next(dados) #Vaz ele começa a partir da segunda linha, dessa forma não vai mostrar a linha que têm 'nome, email, telefone'.
    #Não funciona com 'DictReader', por isso está comentado

    for dado in dados:
        print(dado)

    print('----------------------------------')

    for dado in dados:
        print(dado['Nome'], dado['Sobrenome'], dado['E-mail'], dado['Telefone']) #imprimir dessa forma só é possivel
        #usando o DictReader acima. Retornando em forma de dicionario ordenado

print('----------------------------------')

# #for dado in dados: #Coloquei essa linha comentada pelo seguinte, o 'with open' fecha automaticamente os arquivos quando
#Acabamos de usar, por isso, se eu tento percorrer ele aqui fora, daria erro.
#     print(dados)

#Abaixo vamos refazer o exemplo acimade modo que dê pra usar


print()
print('------------------------------------------------------------------------------------------------')
print()


#SEGUNDO EXEMPLO

#Para mais detalhes sobre abrir, ler e escrever arquivos, procure o arquivo da aula 90
with open('clientes.csv', 'r') as arquivo: #'with' gerenciador de contexto. Ele fecha sozinho seu arquivo depois de executar tudo que têm dentro dele.
#ao acresncetar 'w+', estou dizendo que quero apenas leitura. Estou criando uma variavel 'arquivo' que vai receber
#o conteudo do arquivo que estou abrindo 'clientes.csv'

    dados = [x for x in csv.DictReader(arquivo)] #estou percorrendo meu arquivo csv e adicionando na variavel dados
    # uma a um, afim de que a variavel 'dados' seja uma lista com dicionarios. O DictReader no lugar de apenas 'reader'
    # vai me dar a lista ordenada
    #EXEMPLO
    #Com DictReader:
    # {'Nome': 'Maria', 'Sobrenome': 'Figueiredo', 'E-mail': 'maria@email.com', 'Telefone': ' 55 21 98789-4875'}
    # {'Nome': 'JoÃ£o', 'Sobrenome': 'Miranda', 'E-mail': 'jm@mail.com', 'Telefone': ' 55 11 985787887'}
    #Com o reader:
    # ['Davidsom', 'Marcos', 'davidson@email.com', ' 55 31 99578-7847']
    # ['Maria', 'Figueiredo', 'maria@email.com', ' 55 21 98789-4875']
    # ['JoÃ£o', 'Miranda', 'jm@mail.com', ' 55 11 985787887']

    #next(dados) #Vaz ele começa a partir da segunda linha, dessa forma não vai mostrar a linha que têm 'nome, email, telefone'


for dado in dados: #Coloquei essa linha comentada pelo seguinte, o 'with open' fecha automaticamente os arquivos quando
# Acabamos de usar, por isso, se eu tento percorrer ele aqui fora, daria erro. Abaixo
    print(dados)

#Acima nós armazenamos o conteudo do arquivo 'clientes.csv' na variavel dados no formato de lista
#Abaixo nós vamos escrever o que foi armazenado na variavel dados em um novo arquivo

#obs: vamos escrever apenas a primeira linha que é: 'nome,, sobrenome, email, telefone'



with open('clientes2.csv', 'w') as arquivo: #vamos abrir um novo arquivo com o nomee de 'clientes2.csv'. 'w' é para leitura
    #e escrita

    escreve = csv.writer(arquivo, delimiter=',',quotechar='"', quoting=csv.QUOTE_ALL)
    #delimiter: é o que separa as palavras
    #quotechar: o sergundo caracter é referente qual será usado para aspas, ai, dentro de '' colocamos ".
    #quoting: não obrigatorio. Queremos neste caso que os elementos estejam dentro de aspas



    chaves = dados[0].keys()
    chaves = list(chaves)
    escreve.writerow(  # usando o metodo writerow para escrever o conteudo abaixo
        [
            chaves[0],
            chaves[1],
            chaves[2],
            chaves[3]

        ]
    )

    for dado in dados: #Dentro de dados que possui o conteudo do arquivo gerado no primeiro with open neste segundo exemplo
        escreve.writerow( #usando o metodo writerow para escrever o conteudo abaixo
            [
                dado['Nome'],
                dado['Sobrenome'],
                dado['E-mail'],
                dado['Telefone']
            ]
        )
