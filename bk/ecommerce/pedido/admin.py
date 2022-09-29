from django.contrib import admin
from . import models

class ItemPedidoInline(admin.TabularInline): #Aqui estamos criando uma classe que vai nos possibilitar exibir, criar e
    # editar outra classe model dentro de admin. Por exemplo, a classe produto têm sua classe correpondente variação de
    # cada produto Digamos que eu adicione um produto camisa, este produto possui suas variações, tipo, tamanho, valor
    # promocional cor e etc. Então, sempre que eu adicionar um novo produto na tela de admin, será aberto uma tela com
    # os atributos do produto e os atributos da variação do produto

    model =  models.ItemPedido #estamos escolhendo qual classe que poderá ser editada/acessada, neste caso, classe ItemPedido
    extra = 1 #A cada pedido que eu adicionar, quantos itens para criação serão mostradas a principio. Neste caso
    #uma apenas

class PedidoAdmin(admin.ModelAdmin):
    inlines = [
        ItemPedidoInline
    ]

admin.site.register(models.Pedido, PedidoAdmin)
admin.site.register(models.ItemPedido, )
