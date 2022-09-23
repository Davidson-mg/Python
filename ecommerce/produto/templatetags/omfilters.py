from django.template import Library
from utils import utils #Esse utils fomos nós que criamos para colocar algumas funções que serão reutilizadas

register = Library() #Sempre que criamos um arquivo com funções que terão seus valores utilizados nos arqivos index,
#nós precisamos registrar este arquivo importando Library e registrando essa variavel no arquivo e as funções deste
#arquivo


@register.filter #registrando a função no django
def formata_preco (val):  #metodo para formatar o valores de preco, colocando o R$, substituindo '.' por ','
        #e permitindo apenas duas casas decimais. No arquivo de admin, em list_display, onde vc colocaria o atributo
        #preco_marketing, vc coloca agora o metodo get_preco_formatado

        #Nós já fizemos um metodo como este para formatar valores no arquivo models de produto, porém, naquele caso
        #era para formatar para a tela de admin. Aqui, nós vamos receber as variaveis vindo do arquivo index e retorna-las
        #formatadas.

    return utils.formata_preco(val) #Repare que ao inves de escrever aqui a função, nós estamos chamando a função que foi
    #escrita no arquivo utils dentro da pasta utils. Isso pq vamos reutilizar essa função outras vezes e não
    #queremos ficar rescrevendo ela varias vezes