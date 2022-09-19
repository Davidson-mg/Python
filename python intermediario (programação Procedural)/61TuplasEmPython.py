#Tuplas são bem parecidas com listas. A maior diferença é que não podemos altera-la

#OBS IMPORTANTE: Basicamente tudo que foi ensinado na aula "43DesempacotamentoDeListasEmPython" em "python basico (logica de programação)"
# pode ser aplicado em tuplas, por isso, vou falar apenas das questões mais especificas de tupla

print()

t1 = (1,2,3, 'Davidson', 'Marcos', 'Gomes')

print(t1)

for v in t1: #Como já vimos antes, vai percorrer a tupla imprimir os valores em sequencia
    print(v)


print(t1[2:]) #Vai 'fatiar' (mostrar) os valores a partir do indice 2 até o ultimo. Para mais detalhes, reveja o arquivo (aula) "43DesempacotamentoDeListasEmPython" em "python basico (logica de programação)"



print()
print('--------------------------------------')
print()



t2 = 1,2,3, 'Davidson', 'Marcos', 'Gomes' #Posso criar tuplas dessa forma também
print(t2)




print()
print('--------------------------------------')
print()



t3 = 1, #Criando uma tupla com um elemento. Repare que é necessario usar uma virgula depois do elemento, senão, será entendido como uma variavel de numero inteiro
print(t3)



print()
print('--------------------------------------')
print()



t10 = 1,2,3,4,5,'a'
t11 = 6,7,8,9,'b'
t12 = t10 + t11 #juntando duas tuplas. vai imprimir: (1, 2, 3, 4, 5, 'a', 6, 7, 8, 9, 'b')
print(t12)

n1, n2, n3, *_, n10 = t12
print(n10) #Vai imprimir: 'b'




print()
print('--------------------------------------')
print()



t1 = (1,2,'a','b') * 3 #Será armazenada uma tupla equivalente 3 vezes
print(t1) #Vai imprimir: (1, 2, 'a', 'b', 1, 2, 'a', 'b', 1, 2, 'a', 'b')


print()
print('--------------------------------------')
print()

t1 = (1,2,'a','b')
# tl[1] = 3 #Vai da erro, por isso está comentado. Tentando modificar a tupla e, em tuplas isso não é possivel. Teria que converter pra lista primeiro

t1 = list(t1) #converti minha tupla pra lista
t1[2] = 'Davidson' #agora sim consigo alterar algum item
print(t1) #Vai imprimir [1, 2, 'Davidson', 'b']

tl = tuple(t1)#convertendo minha lista para tupla novamente
print(t1) #Vai imprimir [1, 2, 'Davidson', 'b']
