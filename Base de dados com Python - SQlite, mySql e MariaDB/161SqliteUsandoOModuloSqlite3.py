import sqlite3

conexao = sqlite3.connect('basededados.db') #obj de conexão
cursor = conexao.cursor() #obj de cursor
# #sempre que vc abre uma conexão e um cursor, precisa fechar ao final de seu condigo

cursor.execute('CREATE TABLE IF NOT EXISTS clientes(' #criando a tabela caso não exista
               'idcliente INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT,'
               'peso REAL'
               ')') #criando uma table caso não exista


#OS EXEMPLOS DE INSERT ABAIXO ESTOU DEIXANDO COMENTADO PARA NÃO FICAR INSERINDO DADOS TODA VEZ QUE EXECUTAR O CODIGO


# cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("Davidson", 63.2)') #inserindo os dados na tabela
#
# # Abaixo estamos inserindo valores na tabela de três formas diferentes
#
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Maria', 58))#Neste caso, estamos inserindo no
# # formato de tuplas
#
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)', {'nome':'Joãzinho', 'peso':25}) #Neste caso,
# #estamos inserindo no formato de um dicionario
#
# cursor.execute('INSERT INTO clientes VALUES (:idcliente, :nome, :peso)', { 'idcliente': None, 'nome':'Joana', 'peso':78}) #Neste caso,
# #estamos inserindo no formato de um dicionario passando o id como None (null)

# conexao.commit() #Esse comando vai fazer executar os cursores acima.



#Qualquer comando de SQL vc pode executar conforme exemplo abaixo
cursor.execute('UPDATE clientes SET nome =:nome WHERE idcliente =:idcliente', #modificando um nome na tabela com dicionario
               {'nome': 'João', 'idcliente':3})
conexao.commit() #sempre que executar um comando ddl precisa do commit logo em seguida, se não, não insere



cursor.execute('SELECT * FROM clientes') #vai executar este comando do sql, mas só vai mostrar no comando abaixo 'cursor.fetchall()'
# cursor.fetchall() #depois de ter executado o comando de select acima, aqui, estamos exibindo o resultado



for linha in cursor.fetchall():
    # print(linha) #A cada linha vamos ter uma tupla
    idcliente, nome, peso = linha
    print(idcliente, nome, peso)


cursor.close()
conexao.close()

