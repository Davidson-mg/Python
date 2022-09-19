

from classes123.pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome, idade): #Não estou colocando o parametro conta entre parentese para que eu não seja obrigado
        #a informado quando eu instancia um cliente, pois essa variavel deve receber valor somente quando o metodo
        #inserirConta abaixo for utilizado
        super().__init__(nome, idade)
        self.conta = None

    def inserirConta(self, conta):
        self.conta = conta








