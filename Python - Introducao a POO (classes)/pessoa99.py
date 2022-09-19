#Este arquivo pertence a aula 99ClassesPyhtonPoo

from datetime import datetime


class Pessoa:

    anoAtual = int(datetime.strftime(datetime.now(), '%Y'))

    # def falar(self): #Toda função atrelada a uma classe, é um metodo. Esse self está relacionado a isntancia do obj
    #     print('Pessoa está falando')

    def __init__(self, nome, idade, comendo=False, falando=False): #metodo
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

        variavel='olá'
        print(variavel) #Essa variavel só pode ser acessada dentro desta função

    def outro_metodo(self): #metodo
        print(self.nome) #conseguimos acessar todas as variaveis com selft do metodo init dentro de outros metodos.

        #print(variavel) #Porém, se tentamos acessar um variavel comum de outro metodo, da erro. Por isso essa linhas está comentada

    def comer (self, alimento): #Quando chamarmos este metodo, ele vai print a msg abaixo e alterar variavel comendo para true
        if self.comendo: #Caso já tenha chamado a função comer uma vez, a variavel comendo vai ser True. Então, estou verificando
            #se comendo é verdadeiro. Se sim, retorna a msg a baixo e sair da função pelo return
            print(f'{self.nome} já está comendo')
            return

        if self.falando:
            print(f'{self.nome} não pode comer falando')

        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True



    def paraComer (self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return

        print(f'{self.nome} parou de comer')
        self.comendo = False

    def falar(self, msg):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo')
            return

        if self.falando:
            print(f'{self.nome} já está falando')
            return

        print(f'{self.nome} começou a falar sobre {msg}')
        self.falando = True

    def pararFalar(self):
        if not self.falando:
            print(f'{self.falando} não está falando')
            return
        print(f'{self.nome} parou de falar')
        self.falando = False

    def pegarAnoNascimento(self):
        return self.anoAtual - self.idade