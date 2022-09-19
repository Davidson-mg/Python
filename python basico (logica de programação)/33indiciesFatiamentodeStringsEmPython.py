texto = 'Davidson Marcos'
print(texto[3]) #Vai imprimir apenas o caractere do indice 3 da variavel texto. Neste caso, vai imprimir 'i'

print(texto[2:6]) #vai imprimir somente os caraceteres que vão do indice 2 ao 6. Neste caso, vai imprimir 'vids'

print(texto[:6]) #Vai imprir os caraceteres começando do zero ao sexto indice. Neste caso, vai imprimir 'Davids'

print(texto[4:]) #Vai imprir os caraceteres começando do sendo segundo indice até o final. Neste caso, vai imprimir 'dson Marcos'

print (texto[:-3]) #Vai imprimir a string sem os três caracteres. Quando informamos nº negativos, ele conta de trãs pra frente não os exibindo

novo_texto = texto [-2] #vai salvar na variavel novo_texto o indice 2 de trâs pra frente, ou seja, vai armazenar a letra 'o'
print (novo_texto) #Vai exibir a letra 'o'

novo_texto = texto [-10:-3] #Vai salvar na variavel novo_texto os caracteres 10 e 3 de trâs pra frente, ou seja, vai armazenar 'son Mar'
print (novo_texto) #vai imprimir 'son Mar'

novo_texto = texto [:-10] #vai salvar na variavel novo_texto todos os caracteres contando a partir do carctere 10 de trâs pra frente, ou seja, vai armazenar 'David"
print (novo_texto) #vai imprimir 'David"

novo_texto = texto[0:10:2] #Vai imprimir do indice 0 ao indice 10 pulando de 2 em 2. Vai salvar assim: 'Dvdo'
print (novo_texto) #vai imprimir 'Dvdo'

novo_texto = texto[0::2] #Vai imprimir até o final da string pulando de 2 em 2. Vai salvar assim: 'Dvdo'
print (novo_texto) #vai imprimir 'Dvdo acs'

#EXEMPLO VISUAL
# positivos       [012345678]
txt             = 'python s2'
# negativos      -[987654321] #repare que quando usamos negativo o indice 0 não conta