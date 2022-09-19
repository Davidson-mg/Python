#Este arquivo é continuação do arquivo 90CriandoLendoEscrevendoApagandoArquivos

import json #Para ler ou modificar um arquivo json é necessario este import

with open('abc.json', 'r') as file: #abrindo o arquivo abc.json conforme explicado na aula 90CriandoLendoEscrevendoApagandoArquivos
    #Com o 'r' estamos dizendo que queremos apenas leitura
    d1_json = file.read() #É necessario um varial que vai receber o json do arquivo abc.json e em serguida ler com o comando read
    d1_json = json.loads(d1_json) #Transformando meu json do arquivo abc.jsom em dicionario

for k, v in d1_json.items(): #Dando um print no meu dicionario
    print(k)
    for k1, v1 in v.items():
        print(k1, v1)