from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import View
from django.http import HttpResponse

from . import models
from . import forms

class BasePerfil(View):

    template_name = 'perfil/criar.html'
    def setup(self, *args, **kwargs): #esse metodo é da classe view e estamos sobrescrevendo ele, inserindo
    #os elementos da nossa pagina post, neste caso, post, comentarios e o formulario

        super().setup(*args, **kwargs)#Antes de sobrescrever um metodo, precisamos chama-lo para não perder
        #o que já existe nele. Até este ponto, não alteramos nada neste metodo


    #Nós precisamos checar se o usuario e o e-mail preenchidos no formulario de criar perfil já existe.
    #Existe duas formas de fazer essa checagem. A primeira é esperar o usuario enviar o formulario com e-mail e usuario
    #e simplesmente checar se já existem na base de dados. Outra forma é atualizar
    #Vamos fazer

        if self.request.user.is_authenticated: #verificando se o usuario está autenticado. Tudo isso
        #request.user.is_authenticated vem de herança de View

            self.contexto = { #estamos armazenando o nosso contexto, que é formado pelo formulario e um perfil.
            #contexto é uma variavel que vem como herança de View

                'userform': forms.UserForm(  #UserForm é uma classe que criamos no arquivo forms.py e herda de
                #django forms ModelForm

                #O atributo usuario abaixo, nós criamos manualmente na classe UserForm e os demais data e instance vem
                #de herança, pois a classe UserForm criamos por nós, herda de ModelForm que é do django

                    data=self.request.POST or None,
                    usuario=self.request.user,
                    instance=self.request.user,
                ),
                'perfilform': forms.PerfilForm(
                    data=self.request.POST or None
                )
            }

        else:
            self.contexto = {  # estamos armazenando o nosso contexto, que é formado pelo formulario e um perfil

                'userform': forms.UserForm(data=self.request.POST or None),  # Caso a pessoa clique em enviar o formulario,
                # mas o formulario não é enviado por algum erro, ele não perde o que foi digitado e se enviar sem digitar
                # nada, estará vazio
                'perfilform': forms.PerfilForm(
                    data=self.request.POST or None
                )

            }


        self.renderizar = render(self.request, self.template_name, self.contexto)

    def get(self, *args, **kwargs):
        return self.renderizar



class Criar (BasePerfil):
    def post(self, *args, **kwargs):
        return self.renderizar




class Atualizar (View):
    def get(self, *args, **kwargs):
        return HttpResponse('Atualizar')

class Login(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Login')
class Logout(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Logout')