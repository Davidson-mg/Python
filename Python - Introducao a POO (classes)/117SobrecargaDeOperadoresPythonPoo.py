"""

No python, o comportamento dos operadores é definido por metodos especiais.
Vamos alterar o comportamento de operadores com classes definidas pelo usuario

"""

class Retangulo:
    def __init__(self,x, y):
        self.x = x
        self.y = y


    def get_area(self): #metodo comum que retorna a area de um retangulo
        return self.x * self.y


    #Abaixo vamos usar alguns exemplos de metodos especiais do python

    # chamamos isso de metodo especial do pyhton
    def __repr__(self): #Sem esse metodo retornaria '<__main__.Retangulo object at 0x0117C100>'
        return f"<class 'Retangulo({self.x}, {self.y})'>" #sempre que for solicitado eu der um print x e y ele vai retornar conforme a string

    # Com o metodo abaixo, estou dizendo ao python o que fazer quando for solicitado a soma de duas instancias do obj.

    #chamamos isso de metodo especial do pyhton
    #metodo especial que soma dois objs
    def __add__(self, other): #o primeiro elemento entre parentese representa a instancia em si e o other é qualquer outro obj
        novo_x = self.x + other.x #Estou declarando uma nova variavel (novo_x) que vai receber a soma
        novo_y = self.y + other.y
        return Retangulo(novo_x, novo_y) #podemos dizer que estamos criando um novo obj dentro desssa classe


    def __lt__(self, other): #Metodo especial que vai verificar se um obj é maior que o outro
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 < a2:
            return True
        else:
            return False

    def __gt__(self, other): #Metodo especial que vai verificar se um obj é menor que o outro
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 < a2:
            return True
        else:
            return False

    def __eq__(self, other): #Metodo especial que vai verificar se um obj é igual ao outro
        if self.x == other.x and self.y == other.y:
            return "São iguais"
        else:
            return 'São diferentes'


r1 = Retangulo(10, 20)
r2 = Retangulo(10, 20)
print(r1 + r2) #Daria erro sem o metodo 'def __repr__(self):' que nós criamos acima, pois o python
# 'não sabe' como fazer esse calculo, pois não seria o calculos de dois numeros, mas sim de dois objs
# . Lembrando que por conta do metodo def __add__(self, other) na classe Retangulo, sempre que fizer
# soma de duas variaveis, não vai somar tipo 2+2 é 4 pois nós informamos ao python que soma Retangulo é soma de retangulos no
#metodo def __add__(self, other):


print(r1 > r2)