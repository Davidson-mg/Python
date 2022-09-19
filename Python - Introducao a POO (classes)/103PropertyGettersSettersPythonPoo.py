class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    @classmethod
    def desconto (self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))


    #Getters e setters

    #São meio que uma proteção, um filtro, então, sempre que solicitar uma das variaveis dentro da classe, vai passar por
    #estas funções.
    #Por exemplo: Quando o usario solicitar o preco, seja diretamente na instancia da classe
    #ou pela pela classe de metodo desconto acima, ele vai receber por meio do Getter, e quando for excrever, passará pelo setter

    #Getter
    @property
    def preco(self):
        return self._preco

    #setter
    @preco.setter
    def preco (self, valor):
        if isinstance(valor, str): #Estamos verificando se o valor que queremos escrever é uma string
            valor = float(valor.replace ('R$', '')) #Se for string, vai fazer o casting para float ao mesmo tempo que remove 'R$'
        self._preco = valor

    @property
    def nome(self):
        return self.nome

    @nome.setter
    def nome (self, valor):
        self._nome = valor.lower()



p1 = Produto('Camiseta', 50)
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = Produto('Caneca', 'R$15')
p2.desconto(10)
print(p1.nome, p1.preco)