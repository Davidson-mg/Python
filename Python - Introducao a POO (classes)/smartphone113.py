#ESTE ARQUIVO FAZ PARTE DA AULA 113HerancaMultiplaPythonPoo
#Os arquivos eletronico113 e log113 também fazem parte da aula 113HerancaMultiplaPythonPoo

from eletronico113 import Eletronico #fazendo um import da classe Eletronico do arquivo eletronico113
from log113 import LogMixin


class Smartphone(Eletronico, LogMixin): #Estamos aplicando herança multiplica com as classes Eletronico e LogMixin

    def __init__(self, nome):#Este construtor é da classe Smartphone, nome é herdado de Eletronico.
        super().__init__(nome)# precisamos iniciar o construtor da classe pai
        self._conectado = False

    def conectar(self):
        if not self._ligado: #ligado é um atribudo herdado de eletronico. Vai verificar se é False
            info = f'{self._nome} não está ligado' #nome também é um atribudo herdado de eletronico
            print(info)
            self.logError(info)
            return

        if self._conectado: #conectado também é um atribudo herdado de eletronico. Vai verificar se é True
            error = f'{self._nome} Já está conectado' #nome também é um atribudo herdado de eletronico
            print(error)
            self.logError(error)
            return

        info = f'{self._nome} está conectado'
        print(info)
        self.logInfo(info)
        self._conectado = True

    def desconectar(self):
        if not self._conectado: #conectado é um atribudo herdado de eletronico. Vai verificar se é False
            error = f'{self._nome} não está conectado' #nome também é um atribudo herdado de eletronico
            print(error)
            self.logError(error)
            return

        info = f'{self._nome} foi desligado com sucesso'
        print(info)
        self.logInfo(info)
        self._conectado = False