from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView
from django.views.generic import View, DetailView
from django.http import HttpResponse
from django.contrib import messages
from produto.models import Variacao
from utils import utils
from .models import ItemPedido, Pedido


class DispatchLoginRequiredMixin(View): #Essa classe terá o objetivo apenas de impedir que um usuario anonimo consiga
    #acessar um pedido de um cliente via url.
    def dispatch(self, *args, **kwargs): #Esse metodo dispatch pertence a classe View e têm o objetivo de
    #definir pra onde uma pagina deve ir, tipo, se está indo pro post, pra get e etc. Vamos interferir nele para impedir
    #que usuarios não autenticados possam ir para pagina de pedidos, sendo direcionados para pagina de criar perfil.
    #Para funcionar, será necessario também usar essa classe DispatchLoginRequired como herança na classe responsavel
    #por pagar pedido, neste caso, a classe Pagar abaixo vai recebe-la como herança

        if not self.request.user.is_authenticated:
            return redirect('perfil:criar')
        return super().dispatch(*args, **kwargs)



    #Digamos que com um usuario eu crie um pedido e pegue o id deste pedido na url e cole num nevegador que está logado
    #com outro usuario. Este segundo usuario vai conseguir acessar este pedido do primeiro usuario, e isso é um problema
    # que vamos resolver abaixo
    def get_queryset(self, *args, **kwargs): #Este metodo vem da classe DetailView do Django
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(usuario=self.request.user) #vamos filtrar a consulta considerando apenas o usuario logado
        return qs






class Pagar(DispatchLoginRequiredMixin, DetailView): #repare que também estamos herdando da classe DispatchLoginRequiredMixin
    #acima. Lembrando também que em caso de herança dupla, precisa ser passado na ordem. Neste caso o metodo dispatch
    #será sobrescrito também na classe DetailView

    template_name = 'pedido/pagar.html'
    model = Pedido
    pk_url_kwarg = 'pk' #variavel generica do django que pega o que vem na url. Neste caso, vamos pegar o que foi passado
    #ao final da classe SalvarPedido abaixo. Lembrando também que no arquivo url produto, a url está preparada para
    #receber o id path('pagar/<int:pk>', views.Pagar.as_view(), name='pagar'),

    context_object_name = 'pedido'




