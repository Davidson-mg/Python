import random
import  string

interiro = random.randint(10, 20) #vai pegar um numero inteiro aleatrio entre e 20
print(interiro)

flutuante = random.uniform(10, 20) #vai pegar um numero flutuante aleatrio entre e 20
print(flutuante)

flutuante = random.random() #vai pegar um numero flutuante aleatrio entre 0 e 1
print(flutuante)

inteiro = random.randrange(900, 1000, 10) #vai pegar um numero aleatorio entre 900 e 1000 pulando de 10 em 10
print(inteiro)

print()
print('--------------------------------------------')
print()

lista = ['Davidson', 'Maria', 'José', 'Claudia', 'Jake']
sorteio = random.choice(lista) #Vai armazenar aleatoriamente um dos valores da lista
print(sorteio)


sorteio = random.choices(lista, k=2) #Vai armazenar aleatoriamente dois valores da lista na variavel, gerando uma lista de 2
#Detalhe, o choices neste caso pode ser que repita um mesmo nome, armazenando ele duas vezes
print(sorteio)

sorteio = random.sample(lista, k=2) #vai fazer a mesma coisa do choices acima, porém não existe a possibilidade de salvar
#o mesmo nome duas vezes
print(sorteio)

random.shuffle(lista) #Metodo vai embaralhar milha lista
print(lista)


print()
print('--------------------------------------------')
print()

letras = string.ascii_letters #vai armazenar basicamente todas as letras do alfabeto maiusculo e minusculo
digitos = string.digits #vai armazenar numeros de 0 a 9 no formato de string
caracteres = '!@#$%*._-' #apenas criando uma variavel com alguns caracteres

geral = letras + digitos + caracteres
senha = ''.join(random.choices(geral, k=20))