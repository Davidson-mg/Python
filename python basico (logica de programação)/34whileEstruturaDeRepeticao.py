x = 1

while x < 10:

    if x == 3:
        x = x + 1
        continue #esse continue serve para ele pular um ciclo do while. É necessario somar o x com 1 acima pra não ficar preso em loop infinito

    print(f'Davidson{x}')
    x = x + 1

print('Fim do while')

print()
print('-----------------------------------------')
print()

x2 = 1
while x2 < 10:

    if x2 == 3:
        break #O brek serve para interromper o loog independente dele ter feito todos os ciclos ou não.

    print(f'Davidson{x2}')
    x2 = x2 + 1

print('Fim do while')



while True:
    n1 = input('Digite um numero: ')
    n2 = input('Digite outro numero: ')
    operador = input('Digite um operador: ')

    if not n1.isnumeric() or not n2.isnumeric(): #Estou verificando se n1 e n2 são numeros inteiros. O not é como se eu dissesse 'Se n1 não é numero ou se n2 não é numero'
        print('Você precisa digitar um numero')
        continue # Se atender a condicional, não executa o que está em baixo e volta pro inicio do laço
    else:
        n1 = int(n1)
        n2 = int(n2)

    if operador == '+':
        print (f'Resultado: {n1+n2}')
    if operador == '-':
        print (f'resultado: {n1-n2}')
    if operador == '*':
        print (f'resultado: {n1*n2}')
    if operador == '/':
        print (f'resultado: {n1/n2}')


    pergunta = input('Deseja continuar? digite "s" para sim ou "n" para não')

    if pergunta == 'n':
        break