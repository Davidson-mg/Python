import os #este mododulo acessa arquivos

#Sempre que precisar trabalhar com barras invertidas, use o 'r' antes da string
caminhoProcura = r'C:\Users\David\Documents\testePython' #variavel que receber o caminho da pasta onde queresmos
#pesquisar ou percorrer afim de listar todos os arquivos dela

termoProcura = 'Triste'

def formataTamanho (tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if tamanho < kilo:
        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'K'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'M'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'G'
    elif tamanho < peta:
        tamanho /= tera
        texto = 'T'
    else:
        tamanho /= peta
        texto = 'P'

    tamanho = round(tamanho, 2)
    return f'{tamanho}{texto}'



conta = 0
for raiz, diretorios, arquivos in os.walk(caminhoProcura): #Com os 3 parametros do metodos 'os.walk', estou dizendo que
    #raiz: a pasta que estamos verificando no momento
    #diretorios: são os diretorios ou subdiretorios dentro da minha pasta raiz
    #arquivos: São os arquivos dentro da pasta raiz e dentro dos demais diretorios dentro da pasta raiz

    for arquivo in arquivos: #No for acima, estamos recebendo uma lista, e dentro da lista, temos  lista raiz, diretorios,
        #e arquivos. Por isso este segundo for que vai percorrer somente os arquivos. Lembrando que aqui serão
        #os aquivos que estão dentro da pasta raiz e os arquivos que estão dentro de pastas (diretorios) dentro da pasta raiz

        if termoProcura in arquivo:
            try:
                conta += 1;
                caminhoCompleto = os.path.join(raiz, arquivo)  #Com o metodo 'os.path.join' estamos pegando o caminho completo do arquivo
                #print(caminhoCompleto, )  # Ex: C:/Users/David/Documents/backing track praia.mp4

                nomeArquivo, extArquivo = os.path.splitext(caminhoCompleto) #Com o metodo 'os.path.splitext' (é uma tupla), vai
                #desempacotar nas variaveis 'nomeArquivo' e 'extArquivo' os nomes dos arquivos e suas extensões respectivamente
                #print(nomeArquivo, extArquivo) #ex: C:/Users/David/Documents/backing track praia .mp4

                tamanho = os.path.getsize(caminhoCompleto) #Com o metodo os.path.getsize vou pegar o tamanho de todos os arquivos
                # print(tamanho) #Ex: 516562403

                print()
                print('Encontrei o arquivo: ', arquivo)
                print('Caminho: ', caminhoCompleto)
                print('Nome: ', nomeArquivo)
                print('Extensão: ', extArquivo)
                print('Tamanho: ', formataTamanho(tamanho))
            except PermissionError as e:
                print('Sem premissões')
            except FileNotFoundError as e:
                print('Arquivo não encontrado')
            except Exception as e:
                print('Erro desconhecido: ', e)

print()
print(f'{conta} arquivo(s) encontrados(s)')