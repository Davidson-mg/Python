



# FAZ PARTE DESTA AULA O ARQUIVO classes108. Abra ele para encontrar os restante da aula

from classes108 import Escritor
from classes108 import Caneta
from classes108 import MaquinaDeEscrever

escritor = Escritor('Davidson')
print(f'Escritor: {escritor.nome}') #Acessando

caneta = Caneta('Bic')
print(f'Caneta: {caneta.marca}')

maquina=MaquinaDeEscrever()
print(maquina)

print()
print('--------------------------------------')
print()

print(escritor.nome)
print(caneta.marca)
maquina.escrever()


print()
print('--------------------------------------')
print()

escritor.ferramenta = caneta #A variavel ferramenta está dentro da classe escritor e, estou dizendo que essa variavel
#vai receber o valor da variavel caneta. Ou seja, o atributo ferramenta da classe escritor vai receber a classe caneta inteira.
escritor.ferramenta.escrever() # com isso, consigo acessar o metodo escrever ou qualquer outro que esta dentro da classe caneta. Ou seja,
#Consigo agora acessar um metodo da classe caneta, pelo atributo da classe escritor. Vai imprimir: 'A Caneta está escrevendo...'

