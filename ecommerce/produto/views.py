from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import ListView
from django.views.generic import View
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from . import models
from django.contrib import messages
from pprint import pprint
from perfil.models import Perfil



class ListaProdutos(ListView):

    model = models.Produto

    template_name = 'produto/Lista.html' #Estou defindo o nome do meu template. Lembrando que, por padrão, o django
    #produra por um template com o nome do models seguido de list (neste caso seria produto_list). Porém, como esse não
    #é o nome do nosso template, utilizamos a variavel generica do django template_name

    context_object_name = 'produtos' #Apenas nomeando nosso contexto. Variavel generica do Django

    paginate_by = 10 #definindo a qtd de produtos por pagina. Lembrando que paginate_by é uma variavel generica do django
    #e define pra gente essa questão de elementos por pagina automaticamente





class DetalheProduto(DetailView):
    model = models.Produto
    template_name = 'produto/detalhe.html' #Estou defindo o nome do meu template. Lembrando que, por padrão, o django
    #produra por um template com o nome do models seguido de list (neste caso seria produto_list). Porém, como esse não
    #é o nome do nosso template, utilizamos a variavel generica do django template_name

    context_object_name = 'produto' #Apenas nomeando nosso contexto. Variavel generica do Django

    slug_url_Kwarg = 'slug' #Usando esta variavel generica do django para pegar slug. Essa string slug é a mesma que
    #vai na url no arquivo urls no path deste view em '<slug>'

    #Até este ponto, já conseguimos direcionar para a pagina do produto, sendo possivel até imprimir os atributos do
    #produto utilizando {{ produto.NomeDoAtributo }}







class AdicionarAoCarrinho(View):

    #Quando dentro do produto nós clicamos em adicionar carrinho, esse btn de adicionar carrinho está dentro de um form
    #Um formulario comum (por exemplo de cadastro), possui um method="POST"
    #Por padrão, um formulario que não possui method, faz get method="GET". Neste caso, o get vai pegar o id do produto
    # na url ao inves de postar (POST) como faria um formulario convencional. COmo não vamos usar o post, não vamos
    #definir o metodo post aqui na classe de adicionar carrinho

    def get(self, *args, **kwargs):

        #Este trecho comentado abaixo serviu apenas pra gente apagar o carrinho enquanto estamos desenvolvendo e testando
        # if self.request.session.get('carrinho'):
        #     del self.request.session['carrinho']
        #     self.request.session.save()

        http_referer = self.request.META.get('HTTP_REFERER', reverse('produto:lista')) #Toda essa linha depois do igual,
        # e referente a url anterior e vamos armazela-lo na variavel http_referer. Quando eu clicar no adicionar ao
        # carrinho, por meio dele nós vamos fazer o precesso de o produto recarregando a tela atual, sem carregar outra
        # pagina. Precisa dos imports redirect e reverse. Esse rever serve para caso a agente tente adicionar um
        #produto que não existe, digamos que digitando um vid inexistente na url, ele volta pra tela de produto
        # (produto:lista)

        variacao_id = self.request.GET.get('vid') #Esse vid é um nome dado pelo proprio django para a variavel que
        #recebe a variação do produto. Se não houver variação, não existe o vid e será armazenado none

        if not variacao_id:
            messages.error(self.request, 'Produto não existe')
            return redirect(http_referer)


        variacao = get_object_or_404(models.Variacao, id=variacao_id) #lembrando que o get_object_or_404 obtem o obj
        #erro 404, poupando a necessidade de fazer um try. Aqui vamos selecionar especificamente a variação que o
        #cliente está comprando

        #Aqui precisamos falar sobre cookies. São dados relacionados ao acesso do cliente e que são armazenados no
        # computador ou dispositivo do cliente.
        #Sessões são semlhantes aos cookies só que salvo no lado do servidor. Digamos que o cliente adiciona alguns
        #produtos no carrinho mas não compra. Nós definimos no aquivo settings em 'SESSION_COOKIE_AGE' quanto tempo dura
        #uma sessão, neste caso até 7 dias. Quer dizer os produtos do carrinho ficaram disponiveis por 7 dias, mesmo
        #que o cliente desligue o pc e etc. Além disso, o Django vai sarvar os dados da sessão numa base de dados e não
        #num arquivo

        variacao_estoque = variacao.estoque #armazenando o estoque na variavel
        produto = variacao.produto #A variação produto vai receber a variação do produto, ou seja, todos os seus
        #atributos abaixo. Lembrando que variacao.produto é uma PK dentro de variação que faz relacionamento com
        #Produto

        produto_id = produto.id
        produto_nome = produto.nome
        variacao_nome = variacao.nome or ''
        preco_unitario = variacao.preco
        preco_unitario_promocional = variacao.preco_promocional
        quantidade = 1
        slug = produto.slug
        imagem = produto.imagem

        if imagem: #imagem recebeu produto.imagem acima. Como não é obrigatorio inserir a imagem, temos que verificar
            #se ela existe. Caso não exista, é necessario que retorne vazio
            imagem = imagem.name
        else:
            imagem = ''


        if variacao.estoque < 1: #verificando se existe pelo menos uma qtd daquela variação daquele produto em estoque
            messages.error(self.request, 'Estoque insuficiente')
            return redirect(http_referer) #Lembrando que http_referer é uma variavel que recebe a url da pagina anterior
            #ou atual no caso

        if not self.request.session.get('carrinho'): #será nossa primeira verificação sobre carrinho. Vamos verificar
            #se existe uma chave de sessão, carrinho. Chaves pq sessões são dicionaarios
            self.request.session['carrinho'] = {} #vamos criar uma chave carrinho que não existe na sessão
            self.request.session.save()#salvando nossa chave carrinho criada na sessão do usuario. Lembrando que
            #o usario precisa estar logado para adicionar e estamos usando metodos e variaveis generica do django que
            # fazem tudo isso automaticamente pra gente

            #Ilustrando
            # sessão = { {carrinho: }, {... : ...}, {... : ...} }

        carrinho = self.request.session['carrinho'] #Armazenando a chave carrinho que criamos acima na variavel carrinho



        #A partir de agora temos um dicionario sessão com um dicionario (que é uma chave) carrinho dentro.


        if variacao_id in carrinho: #se id da variação do produto que selecionamos existe na chave do carrinho da sessão
            #, ou seja, se este produto já foi adicionado no carrinho em outro momento

            quantidade_carrinho = carrinho[variacao_id]['quantidade'] #estamos pegando q QTD que esta na chave
            #variacao_id
            quantidade_carrinho += 1 #Estamos adicionando mais um produto na quantidade do carrinho

            if variacao_estoque < quantidade_carrinho: #verificando se temos aa quantidade da variação do produto
                #adicionado pelo cliente no nosso estoque
                messages.warning(self.request, f'Estoque insuficiente para {quantidade_carrinho}x no produto '
                                               f'"{produto_nome}". Adicionamos a {variacao_estoque}x no seu carrinho.')
                quantidade_carrinho = variacao_estoque #Adicionando a o estoque da variação no carrinho

            carrinho[variacao_id]['quantidade'] = quantidade_carrinho
            carrinho[variacao_id]['preco_quantitativo'] = preco_unitario * quantidade_carrinho
            carrinho[variacao_id]['preco_quantitativo_promocional'] = preco_unitario_promocional * quantidade_carrinho


        else: #Caso o produto não exista no carrinho
            carrinho[variacao_id] = { #variacao_id é a chave de um produto. Estamos inserindo no dicionario todas
                #as chaves que correspondem aos atributos do produto e seus respectivos valores

                #Ilustrando
                # sessão = { {carrinho:{ {variacao_id: id}, {'produto' : variacao.produto,}, {'produto' : variacao.produto,}}, {... : ...}, {... : ...} }

                'produto_id' : produto_id, #lembrando que essas variaveis do produto foram declaradas acima
                'produto_nome' : produto_nome,
                'variacao_nome' : variacao_nome,
                'variacao_id' : variacao_id,
                'preco_unitario' : preco_unitario,
                'preco_unitario_promocional' : preco_unitario_promocional,
                'preco_quantitativo': preco_unitario,
                'preco_quantitativo_promocional': preco_unitario_promocional,
                'quantidade': 1,
                'slug': slug,
                'imagem': imagem,

            }

        #Ilustrando o resultado
        #Tudo isso abaixo é o carrinho. 4 é a variação
        # {4: {'imagem': 'produto_imagens/2022/09/download_1.jpg',
        #      'preco_quantitativo': 2500.0,
        #      'preco_quantitativo_promocional': 500.0,
        #      'preco_unitario': 2500.0,
        #      'preco_unitario_promocional': 500.0,
        #      'produto_id': 2,
        #      'produto_nome': 'Notebook Gamer Pentium mmx',
        #      'quantidade': 1,
        #      'slug': 'notebook-gamer-pentium-mmx',
        #      'variacao_id': 4,
        #      'variacao_nome': 'Sem SSD'}
        #      }

        self.request.session.save()
        #pprint(carrinho) serve apenas para printar a ilustração acima e testar

        messages.success(self.request, f'Produto {produto_nome}{variacao_nome} adicionado ao seu carrinho '
                                       f'{carrinho[variacao_id]["quantidade"]}x.')

        return redirect(http_referer)




