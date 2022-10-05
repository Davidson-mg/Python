from django.contrib import admin
from . models import Tarefa

class ListaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'data_inclusao', 'previsao_conclusao', 'observacao', 'status')
    list_display_links = ('id', 'nome')

admin.site.register(Tarefa, ListaAdmin)
