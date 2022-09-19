#exercicio_de_python_somando_duas_listas.py
"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

#Jeito facil
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]

juncao = list(zip(lista_a, lista_b))
print(juncao)

print()

soma = [float(x + y) for x, y in zip(lista_a, lista_b)]
print(soma)


print()
print('-----------------------------------------------')
print()

#Jeito dificil e generica para qualquer linguagem

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

soma = []
for i in lista_a:
    for j in lista_b:
        if i > len(lista_b):
            break
        if i == j:
            soma.append(float(i+j))
        continue
print(soma)


print()
print('-----------------------------------------------')
print()

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

lista_soma = []
for i in range(len(lista_b)):
    lista_soma.append(lista_a[i] + lista_b[i])
print(lista_soma)
