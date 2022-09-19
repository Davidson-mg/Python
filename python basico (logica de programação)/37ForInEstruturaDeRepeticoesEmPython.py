texto = 'Python'
for letra in texto:
    print(letra)

print()
print('-----------------')
print()

for n, letra in enumerate (texto): #se eu quiser usar uma variavel como indice igual ao for de outras liguagens, tipo java, preciso do enumerate
    print(n, letra)

print()
print('--------------------------')
print()

for n in range(10): #Padrão, começa do zero e vai contando de um em um até 10
    print(n)

print()
print('--------------------------')
print()


for n in range(2, 10): #dessa forma, no primeiro parametro (2), estou dizendo de qual valor vai iniciar a contagem, neste caso, vai começar do 2. O segundo numero é até quanto devo contar. Por padrão conta de 1 em 1
    print(n)

print()
print('--------------------------')
print()


for n in range(0, 10, 1): #dessa forma, no primeiro parametro (0), estou dizendo de qual valor vai iniciar a contagem, neste caso, vai começar do zero. O segundo numero é até quanto devo contar. O terceiro numero é de quanto em quanto devo contar
    print(n)


print()
print('--------------------------')
print()

for n in range(20, 10, -1): #dessa forma, no primeiro parametro (20), estou dizendo de qual valor vai iniciar a contagem, neste caso, vai começar do 20. O segundo numero é até quanto devo contar. Como o numero de inicio é maior até o numero que devemos contar, o terceiro parametro precisa ser negativo para que ele conte de forma decrescente, se não, nada acontece
    print(n)


print()
print('--------------------------')
print()

texto = 'O rato roeu a roupa do rei de roma'
nova_string = '';

for letra in texto:
    if letra == 'r':
        nova_string += letra.upper() #esse upper serve pra transformar letras em maiusculas
    else:
        nova_string += letra

print (f'nova string: {nova_string}');
