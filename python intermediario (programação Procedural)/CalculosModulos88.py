#Este arquivo faz parte da aula 88 de como criar modulos em python

import math

PI = math.pi

def dobraLista(lista):
    return [x*2 for x in lista]

def multiplica(lista):
    r = 1
    for i in lista:
        r = r * i
    return r

#Lembrando que quando damos print(__name__) em qualquer arquivo, vai retornar mais
#porém, quando damos um print(__name__) num arquivo que possui import de outro arquivo,
#O arquivo passa a ter o nome do arquivo importado

if __name__ == '__main__': #Estou dizendo que tudo que está dentro do if, se for chamado em outro arquivo por meio de import, não deve ser executado.
    #caso seja executado neste arquivo mesmo, vai executar normalmente
    lista = [1, 2, 3, 4, 5]
    print(dobraLista(lista))
    print(multiplica(lista))
    print(PI)