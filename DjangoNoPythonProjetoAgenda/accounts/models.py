from django.db import models
from contatos.models import Contato #Estamos importando os models criados lá na pasta do primeiro app contatos
from django import forms

class FormContato(forms.ModelForm):

    #Vamos criar um formulario html com base no models já existente no arquivo contatos.

    class Meta: #Essa classe vai representar o models de Contato
        model = Contato #Lembrando que a classe Contato está no arquivo models lá da pasta contatos
        exclude = ('mostrar',) #estamos enviando uma tupla do que queremos exlcuir. Neste caso, como estamos enviando
        #apenas um elemento, precisa da virgula, pois é uma tupla. Como já temos os atributos do formulario
        #neste caso não vamos criar novos, vamos apenas excluir o que não queremos
        #Depois disso vc vai no arquivo views na função que carrega a pagina deashboard

        #A unica coisa que o Django não vai enviar neste caso é o botão enviar, por isso vamos ser obrigados a cria-los
        #no html