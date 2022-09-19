from django.urls import path
from . import views

urlpatterns = [
    #Estamos direcionado para a classe ao inves de direcionar para o arquivo html como feito no exemplo do projetoAgenda
    path('', views.PostIndex.as_view(), name='index'),
    path('categoria/<str:categoria>', views.PostCategoria.as_view(), name='post_categoria'),
    path('busca/', views.PostBusca.as_view(), name='post_busca'),
    path('post/<int:pk>', views.PostDetalhes.as_view(), name='post_detalhes'),

]