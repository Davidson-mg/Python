#ESTE ARQUIVO FAZ PARTE DA AULA 113HerancaMultiplaPythonPoo
#Os arquivos eletronico113 e smartphone113 também fazem parte da aula 113HerancaMultiplaPythonPoo

#Vamos criar um metodo ficticio de log. Vale lembrar que o python já possui metodos especificos pra isso
class LogMixin: #Essa classe não está relacionada com as classes smartphone ou eletronico, porém
    #nós vamos utiliza-la em outras classes para implementar as funcionalidades abaixo. Por isso
    #demos o nome de logMixin

    @staticmethod
    def write(msg): #Esse metodo terá a função de abrir um arquivo e escrever nele
        with open('log.log', 'a+') as f: #Com 'with open' estamos abrindo um novo arquivo. Dentro de parentese estou
            #dizendo o nome e o tipo do arquivo (log.log) e o modo de abertura (quero que sempre adicione linhas ao
            # final do arquivo) e o 'as f' é como vou me referir ao arquivo dentro do python, semelhante ao 'as' de SQL
            f.write(msg) #Estou dizendo que vai escrever a msg que vem como parametro
            f.write('\n') #Precisa colocar sempre o \n pra ele não escrever tudo na mesma linha

            #Repare que acima não usamos a palavra self, indicando que ele pode ser static e não precisa da instancia

    #Daqui para baixo precisamos da instancia, poir isso usamos o self
    def logInfo(self, msg):
        self.write(f'Info: {msg}')

    def logError(self, msg):
        self.write(f'Error: {msg}')