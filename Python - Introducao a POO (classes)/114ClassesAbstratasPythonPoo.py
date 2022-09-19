# # A PASTA CLASSE114 E OS ARQUIVOS DENTRO DELA conta114, ContaPoupanca FAZEM PARTE DESTA AULA. ABRA-OS PARA PODER ACOMPANHAR
#
#
# from abc import ABC, abstractmethod  # Para criar classes abstratas é necessario este import
#
#
# class A(ABC):  # ABC significa abstract basic  class. Toda classe abstrata precisa herdar de ABC
#
#     @abstractmethod
#     def falar(
#             self):  # Toda classe abstrata precisa ter pelo menos um metodo abstrado e, esse metodo dentro da classe abstrata
#         # não precisa fazer nada, mas precisa existir, como é o caso aqui
#         pass
#
#
# class B(A):  # Toda classe normal que herda de uma classe abstrata, precisa ter todas os metodos da classe abstrata
#     def falar(self):
#         print('Falando... B...')
#     # Se eu tentasse executar essa classe sem o metodo falar que existe na classe abastrar, daria erro.
#
#
# a = B()
# a.falar()
#
# # a = A() #Vai da erro pois vc não pode utilizar os metodos abstratos direto pela classe abstrata
#
#
# print()
# print(
#     '------------------------------------------------------------------------------------------------------------------------')
# print()


from classes114.contaPoupanca import ContaPoupanca
from classes114.contaCorrente import ContaCorrente


cp = ContaPoupanca(1111, 2222, 0)
cp.depositar(10)
cp.sacar(5)
cp.sacar(5)
cp.sacar(1)

print()
print('-----------------------')
print()

cc = ContaCorrente(159,268,000)
