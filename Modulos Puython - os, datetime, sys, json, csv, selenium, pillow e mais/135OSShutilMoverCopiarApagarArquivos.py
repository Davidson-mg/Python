import os #este mododulo acessa arquivos
import shutil #este modulos manipula arquivos

caminhoOriginal = r'C:/Users/David/Documents/testePython'
caminhoNovo = 'C:/Users/David/Documents/testePython2'

try:
    os.mkdir(caminhoNovo) #Vamos criar uma pasta nova
except FileExistsError as e:
    print(f'Pasta {caminhoNovo} já existe')


    #Neste exemplo vamos criar uma nova pasta e mover, copiar e apagar para ela arquivos de oustra pasta

for raiz, diretorio, arquivos in os.walk(caminhoOriginal):#Com os 3 parametros do metodos 'os.walk', estou dizendo que
    #raiz: a pasta que estamos verificando no momento
    #diretorios: são os diretorios ou subdiretorios dentro da minha pasta raiz
    #arquivos: São os arquivos dentro da pasta raiz e dentro dos demais diretorios dentro da pasta raiz


    for arquivo in arquivos: #No for acima, estamos recebendo uma lista, e dentro da lista, temos  lista raiz, diretorios,
        #e arquivos. Por isso este segundo for que vai percorrer somente os arquivos. Lembrando que aqui serão
        #os aquivos que estão dentro da pasta raiz e os arquivos que estão dentro de pastas (diretorios) dentro da pasta raiz


        antigoCaminhoArquivo = os.path.join(raiz, arquivo)#Com o metodo 'os.path.join' estamos pegando o caminho completo do arquivo
        #print(caminhoCompleto, )  # Ex: C:/Users/David/Documents/backing track praia.mp4. Vamos pegar de todos os arquivos da pasta
        #caminhoOriginal, que a pasta que estamos percorrendo no for acima


        novoCaminhoArquivo = os.path.join(caminhoNovo, arquivo) #Com o metodo 'os.path.join' estamos pegando o caminho completo do arquivo
        #porém, agora será o caminho da nova pasta juntamente com o arquivo.
        #print(caminhoCompleto, )  # Ex: C:/Users/David/Documents/backing track praia.mp4


        # if '.jpg' in arquivo: #Quero copiar apenas os arquivos que tenha .jpg
        #     shutil.copy(antigoCaminhoArquivo, novoCaminhoArquivo) #Estamos movendo todos os arquivos de uma pasta para outra
        #     print(f'Arquivo {arquivo} copiado com sucesso!')

        #Se eu quisesse apenas mover, seria assim. Repare que é igual o exemplo de copiar acima, só mudando copy por move
        # shutil.move(antigoCaminhoArquivo, novoCaminhoArquivo) #Estamos movendo todos os arquivos de uma pasta para outra
        # print(f'Arquivo {arquivo} movido com sucesso!')
        

        if '.jpg' in arquivo: #Da forma como construimos nosso codigo, estamos apagando os arquivos da nova pasta, e não da pasta antiga
            os.remove(novoCaminhoArquivo)
            print(f'Arquivo {arquivo} removido com sucesso!')

