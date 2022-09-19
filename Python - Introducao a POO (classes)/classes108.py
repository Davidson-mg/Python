#Este arquivo faz parte da aula 108AssociacaoPythonPoo

class Escritor:
    def __init__(self, nome): #Construtor que possui apenas um atributo nome
        self.__nome = nome #Lembrando que atributo que começam com __, são privados, não podem ser acessados fora da classe
        #caso eu precise acessar fora da classe, é necessario metodo getter abaixo
        self.__ferramenta = None #O objetiv deste atributo será receber qualquer coisa

    @property #metodo getter que vai possibilitar acessarmos o atributo __nome fora da classe
    def nome(self):
        return self.__nome

    @property #metodo getter para pegar o valor do atributo ferramenta
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter #metodo setter para escrever no atributo ferramenta o que vem como parametro de fora da classe
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta #Vai escrever dentro do atributo privado __ferramenta, o que está no parametro ferramenta
        #que vem de fora da classe





class Caneta: #Criando uma classe caneta
    def __init__(self, marca): #Construtor que possui apenas um atributo marca
        self.__marca = marca

    @property #metodo getter que vai possibilitar acessarmos o atributo __marca fora da classe
    def marca (self):
        return self.__marca

    def escrever(self):
        print('A Caneta está escrevendo...')


class MaquinaDeEscrever:
    def escrever(self):
        print('A maquina está escrevendo...')
