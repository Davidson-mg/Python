def soma (x: float, y:float) -> float:
    return x+y

print(__name__) #Vai imprimir: print(__name__). Porém, se eu apenas executar um outro aquivo vazio, mas com
#o import deste arquivo, lá vai imprimir 'modelo130'

if __name__ == '__main__': #Isso permite eu criar codigos de teste das nessa propria classe e, quando eu for executar
    #este arquivo em outro arquivo, tudo que estiver dentro deste if não será executad lá
    print(soma(10, 20))
    print(soma(20, 45))
