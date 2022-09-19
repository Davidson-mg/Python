import sqlite3

class AgendaDb:
    def __init__(self, arquivo):
        self.conexao = sqlite3.connect(arquivo)
        self.cursor = self.conexao.cursor()

    def inserir (self, nome, telefone): #Esse 'OR IGNORE' é para não inserir em caso de um valor 'unique' já existem no BD
        consulta = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?, ?)' #interrogação recebe os valores das variaveis abaixo
        self.cursor.execute(consulta, (nome, telefone))
        self.conexao.commit() #sempre que executar um comando ddl precisa do commit logo em seguida, se não, não insere

    def editar(self, nome, telefone, id):
        consulta = 'UPDATE OR IGNORE agenda SET nome = ?, telefone = ? WHERE id = ?'
        self.cursor.execute(consulta, (nome, telefone, id))
        self.conexao.commit()


    def excluir(self, id):
        consulta = 'DELETE FROM agenda WHERE id = ?'
        self.cursor.execute(consulta, (id,)) #Esse modo de consulta com ?, se utiliza de tupla, então
        #neste caso que estamos passando somente id, precisa de uma virgula depois de id
        self.conexao.commit()

    def listar(self):
        self.cursor.execute('SELECT * FROM agenda')
        for linha in self.cursor.fetchall():
            print(linha)

    def buscar(self, valor):
        consulta = ('SELECT * FROM agenda WHERE nome LIKE ?')
        self.cursor.execute(consulta, (f'%{valor}%', )) #Esse modo de consulta com ?, se utiliza de tupla, então

        #neste caso que estamos passando somente um valor, precisa de uma virgula depois de id
        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self): # sempre que vc abre uma conexão e um cursor, precisa fechar ao final de seu codigo
        self.cursor.close()
        self.conexao.close()


if __name__ == '__main__':
    agenda = AgendaDb('agenda.db')
    agenda.inserir('Davidson', '31994274558')
    agenda.inserir('Davidson', '31994274558') #colocando um repedito só pra testar
    agenda.inserir('Davi', '2178866854')
    agenda.inserir('David', '1147758565')
    agenda.inserir('Davis', '3787785414')
    agenda.inserir('Claudia', '31997874212')
    agenda.inserir('Rosa', '31957744852')
    agenda.inserir('Claudia', '31958876321')
    agenda.inserir('Franco', '3187784589')
    agenda.inserir('Apagado', '666665789')
    agenda.editar('Francisco', '1135854771', 11)
    agenda.listar()

    print()
    print('------------------')
    print()

    agenda.excluir(4)
    agenda.listar()

    print()
    print('-------------------')
    print()

    agenda.buscar('vi')




