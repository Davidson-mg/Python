"""
and, or, not e not in

"""

a = 2;
b = 3;

if a == 5 and b == 7:
    print('A e B são diferentes de 5 e 7');
else:
    print('A e B são iguais a 5 e 7');

print();

nome = 'Davidson Marcos';

if 'r' in nome: ##O "in" Vai verificar se existe a letra "u" dentro da varivel nome
    print('Existe a letra "r" no nome');
else:
    print('Não existe a letra "r" no nome');

print();

if 'r' not in nome: ##Se a letra "r" não existir dentro da varivel nome, executa
    print('Não existe');
else:
    print('Não existe a letra "r" no nome');

print();
print("------------------------------------------")
print();

if False:
    print('Um')
elif False:
    print('Dois')
elif False:
    print('Três')
elif True:
    print('Quatro')
elif False:
    print('Cinco')
else:
    print('Seis')

print();
print("------------------------------------------");
print();

num_1 = 0
num_2 = 0

if not num_1 != num_2:
    print('Retorno 1')
else:
    print('Retorno 2')


