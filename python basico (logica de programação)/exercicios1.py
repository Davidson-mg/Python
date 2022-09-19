"""Faça um programa que peça ao usuario para digitar um numero interiro,
informe se este numero é par ou impar. Caso o usuario não digite um numero
inteiro, informe que não é um numero inteiro"""


numero = input("Informe um numero: ")

try:
    numero = int(numero);

    if (numero % 2) == 0:
        print ("O numero é par");
    elif (numero % 2) != 0:
        print("O numero é impar");
except:
    print('ERROR')


print()
print('--------------------------------------------------------')
print()


"""Faça um programa que peça o primeiro nome ao usuario. Se o nome tiver 4 letras ou menos, escreva
"seu nome é curto"; se tiver entre 5 e 6 letras, escreva "seu nome é normal"; maior que 6 escreva\
"seu nome é muito grande"""

nome = input("informe apenas o primeiro nome: ");


if len(nome) <= 4:
    print('Seu nome é curto')
elif len(nome) == 5 or len(nome) == 6:
    print('Seu nome é normal')
else:
    print('Seu nome é grande de mais.');



print()
print('--------------------------------------------------------')
print()

"""Faça um program que pergunte a hora ao usuario e, baseando-se no horario descrito,
exiba a saudação apropriada. Ex. Bom dia 0-11, boa tarde 12-17 e boa niote 18-23"""


horario = int(input('Informe um horario entre 0 e 23 horas: '))

if horario > 23:
    print('Por favor, informe um horario entre 0 e 23 horas')
elif horario >= 0 and horario <= 11:
    print(f'Bom dia! {horario}')
elif horario > 11 and horario <= 17:
    print (f'Boa tarde! {horario}')
else:
    print (f'Boa noite! {horario}')









