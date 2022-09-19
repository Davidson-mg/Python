arq = open('abc.txt', 'w') #Criando um arquivo txt de escrita 'w'
arq.write('Alguma coisa')
arq.close() #Quando abrimos e terminamos com um arquivo precisamos fecha-lo para não dar problemas futuros

with open('abc.txt', 'w') as arq: #Outra forma de abrir um arquivo. Melhor que da forma acima pois não preciso fechar depois de usar
    arq.write('Alguma coisa')

#O with acima pode ser usado para outras coisas, tipo abrir uma conexão de rede, uma base de dados e etc


print()
print('-----------------------------')
print()

class Arquivo: #Aqui estamos criando nosso proprio gerenciador de contexto
    def __init__(self, arquivo, modo): #o 'contrutor' que vai receber o arquivo e o modo de leitura
        print('Init')
        self.arquivo = open(arquivo, modo) #abrindo o arquivo. Até só abrimos o arquivo

    def __enter__(self): #Neste metodo estamos dizendo o que vai ser retornado na variavel arquivo quando passarmos
        #como parametro na instancia do obj
        print('Entou na classe')
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb): #depois de abrir e escrever e usar, este metodo fecha o arquivo
        #Os parametros exc_type, exc_val, exc_tb são padroes desse metodo e só entram em ação em caso de exceção
        #exc_type: tipo da exceção
        #exc_val: valor da exceção
        #exc_val: traceback (sei lá como escreve) da exceção

        print('Saiu da classe')
        self.arquivo.close()

with Arquivo('abc2.txt', 'w') as arquivo:
    arquivo.write('Alguma coisa')


print('-----------------------------------------------')

from contextlib import contextmanager

@contextmanager #Outra maneira de abrir, usar e fechar um arquivo de forma mais simples. Usando uma função comum mesmo
def abrir(arqui, modo):
    try:
        print('Abrindo arquivo')
        arqui = open(arqui, modo)
        yield arqui

    finally:
        print('Fechando arquivo')
        arqui.close()



with abrir('abcd.txt', 'w') as arqui: #Para eu chamar a função acima, mesmo que seja uma função comum, somos obrigados
    #a usar o with
    arqui.write('linha 1\n')
    arqui.write('linha 2\n')
    arqui.write('linha 2\n')