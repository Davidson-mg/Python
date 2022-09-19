from enum import Enum, auto

class Direcoes(Enum):
    direita = auto()
    esquerda = auto()
    cima = auto()
    down = auto()



def move(direction):

    # if direction != 'direita' and direction != 'esquerda':
    #     raise ValueError('Não existe esta direção')

    if not isinstance(direction, Direcoes):
        raise ValueError('Não existe esta direção')

    return f'mova {direction.name}'

# if __name__ == '__main__':
#     print(move('direita'))
#     print(move('esquerda'))
#     print(move('Qualquer lugar'))

if __name__ == '__main__':
    print(move(Direcoes.direita))
    print(move(Direcoes.esquerda))


