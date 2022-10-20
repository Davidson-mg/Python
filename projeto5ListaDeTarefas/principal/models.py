from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django import forms



class Tarefa(models.Model):
    # usuario = models.ForeignKey(User, on_delete=models.CASCADE) #vamos criar uma relação com o usuario do django
    # #de modo que ao deletar o usuario, a sua lista de tarefas seja deletada também

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    nome = models.CharField(max_length=255)
    data_inclusao = models.DateField(default=timezone.now)
    previsao_conclusao = models.DateField()
    descricao = models.TextField(blank=True)
    observacao = models.CharField(max_length=255, blank=True)
    codigo = models.IntegerField()
    status = models.CharField(
        max_length=1,
        default='p',
        choices=(
            ('p','pendente'),
            ('c','concluido')
        )
    )

    def __str__(self):
        return f'{self.nome}'


class FormLista(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ('id', 'nome', 'data_inclusao', 'previsao_conclusao', 'observacao')

    def __init__(self, user=None, *args, **kwargs):
        super(FormLista, self).__init__(*args, **kwargs)


