idade = 18;
sexo = 'F'
nome = input("Informe seu nome: ");

"""elif é igual o else if de outras linguagens"""

if idade >= 18 and sexo == 'F':
    print(f'{nome} maior de idade do sexo feminino');
elif idade >= 18 and sexo == 'M':
    print(f'{nome} de idade do sexo masculino');
elif idade < 18 and sexo == 'F':
    print(f'{nome} de idade do sexo feminino');
else:
    print(f'{nome} de idade do sexo masculino');