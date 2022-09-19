class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__ #Com esse atributo vou saber de qual classe filha vem o obj

    def falar(self):
        print(f'{self.nomeclasse} Falando')

class Cliente(Pessoa): #Ao colocar Pessoa entre parentese, estou dizendo que minha classe Cliente herda de Pessoa
    def comprar(self):
        print(f'{self.nomeclasse} comprando') #Os metodos dentro das classes filhas, vão pertencer somente as classes filhas


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeclasse} estudando')


c1 = Cliente('Davidson', 85)
print(c1.nome, c1.idade)
c1.falar()
c1.comprar()


a1 = Aluno('Crosdineia', 287)
print(a1.nome, a1.idade)
a1.falar()
a1.estudar()
