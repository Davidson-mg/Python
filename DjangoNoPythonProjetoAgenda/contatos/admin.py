from django.contrib import admin

from .models import Categoria, Contato

class ContatoAdmin(admin.ModelAdmin): #Nessa classe definimos os parametros da tela adimin do Django
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'data_criacao', 'categoria', 'mostrar') #Faz aparecer
    #os nomes dos campos na tela de administração do django nos contatos existentes
    list_display_links = ('id', 'nome', 'sobrenome') #Possibilita clicarmos nestes campos para abrir a tebela do contato
    #lá na tela de administração do django
    #list_filter = ('nome', 'sobrenome') #Vai adicionar estas opções de filtro na tela de admin do django
    lest_per_page = 10 #para que ele exiba apenas 10 contatos por filtro na tela de admin do django
    sarch_filds = ('nome', 'sobrenome', 'telefone') #Vai adicionar campos de pesquisa na tela de admin do django
    list_editable = ('telefone', 'mostrar') #vai habilitar o atributo mostrar lá do arquivo models na classe Contato

admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
