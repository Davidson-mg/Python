"""
public, protected, private: O python não utiliza essas retrições, semelhantes ao JAVA por exemplo.
O objetivo delas é restringir o acesso de minhas variaveis. Por exmeplo, private só pode ser acessado
dentro da classe e o protected pode ser acessado somente na classe pai e nas classes que herdam a classe pai.
Public é publico.

"""

#Por conversão, toda variavel numa classe que vem seguida de _ (exemplo: _dados), recomenda-se usar somente dentro da classe

# _  semelhante ao protected, vc ainda consegue acessar, embora seja dificultado pelo _ pois não é sugerido essa variavel quando começa a digita-la sem o _
# __ semelhando ao private. Não te impede de chamar a variavel com __, porém se vc usa essa variavel fora da classe, na pratica, ele vai criar outro atribudo sem inserir ou modificar o original

class BaseDeDados:
    def __init__(self):
        self.__dados = {} #Criando um dicionario vazio. Vamos tratar esse atributo como se fosse uma tabela BD

    @property #Queremos obter um dado
    def dados(self): #Fazendo um metodo da classe parecer uma propriedadade da classe. Vai possibilitar acessarmos os atributos da classe normalmente, sem o __
        return self.__dados

    def inserirCliente(self, id, nome): #Este metodo vai inserir dados. Quando este metodo for chamado,
        #deve receber como parametro id e nome
        if 'clientes' not in self.__dados: #conferindo a chave (do dicionario) clientes não está nesse dicionario.
            # Se não etiver, vamos criar
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome}) #Se já existe a chave cliente no dicionario, nós vamos atualizar o que já existe

    def listaClientes(self): #metodo para exibir os dados.
        for id, nome in self.__dados['clientes'].item():
            print(id, nome)

    def apagaClientes(self, id): #metodo para apagar os dados.
        del self.__dados['clientes'][id]

bd = BaseDeDados()

bd.inserirCliente(1,'Davidson')
bd.inserirCliente(2,'Maria')
# bd.inserirCliente(3,'Cleusa')
#
# bd.dados = 'Uma outra coisa'

# bd.__dados = 'outra coisa'
# print(bd.__dados)


# print(bd.__dados) #Não te impede de chamar a variavel com __, porém se vc usa essa variavel fora da
# classe, na pratica, ele vai criar outro atribudo sem inserir ou modificar o original

# print(bd._BaseDeDados__dados) #Uma vez que utilizo __ nas minhas variaveis da classe

print(bd.dados) #Só esta sendo possivel acessar os dados sem o __ na frente por conta do metodo @property dentro da classe