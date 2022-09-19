
#Exemplo normal
nome = input('Qual o seu nome: ')
if nome: #Lembrando que uma string vazia possui valor booleando 'false'. Se eu não digito nada quando pedir no input acima e apenas dou um enter, fica sendo uma variavel de string vazia
    print(nome)
else:
    print('Você não digitou nada')

print()

#Exemplo curto
nome = input('Qual o seu nome: ')
print(nome or 'Você não digitou nada') #Terá exatamente o mesmo efeito do exemplo acima


print()


a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'Davidson'

variavel = a or b or c or d or e or f or g #Neste caso, vai armazenar a primeira variavel que for verdadeiro
print(variavel) #vai imprimir 22