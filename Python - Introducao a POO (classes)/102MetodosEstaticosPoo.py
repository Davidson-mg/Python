from random import randint

class Pessoa:

    anoAtual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def pegarAnoNascimento (self):
        print(self.anoAtual - self.idade)

    @classmethod #Esse tipo de classe retorna um valor para dentro da propria classe. Por isso chamamos de metodo de classe
    def PorAnoNascimento(cls, nome, anoNascimento): #Com base nesse metodo (função), vamos inserir uma pessoa na minha classe
        idade = cls.anoAtual - anoNascimento #Vale lembrar notar que estamos trocando self por cls (classe), fim de deixar explicito que é um metodo de classe
        #Uma variavel idade que subtrai o anual declarado no incio da classe por um ano passado como parametro
        return cls(nome, idade) #Vai retornar pra dentro da propria classe uma nova pessoa

    @staticmethod #Se trata de um metodo (função) comum, como as funções fora de uma classe, mas para padroniza, usamos a palavra @staticmethod
    def geraId(): #Por se tratar de uma função comum, não precisa do self nem cls
        rand = randint(1000, 19999)
        return rand

p1 = Pessoa.PorAnoNascimento('Davidson', 1237) #Agora eu consigo instanciar um obj pessoa por meio do metodo.
# Seria o mesmo que instanciar dessa forma: p1 = Pessoa('Davidson', 103)
print(p1)
print(p1.nome, p1.idade)
p1.pegarAnoNascimento()

print()
print('------------------------')
print()

print(Pessoa.geraId())
var = p1.geraId()
print(var)