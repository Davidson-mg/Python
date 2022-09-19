print('-------------')
print()

def funcao():
    print('Jesus é Rei!')

funcao();

print()
print('-------------')
print()

def funcaoMsg(msg):
    print(msg)

funcaoMsg('Mensagem')

print()
print('-------------')
print()

def saudacao (msg, nome):
    nome = nome.replace('e', '3') #sempre que achar uma letra "e" vai alterar pra 3
    print(msg, nome)

saudacao('Davidson', 'Lindo')

saudacao(nome='Edineia', msg='coleee') #Caso eu quiera inverter os valores das variaveis que serão passadas como parametro, basta nomea-las

print()
print('-------------')
print()

def saudacaoRetorno(nome, elogio):
    return f'O {nome} é muito {elogio}'

msg = saudacaoRetorno('Davidson', 'Lindo');

print(msg)

