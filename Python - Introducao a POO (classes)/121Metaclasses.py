
"""
EM PYTHON TUDO É OBJ: incluindo classes
MetaClasses são as 'classes' que criam classes.
type é uma metaclsse (!!!???)
"""
class Meta(type): #Meta classe. O objetivo dela aqui será obrigar/avisar que, ao criar a classe B, ela deve possuir
    #um metodo chamado 'b_fala'. Este recurso seria mais aplicavel num ambiente de equipe, onde uma equipe fica
    #responsavel pela classe A e outra equipe fica responsavel pela classe B.

    def __new__(mcs, name, bases, namespace): #mcs: tipo metaclasse, name: nome da classe que vamos monitorar
        #bases: classe pai, no caso classe A, namespace: toda classe possui um namespace, se refere aos atributos e os
        #metodos de uma classe, enfim, o conteudo de uma classe

        if name == 'A': #Estou dizendo que não quero considerar o comportamento de A, logo,
            #devemos considerar apenas a classe B ou demais classes que herdam de A
            return type.__new__(mcs, name, bases, namespace)
        print(namespace)

        if 'b_fala' not in namespace: #caso não exista o metodo b_fala dentro das classes que herdam de A ...
            print(f'Oi, você precisa criar um metodo b_fala em {name}')
        else:
            if not callable(namespace['b_fala']): #Caso eu crie uma variavel chamada b_fala ao contrario de um metodo ...
                print(f'b_fala precisa ser um metodo, não atributo em {name}')

        return type.__new__(mcs, name, bases, namespace)


class A (metaclass=Meta):#Estou dizendo que toda classe que herdar de A, vai se comportar conforme instruido na
    # meta classe acima
    def fala(self):
        self.b_fala()



class B(A):
    pass
    # def b_fala(self):
    #     print('OI')

b = B()


print()
print('-------------------------------------------------------------------------------------')
print()

#No exemplo abaixo, nossa meta classe terá o objetivo de apagar um atributo na classe filho afim de impedir que este
#atributo seja sobrescrito

class Meta2(type): #Meta classe. O objetivo dela aqui será obrigar/avisar que, ao criar a classe B, ela deve possuir
    #um metodo chamado 'b_fala'. Este recurso seria mais aplicavel num ambiente de equipe, onde uma equipe fica
    #responsavel pela classe A e outra equipe fica responsavel pela classe B.

    def __new__(mcs, name, bases, namespace): #mcs: tipo metaclasse, name: nome da classe que vamos monitorar
        #bases: classe pai, no caso classe A, namespace: toda classe possui um namespace, se refere aos atributos e os
        #metodos de uma classe, enfim, o conteudo de uma classe

        if name == 'A2': #Estou dizendo que não quero considerar o comportamento de A, logo,
            #devemos considerar apenas a classe B ou demais classes que herdam de A
            return type.__new__(mcs, name, bases, namespace)

        if 'attr' in namespace: #Vai apagar o atributo attr sempre que ele for utilizado nas classes filhos de A
            #Fazendo com seja exibido somente o valor do atributo na classe pai
            print(f'{name} tentou sobrescrever o atributo attr')
            del namespace['attr']


        return type.__new__(mcs, name, bases, namespace)


class A2 (metaclass=Meta2):#Estou dizendo que toda classe que herdar de A, vai se comportar conforme instruido na
    # meta classe acima
    attr = 'Valor A'



class B2(A2):
    attr = 'Valor B'

class C3(A2):
    attr = 'Valor C'


b2 = B2()
c3 = C3()

print(b2.attr)
print(c3.attr)