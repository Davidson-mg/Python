class TaErradoError(Exception):
    pass

def testar():
    raise TaErradoError('Errado!')

try:
    testar()
except TaErradoError as e:
    print(f'Erro: {e}')