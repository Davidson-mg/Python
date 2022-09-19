nome = input('Qual seu nome? '); """Esse input permite o usuario escrever algo e que será armazenado na variavel nome. OBS: Por padrão, vai sempre armazena como string, mesmo que digite um numero"""

print(f'O nome do usuario é {nome} e o tipo dela é {type(nome)}'); """Lembrando que mesmo que responda digitando um numero, vai dizer que o tipo é string"""

print()

idade = input('Qual sua idade: ');

print(type(idade))

idade = int(idade);

print(type(idade))

idade2 = int(input('Qual sua idade novamente: '))

print(type(idade2))

