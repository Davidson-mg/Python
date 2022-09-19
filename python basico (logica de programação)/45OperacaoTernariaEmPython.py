#Exemplo comum, não ternario

logged_user = False

if logged_user:
    msg = 'Usuario Logado'
else:
    msg = 'Usuario precisa logar'

print(msg)



#Exemplo Ternario

logged_user = True
msg='Usuario logado.' if (logged_user) else 'Usuario precisa logar' #Terá o mesmo efeito do exemplo acima com if

print(msg)



print()
print('-----------------------------------------')
print()



#Exemplo comum, não ternario

idade= int(input('Informe sua idade: '))
if idade >= 18:
    print('Pode acessar')
else:
    print('Não pode acessar')


print()

#Exemplo Ternario

idade= input('Informe sua idade: ')

if not idade.isnumeric(): #Se o valor digitado não é numerico
    print('Você precisa digitar apenas numeros')
else:
    idade = int(idade) #convertendo a string para numero
    de_maior = (idade >= 18) #Vai armazena um valor booleado (verdadeiro ou falso) na variavel "de_maior"
    msg='Pode acessar' if de_maior else 'Não pode acessar' #armazene a msg 'pode acessar' se de_maior for verdadeiro, se não, armazena a msg 'Não pode acessar'

print(msg)

print(type(de_maior))