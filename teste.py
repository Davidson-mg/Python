class Pessoa ():
    def __int__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Aluno(Pessoa):
    def __init__(self, nome, idade, nota):
        super().__int__(nome, idade)

        self.nota = nota

    def multiplica_nota(self, valor):
        return self.nota * valor




aluno = Aluno('Davidson', 22, 10)
print(aluno.nome, aluno.idade, aluno.nota)

print (aluno.multiplica_nota(2))