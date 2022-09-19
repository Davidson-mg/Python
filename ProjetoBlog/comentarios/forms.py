#Este arquivo não é padrão do Django. Nós que criamos para para pegar o form de comentarios.
#vamos usar este arquivo no views de posts

from django.forms import ModelForm
from .models import Comentario
import requests #precisa instalar:  pip install requests

class FormComentario(ModelForm):

    def clean(self):
        raw_data = self.data #Estamos pegando os dados quem vem no formulario de comentario. Neste caso, nome, email,
        #comentario e o codigo data-sitekey que geramos no google e inserimos numa div dentro deste form no html

        recaptcha_response = raw_data.get('g-recaptcha-response') #Esse é o nome da variavel que vem com o codigo (1º codigo)
        #que colocamos na div em data-sitekey no html de comentarios. Se dessemos um 'print(raw_data)' neste ponto, vc
        #veria g-recaptcha-response com a chave junto aos demais valores preenchido no form, tipo, nome, comentario e etc

        recaptcha_request = requests.post( #Estamos postando alguma coisa para o Google

            'https://www.google.com/recaptcha/api/siteverify', #vai postar nesta url

            data={ #Os dados que serão postados. Um dicionario com a SEGUNDA CHAVE (COPIAR CHAVE SECRETA) que foi gerada
            #quando criamos o recapetcha no Google e também a resposta, que ai é a primeira chave que recebemos de
            #recaptcha_response e está na nossa div dentro forma em data-sitekey
                'secret':'jqpjqwpojwpojqwefqwqe', #essa chave está errada por conta dos commits ao
                #github. Sempre que quiser rodar este projeto precisa copiar a chave corre pra não da problema
                'response': recaptcha_response #
            }
        )
        recaptcha_result = recaptcha_request.json() #estamos pegando o resultado do que foi enviado ao google na variavel
        #recaptcha_request e armazenando no formato json

        if not recaptcha_result.get('success'): #succes é um compo que vem na resposta do google que nos diz se houve
        #sucesso na validação do recapetcha. Ele vem com True ou False.  Se ele for FALSE ...
            self.add_error(
                'comentario', #estamos adicionar msg de erro dentro do CAMPO comentario
                'Estou desconfiado que você é um robô. Por isso, você não pode enviar.' #a mensagem
            )

        cleaned_data=self.cleaned_data
        nome = cleaned_data.get('nome_comentario')
        email = cleaned_data.get('email_comentario')
        comentario = cleaned_data.get('comentario')

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







#Aqui, seria a mesma classe acima só que sem o recaptcha
# class FormComentario(ModelForm):
#
#     def clean(self):
#         data=self.cleaned_data
#         nome = data.get('nome_comentario')
#         email = data.get('email_comentario')
#         comentario = data.get('comentario')
#
#         #Daqui pra baixo, vamos adicionar algumas validações. Lembrando que o form já possui
#         #as validações do proprio model, por exemplo, exigir que o campo seja preenchido, informar um e-mail valido e etc
#         #Nós vamos acrescentar novas validações, o que não é obrigatorio
#
#         if len(nome) < 2: #Acrescentamos apenas uma validação que obrigue o nome ter pelo menos 3 caracteres. Fiz isso
#             #mais como exemplo mesmo
#             self.add_error(
#                 'nome_comentario',
#                 'Nome precisa ter mais que 5 caracteres.'
#             )
#
#     class Meta:
#         model = Comentario
#         fields = ('nome_comentario', 'email_comentario', 'comentario') #estamos definindo os atributos do models
#         #comentario que queremos utilizar