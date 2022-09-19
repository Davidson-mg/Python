"""
O que são dataclasses? O módulo Dataclasses fornece um decorador e funções para criar automaticamente métodos,
como __init__(), __repr__(), __eq__ (etc) em classes definidas pelo usuário.
Basicamente, dataclasses são syntax sugar para criar classes normais.
foi originalmente descrito na PEP 557.
Adicionado na versão 3.7 do Python.

"""

from dataclasses import dataclass

@dataclass
class Pessoa: #Ao importar o dataclass, passo a poder criar atributos de classes sem o __init__ por exemplo. Fica mais parecido com java

    nome: str
    sobrenome: str

    def nome_completo(self): # E nada impede de criarmos metodos da mesma forma que criavamos antes do o __init__, podendo
        #inclusive continuarmos a usar a palavra self
        return f'{self.nome} {self.sobrenome}'

p1 = Pessoa('Davidson', 'Marcos')
print(p1.sobrenome)
print(p1.nome_completo())


print()
print('------------------------------------')
print()

@dataclass (order=True)
class Pessoa2: #Ao importar o dataclass, passo a poder criar atributos de classes sem o __init__ por exemplo. Fica mais parecido com java

    nome: str
    sobrenome: str

    def __post_init__(self): #Caso eu precise utilizar o init, basta usar o __post_init__
        self.nome_completo = f'{self.nome} {self.sobrenome}'

    # def nome_completo(self): # E nada impede de criarmos metodos da mesma forma que criavamos antes do o __init__, podendo
    #     #inclusive continuarmos a usar a palavra self
    #     return f'{self.nome} {self.sobrenome}'



p2 = Pessoa2('A', 'Marcos')
print(p2.sobrenome)
print(p2.nome_completo)

p22 = Pessoa2('B', 'Maria')

print(p2 == p22) #conforme dito na descrição de dataclasses acima, um dos metodos que já incluso para vc, é o __eq__
#por isso, essa comparação sem a necessidade de criar um novo metodo especifico dentro da classe



p23 = Pessoa2('C', 'José')

p24 = Pessoa2('D', 'Claudia')

pessoas = [p2, p22, p23, p24]
print(sorted(pessoas)) #Essa ordenação só é possivel pq habilitamos acima em '@dataclass (order=True)'  o metodo
# order que já vem na metaclasse, só quê, por padrão ele vem desabilitado

print(sorted(pessoas, key=lambda pessoa: pessoa.sobrenome)) #usando uma expressão lambda para order por sobrenome
print(sorted(pessoas, key=lambda pessoa: pessoa.sobrenome, reverse=True)) #usando uma expressão lambda para order por
# sobrenome mas ao contrario


#Se eu quiser desativer alguns desses metodos automaticos de dataclasse, bastaria colocar nessa forma abaixo

# @dataclass (eq=False, repr=False): Estou desativando os metodos eq e repr
