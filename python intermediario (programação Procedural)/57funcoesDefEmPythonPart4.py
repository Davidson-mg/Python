variavel = 'valor'
def func():
    print(variavel)

def func2():
    global variavel #a palavra global serve para possibilitar a alteração de uma variavel local no escopo local. OBS: Não é uma boa pratica
    print(variavel)

func()
func2()