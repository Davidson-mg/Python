


#Faz parte da aula deste arquivo, todos os arquivos importados da pasta classes 123. Para mais detalhes, precisa abri-los

"""
Exercicio com abstração herança, encapsulamentto e polimorfismo

Cria um sistema bancario (extremamente simples) que tem clientes, contas e um banco.
A ideia é que o o cliente tenha uma conta (poupança ou corrente)  que possa sacar/depositar
nessa conta. Contas corrente tem um limite extra. Banco tem clientes e contas

conta corrente vc consegue sacar abaixo de zero e conta pupança não

Dicas:

Criar classe cliente que herda da classe pessoa (herança)
    Pessoa tem nome e idade (getters)

    Cliente tem conta (agragação da classe ContaCorrente ou ContaPoupança)


Criar classes contaPoupança e conta ContaCorrente que herdam de Conta

    ContaCorrente deve ter um limite extra

    Contas têm agencia, numero da conta e saldo

    Contas devem ter metodo deposito

    conta (super classe) deve ter o metodo sacar abstrato (Abstração e polimorfismo -
    as subclasses que implementar o metodo sacar)



Criar classe Banco para Agregar classes de clientes e de contas (agragação)
Banco será responsavel por autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clientes (agragação)
    * Checar se a agencia é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar a na autenticação do banco (descrito acima)

"""

from classes123.conta import Conta, ContaCorrente, ContaPoupanca
from classes123.cliente import Cliente
from classes123.banco import Banco

banco = Banco()

cliente1 = Cliente('Davidson', 85)
cliente2 = Cliente('Maria', 74)
cliente3 = Cliente('Gil', 41)

conta1 = ContaPoupanca(1111, 78954, 1500)
conta2 = ContaCorrente(1547, 75841, 0)
conta3 = ContaPoupanca(1234, 75984, 0)


cliente1.inserirConta(conta1)
cliente2.inserirConta(conta1)
cliente3.inserirConta(conta3)

banco.inserirCliente(cliente1)
banco.inserirConta(conta1)


print()
print('---------------------------------------------------------------------------')
print()


if banco.autenticar(cliente1):
    cliente1.conta.sacar(500)
else:
    print('Cliente não autenticado')






