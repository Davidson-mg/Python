# mutaveis: listas, dicionarios
# imutaveis: Tuplas, strings, numeros, True, False, None

def lista_de_clientes (clientes_iteravel, lista=[]): #A ideia desta função é o seguinte: Eu mando uma lista, se eu já tiver uma lista
    #de clientes, elas serão unidas
    lista.extend(clientes_iteravel)
    return lista

clientes1 = lista_de_clientes(['Davidson', 'Maria', 'Eduardo'])
clientes2 = lista_de_clientes(['Claudia', 'Beatriz', 'Amanda'])
clientes3 = lista_de_clientes(['José'])

print(f'Clientes1: {clientes1}')
print(f'Clientes2: {clientes2}') #Repare que neste caso teremos o seguinte problema, será impresso clientes1 a clientes2
#Isso acontece pq na função lista_de_clientes, caso não passe uma lista, ele vai unir com a lista padrão, caso haja uma lista pardão.
#Quando chamamos essa função na primeira vez passando uma lista, na segunda em diante, essa lista se torna padrão e nao importa quantas vezes e
#Quantas listas diferentes nós passamos, ela sempre vai considerar a primeira. Repre também que nem chamei clientes3 e mesmo assim incluir 'josé'

print()
print('----------------------------------------------------------------------------------')
print()

#No exemplo abaixo estamos corrigindo o problema do exemplo acima

def lista_de_clientes2 (clientes_iteravel, lista=None): #A ideia desta função é o seguinte: Eu mando uma lista, se eu já tiver uma lista
    #de clientes, elas serão unidas
    if lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista

clientes11 = lista_de_clientes2(['Davidson', 'Maria', 'Eduardo'])
clientes22 = lista_de_clientes2(['Claudia', 'Beatriz', 'Amanda'])
clientes33 = lista_de_clientes2(['José'])

print(f'Clientes1: {clientes11}')
print(f'Clientes2: {clientes22}') #Repare que neste caso teremos o seguinte problema, será impresso clientes1 a clientes2
#Isso acontece pq na função lista_de_clientes, caso não passe uma lista, ele vai unir com a lista padrão, caso haja uma lista pardão.
#Quando chamamos essa função na primeira vez passando uma lista, na segunda em diante, essa lista se torna padrão e nao importa quantas vezes e
#Quantas listas diferentes nós passamos, ela sempre vai considerar a primeira. Repre também que nem chamei clientes3 e mesmo assim incluir 'josé'



