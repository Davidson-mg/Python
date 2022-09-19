contador = 1;
acumulador = 1

while contador <= 10: #é possivel em python colocar um else.
    print(contador, acumulador)

    if contador > 5:
        break #Ao efetuar o break, ele não vai executar o else abaixo

    acumulador = acumulador + contador
    contador = contador + contador

else: #quando terminar o laço, ao inves de sair do while totalmente, ele executa primeiro o else pra depois sair.
    print('Cheguei no else')


print('Isso será executado')

