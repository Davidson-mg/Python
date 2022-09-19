from string import Template
from datetime import datetime


#No exemplo abaixo nós modificamos palavras em um arquivo HTML
with open ('template.html', 'r') as html:  #vamos abrir um novo arquivo com o nome de 'template.html'. 'w' é para leitura
    #e escrita. Este arquivo template.html está dentro da propria pasta deste arquivo da aula 140
    template = Template(html.read()) #Vamos usar o Templete para ler e receber o arquivo html
    dataAtual = datetime.now().strftime('%d/%m/%Y') #armazenando a data atual
    corpoMsg = template.safe_substitute(nome='Davidson Marcos', data=dataAtual) #usando o metodo safe_substitute
    #para escrever as variaveis nome e data nos locais onde tiver $nome e $data no arquivo html

print(corpoMsg) #vai imprimir o conteudo do arquivo html