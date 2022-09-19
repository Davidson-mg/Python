
from random import randint
numero = str(randint(100000000, 999999999))
novo_cpf = numero
reverso = 10
soma=0
for n in range(19):


    if n > 8:
        n -= 9

    soma += int(novo_cpf[n]) * reverso

    reverso -= 1
    if reverso < 2:
        reverso = 11

        d = 11 - (soma % 11)

        if d > 9:
            d = 0
        soma = 0
        novo_cpf = novo_cpf + str(d)

print(novo_cpf)





