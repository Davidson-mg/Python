
#Na composição, uma classe pertence a outra classe. Neste caso, endereco pertence a cliente
#Quando a classe cliente é criada e cria uma classe endereço, quando a classe cliente é apagada, a classe endereço também é

class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def insereEndereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado)) #Ao contrario do metodo 'inserirProduto' da aula anterior '108AgregacaoPythonPoo' que também
        #possui o objetivo de inserir um obj, aqui estamos instanciando o obj diretamenteo no metodo que insere. A diferença na pratica é que,
        #metodo 'inserirProduto' da aula anterior '108AgregacaoPythonPoo', fora da classe a gente primeiro tinha que instanciar o produto na classe Produto,
        #ex: p1 = Produto('Camisa', 50), para só depois chamar o metodo inserirProduto para poder inserir o produto na classe de carrinho. ex: carrinho.inserirProduto(p1)
        #Já neste caso de insereEndereco, como Já instanciamos Endereco dentro de insereEndereco, fora da classe posso chamar apenas o metodo insereEndereco passando
        #os atributos como parametro. Ex: cliente1.insereEndereco('Betim', 'MG')

    def listaEnderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

    def __del__(self):
        print(f'{self.nome} FOI APAGADO')

class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f'{self.cidade}/{self.estado} FOI APAGADO')



cliente1 = Cliente('Davidson', 58)
cliente1.insereEndereco('Betim', 'MG')
print(cliente1.nome)
cliente1.listaEnderecos()
del cliente1
print()

cliente2 = Cliente('Maria', 66)
cliente2.insereEndereco('Salvador', 'BA')
cliente2.insereEndereco('Rio de Janeiro', 'RJ')
print(cliente2.nome)
cliente2.listaEnderecos()
del cliente2
print()

cliente3 = Cliente('João', 19)
cliente3.insereEndereco('São Paulo', 'SP')
print(cliente3.nome)
cliente3.listaEnderecos()
del cliente3
print()

print('--------------------------------------------------------------------')