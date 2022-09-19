def falaOi():
    print('Oi')

var = falaOi #estou dizendo que minha variavel é igual minha função
var() #Var passa a precisar dos () pois se tornou uma função

print()
print('--------------------------')
print()

def master():
    def slave():
        print('oi')

master() #Nada vai acontercer, pois a função master apenas cria uma função

print()

def master2():
    def slave2():
        print('oi')
    slave2()

#vai imprimir: oi
master2() #Diferente do exemplo acima, a minha função master vai criar uma função e depois executa-la

print()

def master3():
    def slave3():
        print('oi')
    return slave3

#vai imprimir: oi
var = master3() #Dessa forma voltamos o primeiro exemplo deste arquivo. Estou dizendo que minha variavel é igual minha função, porém vai ser igual a função slave
var() #Var passa a precisar dos () pois se tornou uma função

print()
print('--------------------------')
print()


def master4(funcao): #Função master que vai receber uma funcao como parametro
    def slave4():
        funcao() #vai executar a função que a master está recebendo
    return slave4 #Porém, a master vai apenas retornar a função sem ser executada

def fala_oi():
    print('Oi')

var = master4(fala_oi) #Armazendo na variavel var a função slave4 que é retornada pela função master4
var()

print()

def master5(funcao): #Função master que vai receber uma funcao como parametro
    def slave5():
        print('Agora estou decorada')
        funcao() #vai executar a função que a master está recebendo
    return slave5 #Porém, a master vai apenas retornar a função sem ser executada

def fala_oi2():
    print('Oi')

fala_oi2 = master5(fala_oi2) # 'Fala oi' passa a ser igual master que retorna a função 'fala oi'. Vai ser uma volta desgramada
#para voltar pro mesmo ponto. Resumindo, estou dizendo que 'fala oi' é igual 'fala oi'. O obj disso e decorar a função

#Uma vez decorada, mesmo chamando 'fala oi' diretamente, vai executar o que está dentro da slave/master.
fala_oi2() #vai imprimir assim
# Agora estou decorada
# Oi

#OBS IMPORTANTE. TUDO QUE FOI EXPLICADO NESTE ARQUIVO ATÉ AQUI, SERVE APENAS PARA EXPLICAR COMO FUNCIONA DECORADORES EM PYTHON. ABAIXO SEGUE UM EXEMPLO USANDO UM DECORADOR PYTHON

print()
print('--------------------------')
print()

def master6(funcao): #Função master que vai receber uma funcao como parametro
    def slave6():
        print('Agora estou decorada')
        funcao() #vai executar a função que a master está recebendo
    return slave6 #Porém, a master vai apenas retornar a função sem ser executada

@master6 #o '@' seguido do nome de uma função, indica que a função abaixo deve ser decorada
def fala_oi3():
    print('Oi')

#fala_oi2 = master5(fala_oi2) # NÃO VAMOS MAIS PRECISAR DESSA LINHA. 'Fala oi' passa a ser igual master que retorna a função 'fala oi'. Vai ser uma volta desgramada
#para voltar pro mesmo ponto. Resumindo, estou dizendo que 'fala oi' é igual 'fala oi'. O obj disso e decorar a função

#Uma vez decorada, mesmo chamando 'fala oi' diretamente, vai executar o que está dentro da slave/master.
fala_oi3() #vai imprimir assim
# Agora estou decorada
# Oi


print()
print('--------------------------')
print()

def master7(funcao): #Função master que vai receber uma funcao como parametro
    def slave7(*args, **kwargs): #Neste exemplo, estamos recebendo via decorador uma função com parametros, que é a função 'outraFunçao" por isso estamos usando
        #*args e **kwargs. Lembrando que *args e **kwargs são utilizados caso tenha algum parametro. Se tiver ele repassa, se não, ele ignora.
        print('Agora estou decorada')
        funcao(*args, **kwargs) #vai executar a função que a master está recebendo
    return slave7 #Porém, a master vai apenas retornar a função sem ser executada

@master7 #o '@' seguido do nome de uma função, indica que a função abaixo deve ser decorada
def fala_oi4():
    print('Oi')

@master7
def outraFuncao(msg):
    print(msg)

outraFuncao('Olá!')

#fala_oi2 = master5(fala_oi2) # NÃO VAMOS MAIS PRECISAR DESSA LINHA. 'Fala oi' passa a ser igual master que retorna a função 'fala oi'. Vai ser uma volta desgramada
#para voltar pro mesmo ponto. Resumindo, estou dizendo que 'fala oi' é igual 'fala oi'. O obj disso e decorar a função

#Uma vez decorada, mesmo chamando 'fala oi' diretamente, vai executar o que está dentro da slave/master.
fala_oi4() #vai imprimir assim
# Agora estou decorada
# Oi


print()
print('--------------------------')
print()

from time import time
from time import sleep

def velocidade(funcao):
    def interna(*args, **kwargs):
        tempoInicio = time()
        resultado = funcao(*args, **kwargs)
        fimTempo = time()
        tempo = (fimTempo - tempoInicio) * 1000
        print(f'A função{funcao.__name__} levou {tempo:.2f}ms para executar.')
        return resultado
    return interna

@velocidade
def demora():
    for i in range(10):
        print(i, end='')
        sleep(1)

demora()