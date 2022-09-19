
def converteNumero(valor):
    try: #Vai tentar converter o valor independente se é int, float ou string
        valor = int(valor) #se for int, vai converter, se não.....
        return valor
    except ValueError as erro: #se não consegui converter, digamos que o usuario digitou 'a'.
        try:
            valor = float(valor) #vai tentar converter para float
            return valor
        except ValueError: #Se não conseguir converter para int e nem pra float acima, vai retornar "None"
            pass

numero = converteNumero(input('Digite um numero: '))

if numero is not None: #Se o valor não é none
    print(numero*5)
else:
    print("Você está tentando multiplicar uma palavra")
