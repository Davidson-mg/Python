print('-----------------------------')
print()

try: #forma mais simples de usa uma exceção, porém não estamos trantando o erro aqui. No exemplo abaixo estaremos tratando o erro
    print(a)
except:
    print('Erro!')

print('Bora continuar!') #com exceções o codigo não para

print()
print('-----------------------------')
print()

try:
    print(a)
except NameError as erro: #Tratando o erro. Sem a exceção, a executar print(a), no terminal retornaria em vermelho este erro: NameError: name 'a' is not defined
    #Ou seja, pegamos a classe do erro (NameError) e inserimos na nossa exceção
    print('Erro!', erro)

print('Bora continuar!') #com exceções o codigo não para

print()
print('----------------------------')
print()

try:
    a=[] #Agora 'a' existe, não vai cair na exceção 'NameError'.
    print(a[1]) #Porém, a no indice 1 não existe, então, este é um erro que não esparavamos, logo, vai cair na exceção Exception
except NameError as erro: #Tratando o erro. Sem a exceção, a executar print(a), no terminal retornaria em vermelho este erro: NameError: name 'a' is not defined
    #Ou seja, pegamos a classe do erro (NameError) e inserimos na nossa exceção
    print('Erro!', erro)
except Exception as erro: #Caso vc ache que possa ter um erro que vc desconhece, coloque mais essa exceção
    print("ocorreu um erro inesperado")

print('Bora continuar!') #com exceções o codigo não para

print()
print('----------------------------')
print()

try:
    b=[] #Agora 'a' existe, não vai cair na exceção 'NameError'.
    print(a[1]) #Considerando que eu esperava este erro e passando a trata-lo abaixo em 'IndexError'
    c={}
    print(c[1])#Porém, c no indice 1 não existe, então, este é um erro vai cari em 'Erro de indice ou chave'
except NameError as erro: #Tratando o erro. Sem a exceção, a executar print(a), no terminal retornaria em vermelho este erro: NameError: name 'a' is not defined
    #Ou seja, pegamos a classe do erro (NameError) e inserimos na nossa exceção
    print('Erro!', erro)
except (IndexError, KeyError) as erro:
    print('Erro de indice ou chave')
except Exception as erro: #Caso vc ache que possa ter um erro que vc desconhece, coloque mais essa exceção
    print("ocorreu um erro inesperado")

print('Bora continuar!') #com exceções o codigo não para


print()
print('----------------------------')
print()


try:

    a = {} #Não teremos erro neste caso

except NameError as erro: #Tratando o erro. Sem a exceção, a executar print(a), no terminal retornaria em vermelho este erro: NameError: name 'a' is not defined
    #Ou seja, pegamos a classe do erro (NameError) e inserimos na nossa exceção
    print('Erro!', erro)
except (IndexError, KeyError) as erro:
    print('Erro de indice ou chave')
except Exception as erro: #Caso vc ache que possa ter um erro que vc desconhece, coloque mais essa exceção
    print("ocorreu um erro inesperado")
else:
    print('Seu codigo foi executado com sucesso') #O else será executado se não tiver nenhum problema
    print(a) #Imprimindo meu diconario 'a'
finally:
    print('Finalmente') #O bloco finally vai executar tendo ou não um erro

print('Bora continuar!') #com exceções o codigo não para



print()
print('----------------------------')
print()


try:

    a = 0
    try: #POsso também clocar try dentro de try
        a = 1/0
    except:
        print('Erro')

except NameError as erro: #Tratando o erro. Sem a exceção, a executar print(a), no terminal retornaria em vermelho este erro: NameError: name 'a' is not defined
    #Ou seja, pegamos a classe do erro (NameError) e inserimos na nossa exceção
    print('Erro!', erro)
except (IndexError, KeyError) as erro:
    print('Erro de indice ou chave')
except Exception as erro: #Caso vc ache que possa ter um erro que vc desconhece, coloque mais essa exceção
    print("ocorreu um erro inesperado")
else:
    print('Seu codigo foi executado com sucesso') #O else será executado se não tiver nenhum problema
    print(a) #Imprimindo meu diconario 'a'
finally:
    a = ''

print('Bora continuar!') #com exceções o codigo não para