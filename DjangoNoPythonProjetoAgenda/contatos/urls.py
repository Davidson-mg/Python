from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('<busca/', views.busca, name='busca'), #Quando efetuarmos uma busca na barra de busca, ele vai carregar na
    #url busca/ seguido de termo=maria+martins
    path('<int:contato_id>', views.ver_contato, name='ver_contato') #O primeiro parametro, estamos dizendo
    #vai receber um valor int, que o valor do id do contato e ele vai fazer referencia a pagina ver_contato.
    #Ele será passado como parametro no arquivo de views no metodo ver_contato.
    #o terceiro parametro estamoos definindo o nome da url.

]