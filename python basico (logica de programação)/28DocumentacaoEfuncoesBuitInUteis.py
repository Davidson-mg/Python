num1 = input('Informe um numero: ')
num2 = input('Informe outro numero: ')

if num1.isdigit() and num2.isdigit(): #isdigit é uma função que verifica se uma string pode ser convertida para int. Neste caso, para ser possivel converter, a string precisa ter apenas numeros
    num1 = int(num1);
    num2 = int(num2);

    print(f'Resultado: {num1 + num2}')
else:
    print('Os valores informados não podem ser convertidos para inteiro')

print()
print('---------------------------------------')
print()

n1 = input('Informe um numero: ')
n2 = input('Informe outro numero: ')

try:
    n1 = int(num1);
    n1 = int(num2);

    print(f'Resultado: {n1 + n1}')
except:
    print('Os valores informados não podem ser convertidos para inteiro');