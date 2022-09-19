"""Crie uma função1 que recebe uma funcão2 como parametro e retorne o valor da funcao2 executada"""

def funcao1(f):
    return f()

def funcao2():
    return "Olá! Tudo bem?"

var = funcao1(funcao2) #chamando funcao1 e passando a funcao2 como parametro. Funcao1 vai retornar o resultado da funcao2 que ela recebeu como parametro
print(var)


print()
print('-----------------------------------------')
print()

"""Crie uma função1 que recebe uma função1 como parametro e retorne o valor da função2 executada. Faça a função1
executar duas funções que recebam um numero diferente de argumentos"""

def func1(f, *args,**kwargs): # Com **args e **kwargs, estou dizendo que minha função pode OU NÃO receber mais valores
    return f(*args, **kwargs) # **args e **kwargs só serão usados como parametros se tiver um terceiro ou mais parametros na chamada da func1. Se tiver apenas um parametro, vai considerar apenas f como parametro,


    #se ao chamar func1 eu passar apenas 2 parametros, func1 vai retornar apenas o resultado da função func2. Se eu passar 3 parametros, vai chamar a função func3
    #Vale ressaltar que o 1º parametro de func1 é uma função neste caso somos obrigados a passar pois func1 retorna uma função

def func2(nome):
    return f'Olá, {nome}!'

def func3(nome, saudacao):
    return f'{saudacao} {nome}!'


v = func1(func2, 'Davidson') #func1 deve ser chamada passando pelo menos dois parametros, pois o primeiro é uma função e dentro de func1 retorna uma função. O segundo parametro vai ser passado para a segunda função dentro de func1
v2 = func1(func3, 'Davidson', 'Bom dia,')
v3= func1(func2);
print(v)
print(v2)

