from datetime import datetime, timedelta

data = datetime(2019, 4, 20, 10, 42 ,10)# Nos datetime podemos passar 6 parametros que são equivalentes
#a ano, mês, dia, hora, minutos, segundos, sendo que, horas, minutos e segundos são opcionais

print(data) #vai imprimir formatada no padrão americano: 2019-04-20 10:42:10
print(data.strftime('%d/%m/%Y %H:%M:%S')) #Formatando a data e hora para o padrão BR conforme as diretivas do datetime

print()
print('----------------------')
print()

data = datetime.strptime('21/08/2022','%d/%m/%Y')
print(data) #como não enviei a hora, vai imprimir assim: 2022-08-21 00:00:00

print(data.timestamp()) #Vai imprimir: 1661050800.0

print()
print('----------------------')
print()

data = datetime.strptime('20/04/1902 20:00:00', '%d/%m/%Y %H:%M:%S')
data = data + timedelta (days=5, seconds=59) #Estou acrescentando 5 dias a data e 59 segundos
print(data.strftime('%d/%m/%Y %H:%M:%S'))

data = data + timedelta (days=5, seconds=2*60*60) #Estou acrescentando 5 dias a data e 2 horas a mais
print(data.strftime('%d/%m/%Y %H:%M:%S'))

data = data + timedelta (days=5, seconds=59*60) #Estou acrescentando 5 dias a data e 59 minutos a mais
print(data.strftime('%d/%m/%Y %H:%M:%S'))


d1 = datetime.strptime('20/04/1902 20:00:00', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('25/04/1902 22:33:00', '%d/%m/%Y %H:%M:%S')
diferenca = d2 - d1
print(diferenca) #vai mostrar a diferença de tempo entre as duas datas
print(diferenca.days) #vai mostrar a diferença de tempo entre as duas datas mostrando apenas os dias
print(diferenca.total_seconds())#vai mostrar a diferença de tempo entre as duas datas mostrando os segundos totais
print(d1.time())#Vai mostrar apenas a hora da data





"""

DIRETIVAS DO DATETIME

Dia da semana como nome abreviado da localidade.

Dom, Seg, …, Sáb (pt_BR);
Então, Mo, …, Sa (de_DE)
(1)

%A

Dia da semana como nome completo da localidade.

domingo, segunda, …, sábado (pt_BR);
Sonntag, Montag, …, Samstag (de_DE)
(1)

%w

Dia da semana como um número decimal, onde 0 é domingo e 6 é sábado.

0, 1, …, 6

%d

Dia do mês como um número decimal preenchido com zeros.

01, 02, …, 31

%b

Mês como o nome abreviado da localidade.

Jan, Fev, …, Dez (pt_US);
Jan, Fev, …, Dez (de_DE)
(1)

%B

Mês como o nome completo da localidade.

janeiro, fevereiro, …, dezembro (pt_BR);
Janeiro, fevereiro, …, dezembro (de_DE)
(1)

%m

Mês como um número decimal preenchido com zeros.

01, 02, …, 12

%y

Ano sem século como um número decimal preenchido com zeros.

00, 01, …, 99

%Y

Ano com século como um número decimal.

1970, 1988, 2001, 2013

%H

Hora (relógio de 24 horas) como um número decimal preenchido com zeros.

00, 01, …, 23

%I

Hora (relógio de 12 horas) como um número decimal preenchido com zeros.

01, 02, …, 12

%p

Equivalente da localidade de AM ou PM.

AM, PM (en_US);
am, pm (de_DE)
(1), (2)

%M

Minuto como um número decimal preenchido com zeros.

00, 01, …, 59

%S

Segundo como um número decimal preenchido com zeros.

00, 01, …, 59

(3)

%f

Microssegundo como um número decimal, preenchido com zeros à esquerda.

000000, 000001, …, 999999

(4)

%z

Deslocamento UTC no formato +HHMM ou -HHMM (string vazia se o objeto for ingênuo).

(vazio), +0000, -0400, +1030

(5)

%Z

Nome do fuso horário (string vazia se o objeto for ingênuo).

(vazio), UTC, EST, CST

%j

Dia do ano como um número decimal preenchido com zeros.

001, 002, …, 366

%U

Número da semana do ano (domingo como o primeiro dia da semana) como um número decimal preenchido com zeros. Todos os dias de um novo ano que antecedem o primeiro domingo são considerados na semana 0.

00, 01, …, 53

(6)

%W

Número da semana do ano (segunda-feira como o primeiro dia da semana) como um número decimal. Todos os dias de um novo ano que antecedem a primeira segunda-feira são considerados na semana 0.

00, 01, …, 53

(6)

%c

A representação de data e hora apropriada da localidade.

Ter, 16 de agosto 21:30:00 1988 (en_US);
Di 16 ago 21:30:00 1988 (de_DE)
(1)

%x

A representação de data apropriada da localidade.

16/08/88 (Nenhum);
16/08/1988 (pt_US);
16.08.1988 (de_DE)
(1)

%X

A representação de hora apropriada da localidade.

21:30:00 (pt_EUA);
21:30:00 (de_DE)
(1)

%%

Um personagem literal '%'.

%
"""