class RemoverDoCarrinho(View):

    def get(self, *args, **kwargs):
        http_referer = self.request.META.get('HTTP_REFERER', reverse('produto:lista'))

        variacao_id = self.request.GET.get('vid')

        if not variacao_id:
            return redirect(http_referer)

        if not self.request.session.get('carrinho'):
            return redirect(http_referer)

        if variacao_id not in self.request.session['carrinho']:
            return redirect(http_referer)

        carrinho = self.request.session['carrinho'][variacao_id]

        messages.success(
            self.request, f'Produto {carrinho["produto_nome"]} {carrinho["variacao_nome"]} removido do seu carrinho.'
        )

        del self.request.session['carrinho'][variacao_id]
        self.request.session.save()

        return redirect(http_referer)



class Carrinho(View):
    def get(self, *args, **kwargs):
        contexto = {'carrinho': self.request.session.get('carrinho', {})}
        return render(self.request, 'produto/carrinho.html', contexto)


class ResumoDaCompra(View):
    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated: #impedindo que usuarios não autencicado chegue na tela de resumo de
            #compra
            return redirect('perfil:criar')

        perfil = Perfil.objects.filter(usuario=self.request.user).exists()

        if not perfil:
            messages.error(self.request, "Usuário sem perfil.")
            return redirect('perfil:criar')

        if not self.request.session.get('carrinho'):
            messages.error(self.request, 'Carrinho vazio.')
            return redirect('produto:lista')

        contexto = {
            'usuario': self.request.user,
            'carrinho': self.request.session['carrinho'],
        }
        return render(self.request, 'produto/resumodacompra.html', contexto)
