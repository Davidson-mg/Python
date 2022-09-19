

for n in range (0, 11):
    print()
    decrescente = 10
    while decrescente >= 0:
        print(f'Crescente: {n} Decrescente: {decrescente}')
        decrescente -= 1;

print('--------------------------')

decrescente = 10
for n in range (0, 10):
    print(f'{n} - {decrescente}')
    decrescente -= 1;



print('--------------------------')

for x in range (1, 10,):
    print()
    for y in range (10, 1, -1):
        print(f'crescente: {x} descrescebte: {y}')


print('--------------------------')


for x, y in enumerate(range(10, 1, -1), 1):
    print(f' {x} - {y}')




