#Precisa instalar no console do pycharm 'pip install pymysql'

import pymysql.cursors
from contextlib import contextmanager

@contextmanager
def conecta(): # Lembrando que, sempre que vc abre uma conexão e um cursor, precisa fechar ao final de seu codigo. Aqui nós estamos
#colocando a conexao dentro de uma função que vai fazer o papel de um gerenciador de contexto.
#Estamos usando essa função apenas para a conexão, pois o cursor vc consegue fechar por um gerenciador
#de cotexto with simples

    conexao = pymysql.connect( #Se conectando ao servidor jutamente com o banco que queremos deste servidor, neste caso,
        #banco de dados 'clientes'

        host= '127.0.0.1',
        user='root',
        password='',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor

    )
    try:
        yield conexao
    finally:
        conexao.close()

                                            #INSERINDO

# # ABAIXO EU DEIXEI COMENTADO PRA NÃO FICAR INSERINDO DADOS NO BD TODA VEZ QUE O CODIGO FOR EXECUTADO. No exemplo abaixo
# # inserimos no BD um cliente de cada vez
# with conecta() as conexao: #Após inserimos nossa conexão dentro do metod conecta afim de podermos usar o gerenciador
#     #de contexto para abrir e fechar a conexão, sempre que precisarmos acessar e manipular o BD, basta colocar tudo dentro
#     #dessa estrutura que a conexão e o cursor serão fechados automaticamente
#     with conexao.cursor() as cursor:                               #essa barra serve apenas para pula de linha
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES (%s, %s, %s, %s)'
#         cursor.execute(sql, ('Davidson', 'Marcos', 59, 63.2))
#         conexao.commit()



# #No exemplo abaixo inserimos em nossa table cliente varios clientes com base numa lista de python
# with conecta() as conexao: #Após inserimos nossa conexão dentro do metod conecta afim de podermos usar o gerenciador
#     #de contexto para abrir e fechar a conexão, sempre que precisarmos acessar e manipular o BD, basta colocar tudo dentro
#     #dessa estrutura que a conexão e o cursor serão fechados automaticamente
#     with conexao.cursor() as cursor:                               #essa barra serve apenas para pula de linha
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES (%s, %s, %s, %s)'
#
#         dados = [
#             ('Davidson', 'Marcos', 1579815, 72.7),
#             ('Craudineia', 'corcotita', 154, 23),
#             ('Cracudo', 'Macoloca', 21, 70),
#             ('Xiriquiclamatilda', 'Ratildenavasques', 31, 47),
#         ]
#
#         cursor.executemany(sql, dados)
#
#         conexao.commit()


                                                #REMOVENDO

# #No exemplo abaixo apagando em nossa tabela clientes um cliente de cada vez
# with conecta() as conexao: #Após inserimos nossa conexão dentro do metod conecta afim de podermos usar o gerenciador
#     #de contexto para abrir e fechar a conexão, sempre que precisarmos acessar e manipular o BD, basta colocar tudo dentro
#     #dessa estrutura que a conexão e o cursor serão fechados automaticamente
#     with conexao.cursor() as cursor:                               #essa barra serve apenas para pula de linha
#         sql = 'DELETE FROM clientes WHERE ID = %s'
#         cursor.execute(sql, (6,)) #lembrando que precisa da virgula por se tratar de tupla (x,y)
#         conexao.commit()




# #No exemplo abaixo apagando em nossa tabela clientes varios clientes de uma vez
# with conecta() as conexao: #Após inserimos nossa conexão dentro do metod conecta afim de podermos usar o gerenciador
#     #de contexto para abrir e fechar a conexão, sempre que precisarmos acessar e manipular o BD, basta colocar tudo dentro
#     #dessa estrutura que a conexão e o cursor serão fechados automaticamente
#     with conexao.cursor() as cursor:                               #essa barra serve apenas para pula de linha
#         sql = 'DELETE FROM clientes WHERE ID IN (%s, %s, %s)'
#         cursor.execute(sql, (7, 8, 9)) #lembrando que precisa da virgula por se tratar de tupla (x,y)
#         conexao.commit()


                                                #ATUALIZANDO

# #No exemplo abaixo atualizando em nossa tabela clientes um cliente
# with conecta() as conexao: #Após inserimos nossa conexão dentro do metod conecta afim de podermos usar o gerenciador
#     #de contexto para abrir e fechar a conexão, sempre que precisarmos acessar e manipular o BD, basta colocar tudo dentro
#     #dessa estrutura que a conexão e o cursor serão fechados automaticamente
#     with conexao.cursor() as cursor:                               #essa barra serve apenas para pula de linha
#         sql = 'UPDATE clientes SET nome=%s WHERE id=%s'
#         cursor.execute(sql, ('Maxintindoievisque', 12)) #lembrando que precisa da virgula por se tratar de tupla (x,y)
#         conexao.commit()





                                    #APENAS SELECIONANDO (IMPRIMINDO)

with conecta() as conexao: # Lembrando que, sempre que vc abre uma conexão e um cursor, precisa fechar ao final
        # de seu codigo.
    with conexao.cursor() as cursor: #Aqui nós estamos usando o gerenciador de contexto para fechar o cursor, mas ainda sim somos
        # obrigados a fechar a conexão, por isso colocamos nossa conexão dentro do metodo conecta acima, e sem seguida,
        #usanmos um gerenciador de cotexto with para a conexão
        cursor.execute('SELECT * FROM clientes')
        resultado = cursor.fetchall()

        for linha in resultado:
            # print(linha) #A cada linha será um dicionario e a cada chave, o nome da coluna:
            # #ex: {'id': 1, 'nome': 'Luiz', 'sobrenome': 'Otávio', 'idade': 20, 'peso': 100.0}

            print(linha['nome'], linha['idade']) #imprimindo o nome e a idade passando os nomes de suas respectivas chaves
            #do dicionario






# conexao.close() #Se eu não colocasse a conexão dentro do metodo conecta, eu poderia usar apenas o gerenciador do cursor
# #acima, apagar o gerenciador da conexão, mas ai eu precisaria fechar a conexão do banco ao final do codigo


# with conecta() as conexao: #Após inserimos nossa conexão dentro do metod conecta afim de podermos usar o gerenciador
#     #de contexto para abrir e fechar a conexão, sempre que precisarmos acessar e manipular o BD, basta colocar tudo dentro
#     #dessa estrutura que a conexão e o cursor serão fechados automaticamente
#     with conexao.cursor() as cursor:
#         pass
