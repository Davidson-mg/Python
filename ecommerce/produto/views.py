from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import View
from django.http import HttpResponse
from . import models
class ListaProdutos(ListView):
    model = models.Produto

    template_name = 'produto/Lista.html' #Estou defindo o nome do meu template. Lembrando que, por padrão, o django
    #produra por um template com o nome do models seguido de list (neste caso seria produto_list). Porém, como esse não
    #é o nome do nosso template, utilizamos a variavel generica do django template_name

    context_object_name = 'produtos' #Apenas nomeando nosso contexto

    paginate_by = 10 #definindo a qtd de produtos por pagina. Lembrando que paginate_by é uma variavel generica do django
    #e define pra gente essa questão de elementos por pagina automaticamente









class DetalheProduto(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Detalhe')

class AdicionarAoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Adicionar carrinho')

class RemoverDoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Remover carrinho')

class Carrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Carrinho')

class Finalizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Finalizar')
