import random
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic.detail import DetailView, View
from django.views.generic import ListView, UpdateView
from .models import Tarefa, FormLista
from django.contrib import messages


class Index(ListView):

    model = Tarefa
    context_object_name = 'index'
    template_name = 'paginas/index.html'



class DispatchLoginRequiredMixin(View):

    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('accounts:login')

        return super().dispatch(*args, **kwargs)



class ListaDeTarefas(DispatchLoginRequiredMixin, ListView):

    def get(self, *args, **kwargs):
        Tarefa.usuario.primary_key = self.request.user.is_authenticated
        form = FormLista()
        tarefas = Tarefa.objects.filter(usuario=self.request.user)
        # tarefas = {'tarefas': self.request.session.get('tarefas',{})}
        self.model = Tarefa
        self.template_name = 'paginas/listadetarefas.html'

        return render(self.request, self.template_name, {'form': form, 'tarefas': tarefas})


def adicionarTarefa(request):

    http_referer = request.META.get('HTTP_REFERER')
    form = FormLista
    form = FormLista(request.user, request.POST, request.FILES)
    nome = request.POST.get('nome')

    iduser = request.user
    print(f'Id do usuario: {iduser}')

    if Tarefa.objects.filter(nome=nome, usuario=request.user).exists():
        messages.error(request, f'{nome} já existe na lista')
        return redirect(http_referer)

    numero = random.randrange(100, 999, 1)

    if Tarefa.objects.filter(codigo=numero, usuario=request.user).exists():
        while Tarefa.objects.filter(codigo=numero, usuario=request.user).exists():
            numero = random.randrange(100, 999, 1)

    object = form.save(commit=False) #Essas 2 linhas têm o objetivo pegar o usuario logado e inserir dentro do form
    object.usuario = request.user
    object.codigo = numero

    object.save()

    return redirect(http_referer)



def excluir(request, tarefa_id):
    http_referer = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        messages.success(request, 'Item removido com sucesso!')
        Tarefa.objects.filter(id=tarefa_id).delete()

    return redirect(http_referer)



class Detalhes(DispatchLoginRequiredMixin, DetailView):

    model = Tarefa
    context_object_name = 'tarefa'
    template_name = 'paginas/detalhes.html'
    pk_url_kwarg = 'id'



class EditarTarefa (DispatchLoginRequiredMixin, UpdateView):

    model = Tarefa
    template_name = 'paginas/editar.html'
    fields = ['nome', 'previsao_conclusao', 'observacao', 'status', 'descricao']
    exclude = ('codigo',)
    pk_url_kwarg = 'id'

    success_url = '/listadetarefas'

    def post(self, *args, **kwargs):

        object = self.get_object()
        id = object.pk

        nomeTarefa = self.request.POST.get('nome')

        if Tarefa.objects.filter(nome=nomeTarefa, id=id):
            messages.success(self.request, 'Tarefa atualizada com sucesso.')
            return super().post(self.request, *args, **kwargs)

        if Tarefa.objects.filter(nome=nomeTarefa).exists():
            http_referer = self.request.META.get('HTTP_REFERER')
            messages.error(self.request, f'Tarefa {nomeTarefa} já existe.')
            return redirect(http_referer)

        messages.success(self.request, 'Tarefa atualizada com sucesso.')
        return super().post(self.request, *args, **kwargs)











