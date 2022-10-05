from django.urls import path
from . import views

app_name = 'principal'

urlpatterns = [
    path('', views.index, name='index'),
    path('listadetarefas/', views.ListaDeTarefas.as_view(), name='listadetarefas'),
    path('adicionartarefa/', views.adicionarTarefa, name='adicionartarefa'),
    path('<int:tarefa_id>', views.excluir, name='excluir'),
    path('detalhes/<int:id>', views.Detalhes.as_view(), name='detalhes'),
]


