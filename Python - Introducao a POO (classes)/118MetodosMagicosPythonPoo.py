"""

https://rszalski.github.io/magicmethods/

"""


class A:

    def __new__(cls, *args, **kwargs): #A descrição do metodo abaixo vale para este também
        if not hasattr(cls, '_jaexiste'): #Se não existe o '_jaexiste', cria o '_jaexiste'
            cls._jaexiste = object.__new__(cls)

        return cls._jaexiste

    def __init__(self): #Este metodo é executado sempre automaticamente quando instanciamos o obj.
        #Geralmente usamos eles para inicilizar o atributos de instancia. Por isso chamamos ele de construtor
        #embora ele não seja. Ele funciona tipo o new do java. Outro metodo magico que faz isso é o metodo new acima
        print('Eu sou o INIT')


a = A()
b = A()
c = A()

print(a==b)

print()
print('-----------------------------')
print()

class A2 :
    def __init__(self):
        print('Eu sou o Init')

    def __call__(self, *args, **kwargs): #Por causa dete metodo passa a ser possivel chamarmos a Classe como se fosse uma função
        #E passando argumentos e argumentos nomeados. Esse call só entra em cena quando chamo a instancia com parentese

        resultado = 1

        for i in args:
            resultado *= i
            return resultado

a2 = A2()
variavel = a2(1,2) #Só é possivel por conta do metodo 'def __call__' dentro da classe
print(variavel)

print()
print('-------------------------------------------')
print()
