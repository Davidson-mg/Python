
# JSON   >>    PYTHON
# object       dict
# array        list
# string       str
# number(int)  int
# number(real) float
# true         True
# false        False
# null         None


# PYTHON                                          JASON
# dict                                            object
# list tuple                                      array
# str                                             string
# int, float, int- & float-derived Enums          number
# True                                            true
# False                                           false
# None                                            null


from dados137.dados import *
from dados137 import *
import json

lista = [1,2,3,4,5,6]
dadosJson = json.dumps(lista) #convertendo minha lista para Json
print(dadosJson) #Vai imprimir: [1, 2, 3, 4, 5, 6], porém, mesmo parecendo lista, se trata de uma string
print(type(dadosJson))# Vai imprimir <class 'str'>

dadosJson = json.dumps(clientes_dicionario, indent=4) #Aqui estamos convertendo o dicionario do arquivo dados137 para json.
#ident de 4 espaços para que armazene de baixo pra cima e não tudo na mesma linha
print(dadosJson)#Repare que quando imprimir, se parece muito com uma dicionario do python, mas não é Json


dicionario = json.loads(clientes_json) #Agora estamos convertendo o arquivo json clientes em um dicionario python
for chave, valor in dicionario.items():
    print(chave)
    print(valor)

print()
print('----------------------------------------------------------------------------------------------')
print()

#Vamos converter um dicionario python salvando no arquivo .json
#Para mais detalhes sobre abrir, ler e escrever arquivos, procure o arquivo da aula 90
with open('clientes137.json', 'w') as arquivo: #'with' gerenciador de contexto. Ele fecha sozinho seu arquivo depois de executar tudo que têm dentro dele.
#ao acresncetar 'w+', estou dizendo que quero leitura e escrita
    json.dump(clientes_dicionario, arquivo, indent=4) #Aqui estamos convertendo meu dicionario do arquivo dados137 para json,
    #em seguida, em 'arquivo' entre parenteses, estamos escrevendo nosso dicionario
    #Não estamos printando nada pois está criando um arquivo e escrevedo nele.



with open('clientes137.json', 'r') as arquivo: #'with' gerenciador de contexto. Ele fecha sozinho seu arquivo depois de executar tudo que têm dentro dele.
#ao acresncetar 'r+', estou dizendo que quero apenas leitura. Estou criando uma variavel 'arquivo' que vai receber
#o conteudo do arquivo que estou abrindo 'clientes.csv'
    dados = json.load(arquivo) #Aqui estamos convertendo meu json do arquivo dados137 para dicionario e
    # armazenando na variavel dados,



for chaves, valores in dados(): #imprimindo meu dicionario convertido de json
    print(chaves)
    print(valores)



