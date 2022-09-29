#Este arquivo não é padrão do Django. Nós que criamos para para pegar o form de comentarios.
#vamos usar este arquivo no views de posts

from django.forms import ModelForm
from .models import Comentario

class FormComentario(ModelForm):

    def clean(self):
        data=self.cleaned_data
        nome = data.get('nome_comentario')
        email = data.get('email_comentario')
        comentario = data.get('comentario')

        #Daqui pra baixo, vamos adicionar algumas validações. Lembrando que o form já possui
        #as validações do proprio model, por exemplo, exigir que o campo seja preenchido, informar um e-mail valido e etc
        #Nós vamos acrescentar novas validações, o que não é obrigatorio

        if len(nome) < 2: #Acrescentamos apenas uma validação que obrigue o nome ter pelo menos 3 caracteres. Fiz isso
            #mais como exemplo mesmo
            self.add_error(
                'nome_comentario',
                'Nome precisa ter mais que 5 caracteres.'
            )

    class Meta:
        model = Comentario
        fields = ('nome_comentario', 'email_comentario', 'comentario') #estamos definindo os atributos do models
        #comentario que queremos utilizar