class SalvarPedido(View):

    template_name = 'pedido/pagar.html'
    def get(self, *args, **kwargs):

        if not self.request.user.is_authenticated:
            messages.error(self.request, 'Você precisa fazer login')
            return redirect('perfil:criar')

        if not self.request.session.get('carrinho'): #verificando se existe algum produto no carrinho
            messages.error(self.request, 'Carrinho vazio.')
            return redirect('produtos:lista')

        #Digamos que o usario montou seu carrinho de compras mas desistiu de comprar. Depois de alguns dias ele
        #acessa o site e, ao perceber que o carrinho ainda está lá, ele resolver finalizar a comprar. Precisamos
        #verificar se depois destes dias ainda temos a qtd de produto em estoque

        carrinho = self.request.session.get('carrinho') #pegando na sessão atual o carrinho de comprar atual

        carrinho_variacao_ids = [v for v in carrinho] #Vamos pegar os ids das variações. Lembrando que neste caso
        #os ids são a chaves pois nosso carrinho é um diconario. Vamos percorrer o carrinho pegando os ids

        #print(carrinho) #Vai imprir algo assim ['1', '3', '8'], que são os ids das variações

        bd_variacoes = list(Variacao.objects.select_related('produto').filter(id__in=carrinho_variacao_ids)) #vamos selecionar
        # todas as variações correpondentes aos ids armazenados na variavel carrinho_variacao_ids no banco de dados e
        # armazenar na variavel bd_variacoes. Além disso, estamos convertendo para lista. O select_related não é
        # obrigatorio mas recomendavel pois por meio dele estamos especificando o tipo de objeto que queremos na
        # consulta. Ou seja, ele vai reduzir a qtd de consulta no BD para trazer o que queremos

        for variacao in bd_variacoes: #vamos percorrer todos os produtos armazenados na variavel bd_variacoes

            vid = str(variacao.id) #estamos armazenando o id da variação atual. Precisa ser uma string pois estamos
            #usando a chave como string. Poderia ter feito diretamente nas variaveis abaixo, mas para ficar mais
            #curta as linhas pegamos a vid separada

            estoque = variacao.estoque #armazenando o estoque da variação atual
            qtd_carrinho = carrinho[vid]['quantidade'] #selecionando o atributo quantidade da variação do id vid.
            #dicionario, {'chave': atributo}
            preco_unt = carrinho[vid]['preco_unitario']
            preco_unt_promo = carrinho[vid]['preco_unitario_promocional']

            #Se a qtd do carrinho for maior que a qtd de estoque, não vamos proibir a compra quando o cliente clicar
            #em comprar, vamos apenas reduzir a qtd daquele produto/variação no carrinho e recalcular os valores
            #unitarios e promocionais de acordo com a qtd de produto em estoque, e por fim, deixar a msg para o cliente
            #falando que o estoque foi reduzido e falando para ele verificar ou comprar de acordo com as alterações
            #feitas no carrinho por conta da redução de estoque

            error_msg_estoque = ''

            if estoque < qtd_carrinho: #se nosso estoque é menor que a qtd no carrinho
                carrinho[vid]['quantidade'] = estoque #Vamos reduzir a qtd do carrinho para igual a qtd do estoque
                carrinho[vid]['preco_quantitativo'] = estoque * preco_unt #Recalculando o valor total unitario de acordo
                #com o novo estoque. Faremos o mesmo abaixo para o valor total promocional
                carrinho[vid]['preco_quantitativo_promocional'] = estoque * preco_unt_promo

                #Se ntou no if é pq teve erro. Se teve erro, armazena essa msg
                error_msg_estoque= 'Você demorou de mais para comprar e o nosso estoque foi reduzido neste meio ' \
                                   'tempo. Caso queira continuar a compra, já reduzimos para você a quantidade' \
                                    'de produtos em seu carrinho de acordo com a quantidade em estoque atual.'

            if error_msg_estoque:
                messages.error(self.request, error_msg_estoque)

                self.request.session.save()#salvando a sessão com suas alterações
                return redirect('produto:carrinho')


        #Daqui para baixo vamos salvar nosso pedido no bd. Os pedidos estrão disponiveis na tela de admin do Django

        qtd_total_carrinho = utils.cart_total_qtd(carrinho) # Lembrando que cart_total_qtd é uma função que criamos no
        # arquivo utils/utils.py para somar a quantidade de todos os produtos

        valor_total_carrinho = utils.cart_totals(carrinho) # Lembrando que cart_totals é uma função que criamos no
        # arquivo utils/utils.py para somar os valores de todos o itens no carrinho

        pedido = Pedido( #Variavel pedido vai receber o obj da classe pedido já definindo os valores dos atributos
            # da classe Pedido com os valores que coletamos até aqui.
            usuario=self.request.user,
            total=valor_total_carrinho,
            qtd_total=qtd_total_carrinho,
            status='C', #Lembrando que definimos status no models Pedido como um atributo charfield, porém com opção de
            # escolha. O 'C' neste caso é referente a Criado. Ou seja, status atual é criado

        )

        pedido.save() #vamos salvar o pedido e depois abaixo, vamos inserir neste pedido os itens. Lembrando que
        #ItemPedido possui uma relação com pedido lá em models. Dentro de ItemPedido temos um atributo FK pedido

        ItemPedido.objects.bulk_create( #O bulk_create serve para inserir uma grande quantidade de dados num banco de
            # forma super rápida. É um metodo generico do Django. Lembrando que ItemPedido é um models e estamos
            #inserindo nessa classe (obj) os itens que estão neste momento no carrinho. Estamos criando varios objetos
            [
                ItemPedido( #vamos inserir item por item. Cada item possui os atributos abaixo
                    pedido=pedido,
                    produto=v['produto_nome'],
                    produto_id=v['produto_id'],
                    variacao=v['variacao_nome'],
                    variacao_id=v['variacao_id'],
                    preco=v['preco_quantitativo'],
                    preco_promocional=v['preco_quantitativo_promocional'],
                    quantidade=v['quantidade'],
                    imagem=v['imagem'],
                )for v in carrinho.values() #percorrendo o carrinho e selecionando cada item do carrinho
            ]
        )

        contexto = {
            'qtd_total_carrinho': qtd_total_carrinho,
            'valor_total_carrinho': valor_total_carrinho,
        }

        del self.request.session['carrinho'] #uma vez que o cliente confirmou o pedido, vamos eliminar o carrinho pra
        #garantir que ele não vai comprar duas vezes o mesmo carrinho

        # return render(self.request, self.template_name, contexto)

        return redirect(reverse('pedido:pagar', kwargs={'pk':pedido.pk }))

class Detalhe(DispatchLoginRequiredMixin, DetailView):
    model = Pedido
    context_object_name = 'pedido'
    template_name = 'pedido/detalhe.html'
    pk_url_kwarg = 'pk'


class Lista(DispatchLoginRequiredMixin, ListView):
    model = Pedido
    context_object_name = 'pedidos'
    template_name = 'pedido/lista.html'
    paginate_by = 10
    ordering = ['-id'] #ordenando de forma decrescente