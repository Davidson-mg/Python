# FAZ PARTE DESTA AULA O ARQUIVO classes109. Abra ele para encontrar os restante da aula

from classes109 import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()
print(carrinho)

print()
print('------------------')
print()

p1 = Produto('Camisa', 50) #Ao adicionar um produto, estou instanciando a classe Produto. Ainda não estou adicionando nada dentro CarrinhoDeCompras
p2 = Produto('Caneca', 10)
p3 = Produto('boné', 25)

carrinho.inserirProduto(p1) #Agora, estou inserindo o produto que instenciei na classe produto acima, dentro da minha classe CarrinhoDeCompras por meio do metodo inserirProduto
carrinho.inserirProduto(p2)
carrinho.inserirProduto(p3)
carrinho.inserirProduto(p1) #Posso adicionar novamente o mesmo produto em p1 que será considerado um novo produto, mesmo que igual

carrinho.listarProduto()

print()
print('------------------')
print()

print(carrinho.somaTotal())