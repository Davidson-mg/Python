#string = '01234567890123456789012345678901345678901234567890124567890123456789'
#lista = ['0123456789','0123456789','0123456789','0123456789'] #devemos criar uma lista neste formato
#retorno = '0123456789.012345789.0123456789.0123456789.0123456789' #Depois, devemos retornar a string dessa forma


def func(str):

    stringNumeros = ''
    for i in str:
        stringNumeros += i
        if i == '9':
            stringNumeros += ' '


    lista = stringNumeros.split(' ')
    print(f'Lista dentro da função: {lista} {type(lista)}')

    stringRetorno = stringNumeros.replace(' ', '.')
    return stringRetorno;


print()

string = '01234567890123456789012345678901345678901234567890124567890123456789'

Resposta = func(string)
print()
print(f'Retorno da função pedido pelo exercicio: {Resposta}')



print()
print('------------------------------------')
print()


#Como foi resolvido na aula pelo professor

string = '01234567890123456789012345678901345678901234567890124567890123456789'
n=10


#Tentando ilustrar como funciona o exemplo da lista abaixo
# comp = [(i, i+n) for i in range(0, len(string), 10)] #Entre parentese, estou criando uma tupla que recebe os valores de 'i' e 'i+n' (0, 10), lembrando que i inicia com 0.
#na parte do range, estou dizendo que ele vai receber TRÊS valores, o primeiro (0) é de onde inicia, o segundo (string) é referente ao tamanho da string e o terceiro (10) é de quanto
#em quanto ele deve contar,

lista = [string[i : i+n] for i in range(0, len(string), 10)] #estou criando uma tupla que recebe os valores de 'i' e 'i+n' (0, 10), lembrando que i inicia com 0.
#na parte do range, estou dizendo que ele vai receber TRÊS valores, o primeiro (0) é de onde inicia, o segundo (string) é referente ao tamanho da string e o terceiro (10) é de quanto
#em quanto ele deve contar,
print(lista);

retorno='.'.join(lista)