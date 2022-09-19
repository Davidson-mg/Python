variavel = ['Davidson Marcos', 'João Pereira', 'Maria']

for indice in variavel:
    if indice.startswith('D'): #Essa função "startswith" Vai verificar se o conteudo no indice atual começa com a letra j
        print(f'{indice} começa com D')
    else:
        print(f'{indice} não começa com D')



print()
print('-----------------------------------------')
print()




variavel = ['João Pereira','Davidson Marcos', 'Maria']

comeca_com_d = False

for indice in variavel:
    if indice.lower().startswith('d'): #Ele vai converter a letra em minuscula e depois comparar com letra minuscula. Isso resovel o problema de não considerar a letra minuscula caso a letra seja maiuscula.
        comeca_com_d = True

if comeca_com_d:
    print('Existe uma palavra que começa com d')

else:
    print('Não existe uma palavra que começa com d')




print()
print('-----------------------------------------')
print()


variavel = ['João Pereira','Davidson Marcos', 'Maria']

comeca_com_d = False

for indice in variavel:
    if indice.lower().startswith('d'): #Ele vai converter a letra em minuscula e depois comparar com letra minuscula. Isso resovel o problema de não considerar a letra minuscula caso a letra seja maiuscula.
        comeca_com_d = True

if comeca_com_d:
    print('Existe uma palavra que começa com d')

else:
    print('Não existe uma palavra que começa com d')