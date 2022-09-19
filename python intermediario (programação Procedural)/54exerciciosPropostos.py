"""Crie uma função que exibe uma saudação com os parametros saudação e nome"""

def saudacaoNome (n):
    print(f'Olá, {n} lindeza!')

saudacaoNome('Davidson');

print()
print('------------------------------------')
print()




"""Crie uma função que recebe 3 numeros como parametro e exiba a soma entre eles"""

def tresNumeros (n1, n2 ,n3):
    print(n1+n2+n3)

tresNumeros(5, 4, 3)

print()
print('------------------------------------')
print()





"""Crie uma função que receba 2 numeros. O primeiro é um valor e o segundo um percentual
(ex: 10%). Retorne (return) o valor do primeiro numero somado do aumento do percentual do"""

def aumentoPercentual(valor, percentual):
    resultado = valor * (percentual/100)
    return (f'Você teve um aumento de R${resultado}, totalizando agora R${valor + resultado}')

var1 = float(input('Informe quanto de dinheiro você tinha: '))
var2 = float(input('Informe a porcentagem que você recebeu de aumento: '))
aumento = aumentoPercentual(var1, var2)

print(aumento)


print()
print('------------------------------------')
print()




""" - Fizz Buzz - Se o parametro da função for divisivel por 3, retorne fizz,
se o parametro da função for divisivel por 5, retorne buzz. Se o parametro da função for 
divisivel por 5 e por 3, retorne FizzBuzz, caso contrario, retorne o numero enviado"""


def divisivel(n):
    if n%3 == 0 and n%5 == 0:
        return f'FizzBuzz, {n} é divisivel por 3 e 5'
    if n%5 == 0:
        return f'Buzz, {n} é divisivel por 5 apenas'
    if n%3 == 0:
        return f'Fizz, {n} é divisivel por 3 apenas'

    return 'Numero invalido';

numero = int(input('Informe um numero inteiro: '))

print(divisivel(numero))




from random import randint #Ele ainda vai explicar isso, mas o obj aqui é gerar numeros aleatorios

for i in range(10):
    aleatorio = randint(0, 10)
    print(divisivel(aleatorio))