from pessoa99 import Pessoa #Importando do arquivo pessoa99 a classe Pessoa

# p1 = Pessoa()
# p2 = Pessoa()
#
# p1.nome = 'Davidson' #Instancia de um obj. Atribuindo uma variavel e seu valor a classe Pessoa no obj p1
# p2.nome = 'Marcos'
#
# print(p1.nome)
# print(p2.nome)
#
# p1.falar() #chamando o metodo falar da classe Pessoa

p1 = Pessoa('Davidson', 103) #Existem ainda os atributos comendo e falando, mas, como receberam valores padrões dentros da classe, não precisa eu passar aqui
p2 = Pessoa('Marcia', 2)

p1.comer('maçã') #Aqui vai retornar Davidson está comendo maçã
p1.paraComer()
p1.comer('Manga') #Aqui vai retornar Davidson já está comendo
p1.paraComer()

print()
print('--------------------')
print()

p1.comer('churros')
p1.falar('vida')
p1.paraComer()
p1.falar('vida')
p1.pararFalar()


print()
print('--------------------')
print()

p1.comer('Caju')
p2.comer('Arroz')

print()
print('--------------------')
print()

print(p1.anoAtual)
print(p2.anoAtual)
print(Pessoa.anoAtual)

print()
print('--------------------')
print()

print(p1.pegarAnoNascimento())
