# Indices lembrando que strings têm indices, conforme explicado na aula 33.IndicesFaruamentoDeStringsEmPython
#        0123456789........................'

frase = 'O rato roeu a roupa do rei de roma' #possui tamanho de 34 caracteres
tamanho_frase = len(frase) #vai armazenar na variavel tamanho_frase o valor que a qtd total de caracteres contidos no texto da variavel frase, que neste caso é 34 caracteres
contador = 0;

while contador < tamanho_frase:
    print(frase[contador], contador)
    contador = contador + 1;




print()
print('--------------------------------------------------')
print()




contador = 0;
string_vazia = ''

while contador < tamanho_frase:

    if frase[contador] == 'r': #verificando se o caractere atual da frase da varial 'frase' é um r minusculo, se for...
        string_vazia += 'R' #Vai concaterna um R maiusculo
    else:
        string_vazia += frase[contador] #vai inserindo (concatenando) as letras da frase da variavel 'frase'  nessa nova variavel 'string_vazia'

    contador += 1;


print (f'String Vazia: {string_vazia}');
