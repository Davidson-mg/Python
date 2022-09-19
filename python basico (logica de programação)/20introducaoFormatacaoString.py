

x = 10;
y = 20;

print(f'{x} somado ao numero {y} resultará no valor de {x+y}'); "colocando um f antes das apas, possibilitia colocar valores dentro {}"

nome = 'Davidson'
peso = 63;
idade = 31;
altura = 1.65;
imc = peso / (altura ** 2); """Lembrando que '**' duas vezes é o mesmo que elevado"""

print(f'{nome} possui um imc de {imc:.2f}'); """O :.2f dentro das chaves do imc, serve para deixar o resultado flout com apenas duas casas decimais depois da virgula"""

print('{} possui {} anos de idade e seu imc é de {}'.format(nome, idade, imc)); """Outra forma de imprimir. Colocando {} onde serão variaveis. Após as apas vc coloca .format e as variaveis na sequencia que certa da string"""

print('{n} possui {i} anos de idade e seu imc é de {im}'.format(n=nome, i=idade, im=imc)); """Semelhante ao exemplo de cima, a diferença é que estou dando nome para as variaveis, dessa forma não precisaria seguir a ordem"""