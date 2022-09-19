
#                                                           COMBINATIONS

from itertools import combinations #Para usar o combinations somos obrigados a fazer este import

pessoas = ['Davidson', 'André', 'Claudia']

for grupo in combinations(pessoas, 2): #Estou usando a função combinations que vai fazer uma combinação de 2 entre os elementos da lista pessoas
    print(grupo)
# Vai imprimir
# ('Davidson', 'André')
# ('Davidson', 'Claudia')
# ('André', 'Claudia')

#OBS IMPORTANTE. EX: NESTE CASO, AO COMBINAR 'DAVIDSON' COM 'ANDRE', QUANDO FOR COMBINAR 'ANDRE' COM OS NOMES, NÃO VAI FAZER A COMBINAÇÃO 'ANDRE' 'DAVIDSON', POIS ELE ENTENDE QUE
#SERIA UMA REPETICAO DE 'DAVIDSON' COM 'ANDRE'. OU DETALHE É QUE NÃO LEVA EM CONTA A ORDEM

print()
print('--------------------------------------------------')
print()

#                                                           PERMUTATIONS

#CASO QUEIRA PEGAR TODAS AS COMBINAÇÕES POSSIVEIS, INDEPENDENTE SE VAI REPETIR OU NÃO, DEVE USAR ESSE EXEMPLO ABAIXO COM

from itertools import permutations #Para usar o permutations somos obrigados a fazer este import

pessoas = ['Davidson', 'André', 'Claudia']

for grupo in permutations(pessoas, 2): #Estou usando a função combinations que vai fazer uma coninação de 2 entre os elementos da lista pessoas
    print(grupo)

# NESTE CASO. AO CONTRARIO DO EXEMPLO ACIMA DE COMBINATIONS, VAI FAZER TODAS AS COMBINAÇÕES POSSIVEIS CONSIDERANDO A ORDEM
#OBS IMPORTANTE: REPARE QUE ELE NÃO FEZ AS COMBINAÇÕES CONSIDERANDO O MESMO NOME. CASO QUEIRA INCLUIR ESSA COMBINAÇÃO, PRECISA USAR O EXEMPLO ABAIXO PRODUCT ABAIXO

# vai imprimir assim:
# ('Davidson', 'André')
# ('Davidson', 'Claudia')
# ('André', 'Davidson')
# ('André', 'Claudia')
# ('Claudia', 'Davidson')
# ('Claudia', 'André')


print()
print('--------------------------------------------------')
print()

#                                                           PRODUCT


#CASO QUEIRA PEGAR TODAS AS COMBINAÇÕES POSSIVEIS, INDEPENDENTE SE VAI REPETIR OU NÃO, DEVE USAR ESSE EXEMPLO ABAIXO COM

from itertools import product #Para usar o permutations somos obrigados a fazer este import

pessoas = ['Davidson', 'André', 'Claudia']

for grupo in product(pessoas, repeat=2): #Estou usando a função product que vai fazer uma coninação de 2 (precisa do repeat) entre os elementos da lista pessoas
    print(grupo)

# NESTE CASO. AO CONTRARIO DO EXEMPLO DO TOPO ACIMA, DE COMBINATIONS, VAI FAZER TODAS AS COMBINAÇÕES POSSIVEIS EM CONSIDERANDO A ORDEM E, AO CONTRARIO DO EXEMPLO PERMUTATIONS VAI
# FAZER TAMBÉM AS COMBINAÇÕES DE UM MESMO NOME

# vai imprimir assim:
# ('Davidson', 'Davidson')
# ('Davidson', 'André')
# ('Davidson', 'Claudia')
# ('André', 'Davidson')
# ('André', 'André')
# ('André', 'Claudia')
# ('Claudia', 'Davidson')
# ('Claudia', 'André')
# ('Claudia', 'Claudia')