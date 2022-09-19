from datetime import datetime, timedelta
from locale import setlocale, LC_ALL
from calendar import mdays


dt = datetime.now() #Vai pegar a data atual
print(dt)
formatacao = dt.strftime('%A, %d de %B de %Y') #Estamos formatando exibindo o dia, depois uma virgural, depois o mês e o ano
#Essa formatação será feita no padrão EUA
print(formatacao) #Vai imprimir: Sunday, 21 de August de 2022

setlocale(LC_ALL, '') #Vamos usar o setlocale para receber a localização do brasil. Se coloco uma string '' vazia, ele.
#o setlocale precisa do import acima
#vai considerar a data do computador do usuario
formatacao = dt.strftime('%A, %d de %B de %Y')
print(formatacao) #Vai imprimir domingo, 21 de agosto de 2022

setlocale(LC_ALL, 'pt_BR.utf-8') #como dito acima, string vazia considera da data do pc do usuario, porém, caso eu queira
#especificar a o padrão brasileiro de data hora, basta fazer dessa forma
formatacao2 = dt.strftime('%d/%m/%Y %H:%M:%S')
print(formatacao2) #Vai imprimir: 21/08/2022 14:56:55

print()
print('----------------------------------')
print()

print(mdays) #mdays é uma lista com todos os ultimos dias de todos os meses. vai imprimir: [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dt = datetime.now() #Vai pegar a data atual
mesAtual = int(dt.strftime('%m'))
print(mesAtual, mdays[mesAtual]) #vai imprimir: 8 31 vai mostrar o mes da data atual e o ultimo dia dela,
# ou seja, o total de dias que ele têm


