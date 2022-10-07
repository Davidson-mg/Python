
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic.detail import DetailView, View
from django.views.generic import ListView, UpdateView
from .models import Tarefa, FormLista
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect



class DispatchLoginRequiredMixin(View):
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('principal:listadetarefas')
        return super().dispatch(*args, **kwargs)



def index(request):
    return render(request, 'paginas/index.html')



class ListaDeTarefas(ListView):

    def get(self, *args, **kwargs):
        form = FormLista
        tarefas = Tarefa.objects.all()
        self.model = Tarefa
        self.template_name = 'paginas/listadetarefas.html'

        return render(self.request, self.template_name, {'form': form, 'tarefas': tarefas})


def adicionarTarefa(request):

    http_referer = request.META.get('HTTP_REFERER')
    form = FormLista
    form = FormLista(request.POST, request.FILES)
    nome = request.POST.get('nome')

    if Tarefa.objects.filter(nome=nome).exists():
        messages.error(request, f'{nome} já existe na lista')
        return redirect(http_referer)

    # return HttpResponseRedirect('paginas/listadetarefas.html')

    form.save()

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
    fields = ['id', 'nome', 'previsao_conclusao', 'observacao', 'status', 'descricao']
    pk_url_kwarg = 'id'
    success_url = '/listadetarefas'

    def post(self, *args, **kwargs):
        messages.success(self.request, 'Tarefa atualizada com sucesso.')
        return super().post(self.request, *args, **kwargs)












