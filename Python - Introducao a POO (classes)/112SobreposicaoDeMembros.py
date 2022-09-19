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

    def falar(self):
        print('Estou em cliente')

class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeclasse} estudando')



class ClienteVip(Cliente): #Estamos criando uma cadeia de herança pois, ClienteVip herda de Cliente, que herda de pessoa

    # Quando chamamos um metodo ou atributo, ele procura por ele em sua classe original, neste caso, ClienteVip.
    # Caso ele não encontre o metodo em sua classe orginal, ele vai procurar na classe que ele herda, neste caso, na classe CLiente.
    # Se não achar na Classe Cliente, ele vai na classe pai da classe Cliente, enfim, vai intercalando até achar esse metodo.


    def falar(self):
        super().falar()  # Neste caso, temos o metodo falar na classe da chamada da instancia. Com a palavra super com o nome do metodo
        # estou dizendo que, quando o metodo falar for chamado numa instancia de ClienteVip, ele deve ler o metodo 'falar' primeiro da classe
        # que ele herda, neste caso, na classe CLiente. Se não achar na Classe Cliente, ele vai na classe pai da classe Cliente.
        # Quando encontrar o metodo, ele vai executar e depois executar de novo na classe da instancia
        Pessoa.falar(self)  # continuando a explicação acima, se eu quiser ser especifico em relação a qual metodo deve ser lido primeiro
        # basta fazer dessa forma.
        print('Falando outra coisa')



class ClienteVip2(Cliente): #Digamos que queiramos acrescentar novos atributos aos atributos que já hedamos da classe pai.
    #Neste caso, vamos pegar os atributos nome e idade herdados de Cliente, e adicionar em ClienteVip2 o atributo sobrenome

    def __init__(self, nome, idade, sobrenome): #Este construtor é do clienteVip2, nome e idade são herdados de Cliente.

        Pessoa.__init__(self, nome, idade) #Ao gerar um novo atributo dentro de uma classe filho aos atributos
        #herdados da classe pai, dentro da classe filho precisamos iniciar o construtor da classe pai

        self.sobrenome = sobrenome #Os dois primeiros atributos nome e idade serão herdados de Cliente, por isso não
        #precisa seta-los

    def falar(self):
        Pessoa.falar(self) #Conforme explicado acima em ClienteVip para estes este exemplo. Ele vai executar o metodo falar Pessoa
        Cliente.falar(self) #Aqui vai executar o metodo falar de Cliente
        print(f'{self.nome} {self.sobrenome}') #Foi fim vai executar o metodo falar dentro de ClienteVip2


c1 = Cliente('Davidson', 85)
print(c1.nome, c1.idade)
c1.falar()
c1.comprar()

c2 = ClienteVip('Rose', 99)
c2.falar() #Quando chamamos um metodo ou atributo, ele procura por ele em sua classe original, neste caso, ClienteVip.
#Caso ele não encontre o metodo em sua classe orginal, ele vai procurar na classe que ele herda, neste caso, na classe CLiente.
#Se não achar na Classe Cliente, ele vai na classe pai da classe Cliente, enfim, vai intercalando até achar esse metodo.


a1 = Aluno('Crosdineia', 287)
print(a1.nome, a1.idade)
a1.falar()
a1.estudar()

print()
print('--------------------')
print()

cv2 = ClienteVip2('Maria',22, 'Lima')
cv2.falar()