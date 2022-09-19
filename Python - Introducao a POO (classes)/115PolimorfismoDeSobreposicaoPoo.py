"""

Polimorfimos é o principio que permite que classes derivdas de uma mesma superclasse tenham metodos iguais (
da mesma assinatura) mas comportamento diferentes.
Mesma assinatura =Mesma quantidade e tipo de parametros

"""

from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def fala(self, msg):
        pass

class B(A):
    def fala (self, msg):
        print(f'B Está falando {msg}')

class C(A):
    def fala(self, msg):
        print(f'C est[a falando {msg}')


b = B()
c = C()
b.fala('Um assunto')
c.fala('Outro Assunto')