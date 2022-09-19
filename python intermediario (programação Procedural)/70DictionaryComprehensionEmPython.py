l1 = [1,2,3,4]
l2 = [v*2 for v in l1]
print(l2)

print()
print('------------------------------')
print()

lista = [('chave', 'valor'),
         ('chave2', 'valor')
]

d1 = {x : y for x, y in lista} #x e y serão equivalentes a chave e valor
#  d1=disct(lista)#Teria exatamente o mesmo resultado acima
print(d1) #Vai imprimir um dicionario: {'chave': 'valor', 'chave2': 'valor'}

d1 = {x : y.upper() for x, y in lista}#x e y serão equivalentes a chave e valor. Ao utilizar o 'upper' Estou transformando as letras da string em maiuscula
print(d1)#Vai imprimir: {'chave': 'VALOR', 'chave2': 'VALOR'}

print()
print('------------------------------')
print()

lista = [('chave', 2),
         ('chave2', 'valor')
]

d1 = {x : y*2 for x, y in lista} #x e y serão equivalentes a chave e valor. Neste caso, estou multiplicando o valor de y por 2.
#Onde for numero, será multiplicado, onde for string, serão duplicado
print(d1) #Vai imprimir assim

print()
print('------------------------------')
print()

lista = [('chave', 2),
         ('chave2', 'valor')
]

d1 = {f'chave_{x}': x**2 for x in range(5)} #Estamos criando um dicionario com chave e valor. O valor nesse caso será o numero elevado a 2. Com range, estou dizendo
#que a contagem vai até 5
print(d1) #Vai imprimir: {'chave_0': 0, 'chave_1': 1, 'chave_2': 4, 'chave_3': 9, 'chave_4': 16}