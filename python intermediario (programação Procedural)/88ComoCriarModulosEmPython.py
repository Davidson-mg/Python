
#Primeira forma de importar funções de outro arquivo
import CalculosModulos88 #Importando do meu arquivo CalculosModulos88
print(CalculosModulos88.PI)

lista = [1,2,3,4,5]
print(CalculosModulos88.multiplica(lista)) #Dessa forma eu preciso informar o nome do arquivo, seguido de '.nomeDaFunção'


##Segunda forma de importar funções de outro arquivo

from CalculosModulos88 import multiplica #Neste caso estou importando apenas a função multiplica

lista = [1,2,3,4,5]
print (multiplica(lista)) #Neste segundo import não precisa eu passar o nome do arquivo, basta passar o nome da função direto