lista = ['luiz', 'joão', 'maria']

n1, n2, n3 = lista #Neste caso, cada variavel vai receber um dado da lista "lista" nas respectiva ordem.

print(n2) #vai imprimir "joão"



d1, d2 = lista ##Ainda neste caso, se você digita um numero menor de variaveis em relação a qtd de dados da lista, da erro. No exemplo abaixo resolvemos isso



lista2 = ['Davidson', 'Claudia', 'Julia', 45, 87, 8.4]

c1, c2, *outra_lista = lista2 #RESOLVENDO O ERRO CITADO ACIMA. Aqui, estou pegando os dois primeiros dados da lista acima e adicionando nas variaveis c1 e c2 na respectiva ordem. O asterix na ultima variavel *outra_lista, serve para dizer que não desejo pegar os demais dados da lista separadamente, não importando quantos tenha, então, ele vai formar uma nova lista com os demais dados

print(n1, n2) #Vai imprimir: 'Davidson', 'Claudia'

print(n1, n2, outra_lista) #vai imprimir: 'Davidson', 'Claudia', ['Julia', 45, 87, 8.4]




e1, e2, *outra_lista2, e3 = lista #Neste caso, as duas primeiras variaveis vão receber os dois primeiros valores da lista na respectiva ordem, a variavel com asterix *outra_lista2 vai receber uma nova lista com os damsi valores, menos o ultimo, que será adicionado na ultima variavel e3

print(e1, e2, outra_lista2, e3) #vai imprimir: 'Davidson', 'Claudia', ['Julia', 45, 87], 8.4


*outra_lista3, v1, v2 = lista2 #Neste caso, vai armazenar os dois ultimos valores da lista nas variaveis v1 e v2 na respectiva ordem e os demais dados serão armazenados na variavel com * *outra coisa.

print(v1, v2, outra_lista2) #vai imprimir assmi: ['Davidson', 'Claudia','Julia', 45], 87, 8.4