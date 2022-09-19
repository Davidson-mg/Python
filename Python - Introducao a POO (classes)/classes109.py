#Este arquivo faz parte da aula 108AgregacaoPythonPoo


#Agragadação é o que está acontecend abaixo. Existe uma relação entre as classes CarrinhoDeCompras e produtos.
#Repare que não conseguirmos, listar, ou inserir produtos, ou somar o valor tatal de CarrinhoDeCompras sem depender de produtos
class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = [] #Essa classe vai ter somente este atributo, que é uma lista. O objetivo é que essa lista
        #receba varios objetos de produtos da classe produto. Ou seja, uma lista com obejtos, e objetos com nome e valor

    def inserirProduto (self, produto): #Este metodo vai receber como parametro um produto (obejto) e vai inseri-lo na minha lista
        self.produtos.append(produto) #Lembrando que cada objeto produto terá os atributos nome e valor

    def listarProduto(self): #Este metodo vai apanas imprimir os produtos
        for produto in self.produtos: #um for que que vai percorrer os atributos do meu objeto produtos
            print(produto.nome, produto.valor) #Lembrando que cada objeto produto terá os atributos nome e valor

    def somaTotal(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

