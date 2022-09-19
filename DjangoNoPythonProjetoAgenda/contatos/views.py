from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Contato
from django.core.paginator import Paginator #Nescessario este import para paginação
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages

def index(request):


    contatos = Contato.objects.order_by('-id').filter( #estamos ordenando por id de forma decrescente. Se seu quisesse
        #de forma crescente, bastaria remover o '-'
        mostrar=True #estamos filtrando de modo que mostre apenas os contatos que possue o atributo mostrar como verdadeiro (marcado)
    )

    #As proximas 3 linhas estão relacionadas a paginação. Tambémno arquivo index no for dentro do nav 'Page navigation example'
    paginator = Paginator(contatos, 10) #Estamos definindo que nossa pagina mostre apenas 10 contatos

    page = request.GET.get('p') #Vai pegar o numero da pagina na paginação
    contatos = paginator.get_page(page)

    return render(request, 'contatos/index.html', {'contatos': contatos}) #Estamos passando um dicionario
    #como parametro. Esse dicionario vai receber A classe Contato com parametro e possibilitar o uso dela
    #na pagina contatos/index.html. Verifique essa pagina para entender melhor


def ver_contato(request, contato_id): #o primeiro parametro do arquivo url de ver_contato é passado aqui
    contato = get_object_or_404(Contato, id=contato_id) # contato vai receber o ip de contato. Esse _or_404 é um
    #atalho para o exemplo feito com try abaixo comentado. Estamos tratando o erro de buscar por um contato de um id
    #que não existe (talvez tenha sido apagado), que é o erro 404. Se não tratassemos e buscassemos um id que não existe
    #retornaria erro 500, que é um erro relacionado ao servidor

    if not contato.mostrar: #Quando atributo mostrar do contato esta desmarcado, o contato não aparece na pagina, porém
        #é possivel digitar o id do contato na url e ele aparece. Esse if vai fazer essa verificação.
        #caso o usuario digite o id na url, mesmo que ele exista, caso atributo mostrar dele esteja desativado,
        #vai retornar o erro 404
        raise Http404()

    return render(request, 'contatos/ver_contato.html',
                  {'contato': contato})  # Vai retornar a pagin vercontato que esta no
    # arquivo contatos adicionando o numero de id na url



    # try:
    #     contato = Contato.objects.get(id=contato_id) #contato vai receber o ip de contato
    #     return render(request, 'contatos/ver_contato.html', {'contato': contato}) #Vai retornar a pagin vercontato que esta no
    #     #arquivo contatos adicionando o numero de id na url
    # except Contato.DoesNotExist as e:
    #     raise Http404()


#Esse metodo têm relação com o campos de busca. Lembrando que para busca, usarmos uma pagina que é copia da pagina
#onde está o campo de busca, neste caso, a pagina index
def busca(request):

    termo = request.GET.get('termo') #Essa variavel vai receber a string da variavel 'termo' lá no html refente ao
    #campo de busca na pagina 'base'

    if termo is None or not termo: #Se não digitar nada no campo de busca e der enter retorna, vai exibir uma msg
        #amigavel que personalizamos. Essa msg estamos captarando depois de no arquivo settings termos customizado nossa
        # msg com bootstrap na variavel 'MESSAGE_TAGS'. Essa msg será exibida uma ve e sumir automaticamente sem a gente
        # precisar fazer mais nada. A implementação disso contina no arquivo base.html e no arquivo parciais/_messagens
        messages.add_message(request, messages.ERROR, 'Campo termo não pode ficar vazio.')
        return redirect('index')

        # Essa msg estamos captarando depois de no arquivo
        # settings termos customizado nossas msg com bootstrap na variavel 'MESSAGE_TAGS'. Essa msg será exibida uma
        # e sumir automaticamente sem a gente precisar fazer mais nada. A implementação disso contina no arquivo base.html

    campos = Concat('nome', Value(' ') ,'sobrenome') #Vamos concatenar os atributos da base de dados separados por espaço.
    #como esse espço não existe no BD, usamos o Values para simular o espaço

    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(

        #o filter funciona como uma consulta sql. Abaixo, ustilizando o campo de filtro seria como se nossa colsulta
        #ficasse assim:
        # select nome from contatos where (nome like 'me' or sobrenome like 'me') and mostrar = true

        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo) #O __icontains estou dizendo que pode ser parcial
    )


    #Abaixo seria outra forma de efetuar a pesquisa, porém, dessa forma esbarra num problema, por isso está comentado.
    #Se vc digitasse nome OU sobrenome no campo de pesquisa, ele acharia, mas se digitasse nome E sobrenome no campo
    # de pesquisa, como os campos nome e sobrenome são separados no BD, ele não encontraria.


    # contatos = Contato.objects.order_by('-id').filter( #estamos ordenando por id de forma decrescente. Se seu quisesse
    #     #de forma crescente, bastaria remover o '-'. O filter é para filtrar conforme variaveis abaixo
    #
    #
    #     #o filter funciona como uma consulta sql. Abaixo, ustilizando o campo de filtro seria como se nossa colsulta
    #     #ficasse assim:
    #     # select nome from contatos where (nome like 'me' or sobrenome like 'me') and mostrar = true
    #
    #     #Abaixo esse Q com parentes e o caracter '|', funcionam como o 'or' no sql. Sem eles, a consulta seria com 3
    #     # 'ands'. Precisa do import 'Q'
    #     Q(nome__icontains=termo) | Q(sobrenome__icontains=termo),#vai filtrar pelo nome recebendo o valor da variavel termo. O __icontains estou dizendo
    #     #que pode ser o nome parcial.
    #     mostrar=True #estamos filtrando de modo que mostre apenas os contatos que possue o atributo mostrar como verdadeiro (marcado)
    # )

    #As proximas 3 linhas estão relacionadas a paginação. Tambémno arquivo index no for dentro do nav 'Page navigation example'
    paginator = Paginator(contatos, 10) #Estamos definindo que nossa pagina mostre apenas 10 contatos

    page = request.GET.get('p') #Vai pegar o numero da pagina na paginação
    contatos = paginator.get_page(page)

    return render(request, 'contatos/busca.html', {'contatos': contatos}) #Estamos passando um dicionario
    #como parametro. Esse dicionario vai receber A classe Contato com parametro e possibilitar o uso dela
    #na pagina contatos/index.html. Verifique essa pagina para entender melhor
