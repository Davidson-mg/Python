def divide(n1, n2):
    try:
     return n1/n2
    except ZeroDivisionError as error:
        print(error)
        return False

print(divide(2,0)) #Lembrando que dividir zero por um numero inteiro da erro



print()
print('-----------------------------')
print()

def divide2(n1, n2):
    try:
     return n1/n2
    except ZeroDivisionError as error:
        print('Log: ',error)
        raise#Neste caso, estou usando o raise para capturar parte da exceção, pois quero capturar-la também na chamada desta função divide2
        #conforme feito abaixo.

try:
    print(divide2(2,0)) #Lembrando que dividir zero por um numero inteiro da erro
except ZeroDivisionError as error:
    print (error)


print()
print('-----------------------------')
print()

# def divide3(n1, n2): #Coloquei comentado para não parar o codigo, pois, como não tratei o erro, para nas msg vermelhas de erro
#     if n2 == 0:
#         raise ValueError("n2 não pode ser 0.")#Aqui estou criando minha propria exceção com uma msg especifica minha para este problema.
#     #Com isso, ao tentar dividir por zero, vai aparecer aquela msg de erro normal do python, porém o nome do erro será esse que descrevi acima em raise
#     return n1/n2
#
# print(divide3(2,0)) #Lembrando que dividir zero por um numero inteiro da erro


print()
print('-----------------------------')
print()

def divide4(n1, n2): #igual ao exemplo de cima que comentei para não para o codigo, porém, na chamada da função eu tratei o erro
    if n2 == 0:
        raise ValueError("n2 não pode ser 0.")#Aqui estou criando minha propria exceção com uma msg especifica minha para este problema.
    #Com isso, ao tentar dividir por zero, vai aparecer aquela msg de erro normal do python, porém o nome do erro será esse que descrevi acima em raise
    return n1/n2

try:
    print(divide4(2,0)) #Lembrando que dividir zero por um numero inteiro da erro
except ValueError as error:
    print(error)


