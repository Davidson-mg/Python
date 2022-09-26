
#OS ARQUIVOS eletronico113, smartphone113 e log113 fazem parte desta aula. Abra-os para pode acompanhar

class A:
    def falar(self):
        print('Falando... Estou em A')

class B:
    def falar(self):
        print('Falando... Estou em B')

class C(A): #herda tudo da classe A
    def falar(self): #Se eu instancio A, mesmo que metodo falar tb exista no metodo A, neste caso o metodo
        #falar da classe C vai sobreescrever o metodo falar da classe A
        print('Falando... Estou em C')


class D(B, C): #herda tudo das classes B e C. Neste caso, considerando que vc tenha dois metodos ou atributos
    #iguais nas classes B e C, o Python vai considerar da esquerda para direita (B depois C). Se ele achar o metodo ou atributo
    #em B, ele não vai procurar em C. Só vai procurar em C caso não tenha encontrado primeiro em B
    pass



d = D()
d.falar() #Vai imprimir: 'Falando... Estou em B'
c = C()
c.falar()

print()
print('---------------------------------------------')
print()

from smartphone113 import Smartphone

smartphone = Smartphone('Pocophone F1')
smartphone.conectar()
smartphone.desligar()
smartphone.ligar()
smartphone.conectar()
smartphone.conectar()
smartphone.conectar()
smartphone.desligar()
smartphone.conectar()
smartphone.desconectar()

