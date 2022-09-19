"""
Faça uma lista de tarefas com as seguintes opções:
    adicionar tarefa
    listar tarefas
    opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
    opção de refazer (a cada vez que chamarmos, refaz a última ação)
    ['Tarefa 1', 'Tarefa 2']
    ['Tarefa 1'] <- Desfazer
    ['Tarefa 1', 'Tarefa 2'] <- Refazer
    input <- Nova tarefa
"""



def addTarefa (tarefa):

    listaTarefas.append(tarefa)
    print()
    print('Lista de tarefas: ')
    print(listaTarefas)
    print()



def removeTarefa (listaBk, listaTarefas):


    if not listaTarefas: #Esta verificando se minha listaTarefas está vazia, se estiver, não a nada a remover

        print()
        print('Lista vazia')
        print()
        return

    ultimoRemovido = listaTarefas.pop() #O pop, quando combinado com outra variavel, não só remove da lista, como armazena nesta variavel
    listaBk.append(ultimoRemovido) #adicionando na minha lista de bk o elemento salvo em 'ultimoRemovido'. Dessa forma, toda vez que
    #seleciono a opção de remover, eu estou gerando uma lista com os elementos removidos na ordem correta

    print()
    print('Lista de tarefas: ')
    print(listaTarefas)
    print()

def refazerTarefa(listaBk, listaTarefas):

    if not listaBk: #Verificando se minha lista de BK está fazia. Se estiver, é pq não a nada a refazer. Se não a nada a refazer,
        #é pq nada foi removido, e se nada foi removido, nada foi inserido na minha lista de BK
        print()
        print('Lista de tarefas: ')
        print(listaTarefas)
        print('Nada a refazer')
        print()
        return

    ultimoRefazer = listaBk.pop() #O pop, quando combinado com outra variavel, não só remove da lista, como armazena nesta variavel
    listaTarefas.append(ultimoRefazer)#adicionando na minha lista de 'listaTarefas' o elemento salvo em 'ultimoRefazer'. Dessa forma, toda vez que
    #seleciono a opção de refazerTarefa, eu estou adicionando a lista 'listaTarefas' os elementos salvos na lista de BK

    print()
    print('Lista de tarefas: ')
    print(listaTarefas)
    print()



listaTarefas = []
listaBk = []

while True:
    print()
    print('1: Adicionar tarefa \n2: Remover tarefa \n3: Refazer tarefa \n4: sair')
    try:
        acao = int(input("Escolha uma das opções acima: " ))
        print()

        if acao < 1 or acao > 4:
            print('Opção invalida')
            continue

        if acao == 1:
            tarefa = input('Informe a nova tarefa: ')
            addTarefa(tarefa)
        if acao == 2:

            removeTarefa(listaBk, listaTarefas)

        if acao == 3:

            refazerTarefa(listaBk, listaTarefas)

        if acao == 4:
            break

    except ValueError as erro:
        print()
        print('Digite um valor numerico de 1 a 4.')
        print()
        print('Lista de tarefas: ')
        print(listaTarefas)
        print()

print()
print(listaTarefas)








