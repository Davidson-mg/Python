from django.contrib import admin
from . import models

class VariacaoInline(admin.TabularInline): #Aqui estamos criando uma classe que vai nos possibilitar exibir, criar e
    # editar outra classe model. Por exemplo, a classe produto têm sua classe correpondente variação de cada produto
    # Digamos que eu adicione um produto camisa, este produto possui suas variações, tipo, tamanho, valor promocional
    #cor e etc. Então, sempre que eu adicionar um novo produto na tela de admin, será aberto uma tela com os atributos
    #do produto e os atributos da variação do produto

    model = models.Variacao #estamos escolhendo qual classe que poderá ser editada/acessada, neste caso, classe Variacao
    extra = 1 #A cada produto que eu adicionar, quantas variações para criação serão mostradas a principio. Neste caso
    #uma apenas






class ProdutoAdmin(admin.ModelAdmin): #essa é a classe que definimos os campos na tela de admin. Tipo, quais campos
    #eu poderia clicar para abrir a tela de edição, quais campos eu poderia editar sem abrir a tela de edição, quais
    #campos seriam exibidos sem abrir a tela de edição e etc.

    list_display = ['nome', 'descricao_curta', 'get_preco_formatado', 'get_preco_promocional']
    #get_preco_formatado estamos trocando pelo o que seria o atributo de models preco_marketing e get_preco_promocional
    # estamos trocando pelo que seria o atributo preco_marketing_promocional. São um metodos que criamos no arquivo de
    # models para formatar o valor do preço e preço promocional

    inlines = [VariacaoInline]#Estamos definindo a classe acima que possibilitar criamos variações dentro de produto





admin.site.register(models.Produto, ProdutoAdmin) #aqui estamos registrando a classe produto e produto admin para serem
#disponibilizados na tela de admin

admin.site.register(models.Variacao)
