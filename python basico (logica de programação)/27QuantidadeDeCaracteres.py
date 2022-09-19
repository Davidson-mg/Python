usuario = input('Digite seu usuario: ');
qtd_caracteres = len(usuario) #o len armazena na variavel a qtd de caracteres de uma variavel (entre parenteses). Ele faz isso armazenando no tipo int

print (usuario, qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres < 6:
    print('Você precisa digitar pelo menos 6 caracteres');
else:
    print('Você foi cadastrado no sistema');

print()
print('-----------------------------------------')
print()

string1 = input('Digite alguma coisa: ');
string2 = input('Digite outra coisa: ');

print(f'A quantidade total de caracteres digitados foi {len(string1) + len(string2)}')