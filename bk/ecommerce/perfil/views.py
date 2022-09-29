from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import copy

from . import models
from . import forms

class BasePerfil(View):

    template_name = 'perfil/criar.html'
    def setup(self, *args, **kwargs): #esse metodo é da classe view e estamos sobrescrevendo ele, inserindo
    #os elementos da nossa pagina post, neste caso, post, comentarios e o formulario

        super().setup(*args, **kwargs)#Antes de sobrescrever um metodo, precisamos chama-lo para não perder
        #o que já existe nele. Até este ponto, não alteramos nada neste metodo

        self.carrinho = copy.deepcopy(self.request.session.get('carrinho', {}))  # Quando o usuario altera a senha ou
        # qualquer outro dados, ele perde a sessão e consequentemente o carrinho. Estamos fazendo uma copia do carrinho
        # logo no inicio para podermos mais abaixo na parte reponsavel por senha e etc

        self.perfil = None

    #Nós precisamos checar se o usuario e o e-mail preenchidos no formulario de criar perfil já existe.
    #Existe duas formas de fazer essa checagem. A primeira é esperar o usuario enviar o formulario com e-mail e usuario
    #e simplesmente checar se já existem na base de dados. Outra forma é atualizar
    #Aqui vamos optar pela forma de atualizar
    #Em nosso projeto, teremos uma unica tela para login e para cadastro/atualizar cadastro. Se o usuario estiver logado
    #A tela de login fica a esquerda e a de cadastro/atualizar fica a direita.
    #Se o cadastro do cliente já existe, ele consegue atualizar algum informação de seu cadastro no formulario
    #a direita. Além disso, se o cadastro já existe, ele não é obrigado a preencher nova senha

        if self.request.user.is_authenticated: #verificando se o usuario está autenticado. Tudo isso
        #request.user.is_authenticated vem de herança de View

            self.perfil = models.Perfil.objects.filter(usuario = self.request.user).first() #criando uma variavel de
            # instancia de perfil. Um perfil que tenha um usuario

            self.contexto = { #estamos armazenando o nosso contexto, que é formado pelo formulario e um perfil.
            #contexto é uma variavel que vem como herança de View

                'userform': forms.UserForm(  #UserForm é uma classe que criamos no arquivo forms.py e herda de
                #django forms ModelForm

                #O atributo usuario abaixo, nós criamos manualmente na classe UserForm e os demais data e instance vem
                #de herança, pois a classe UserForm criada por nós, herda de ModelForm que é do django

                    data=self.request.POST or None,
                    usuario=self.request.user,
                    instance=self.request.user, #Se ele está autenticado, a gente envia uma instancia do usuario
                ),
                'perfilform': forms.PerfilForm(
                    data=self.request.POST or None,
                    instance=self.perfil
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

        # criando variaveis para os formularios. Essas duas variaveis vão conter os formularios
        self.userform = self.contexto['userform'] #pegando a chave do contexto acima
        self.perfilform = self.contexto['perfilform']


        if self.request.user.is_authenticated: #se o usuario estive autenticador, queremos que na tela de perfil de
            #cadastro, ao inves de aparece cadastro, será atualizar
            self.template_name = 'perfil/atualizar.html'


        self.renderizar = render(self.request, self.template_name, self.contexto)

    def get(self, *args, **kwargs):
        return self.renderizar



class Criar (BasePerfil):
    def post(self, *args, **kwargs):
        if not self.userform.is_valid() or not self.perfilform.is_valid(): #se o formulario de perfil e de usuario não
            #são validos
            messages.error(
                self.request, 'Existem erros nos formulario. Por gentileza, verifique todos os campos.'
            )

            return self.renderizar

        #pegando usuario, senha e email do formulario de usuario
        username = self.userform.cleaned_data.get('username')
        password = self.userform.cleaned_data.get('password')
        email = self.userform.cleaned_data.get('email')
        first_name = self.userform.cleaned_data.get('first_name')
        last_name = self.userform.cleaned_data.get('last_name')

        #usuario logado
        if self.request.user.is_authenticated:
            usuario = get_object_or_404(User, username=self.request.user.username)
            usuario.username = username

            if password:
                usuario.set_password(password)

            usuario.email = email
            usuario.first_name = first_name
            usuario.last_name = last_name
            usuario.save()

            if not self.perfil: #Quando o cliente digitar os dados de perfil, vamos verificar se esse perfil já existe
                self.perfilform.cleaned_data['usuario'] = usuario #vamo imbutir o usuario neste perfil. Sem essa linha,
                #na linha de baixo o perfil não teria o usuario
                perfil = models.Perfil(**self.perfilform.cleaned_data)
                perfil.save()
            else:
                perfil = self.perfilform.save(commit=False)
                perfil.usuario = usuario
                perfil.save()

        #usuario não logado (novo)
        else:

            #Vamos registrar o usuario e o perfil
            usuario = self.userform.save(commit=False) #esse commit false é para salvar mas não base de dados ainda
            usuario.set_password(password)
            usuario.save()

            perfil = self.perfilform.save(commit=False)
            perfil.usuario = usuario
            perfil.save()

        if password:#Se uma senha foi enviada é pq o usuario logado atualizou ela ou que é um novo usuario. Se ele já
        #é um usuario e esta logado, quando altera/atualiza a senha, ele é deslogado. Por isso vamos reloga-lo
        #se alterar a senha

            autentica = authenticate(self.request, username=usuario, password=password) #Vamos autenticar o usuario

            if autentica: #se autentica
                login(self.request, user=usuario)


        # Quando o usuario altera a senha ou qualquer outro dados, ele perde a sessão e consequentemente o carrinho.
        # Estamos fazendo uma copia do carrinho logo no inicio na variavel self.carrinho e vamos

        self.request.session['carrinho'] = self.carrinho
        self.request.session.save()

        messages.success(self.request, 'Seu cadastro foi criado ou atualizado com sucesso.')
        messages.success(self.request, 'LOGIN EFETUADO!')

        return redirect('produto:carrinho')
        return self.renderizar


class Atualizar (View):
    def get(self, *args, **kwargs):
        return HttpResponse('Atualizar')

class Login(View):
    def post(self, *args, **kwargs):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')

        if not username or not password:
            messages.error(self.request, 'Desculpe! Usuário ou senha inválidos.')
            return redirect('perfil:criar')

        usuario = authenticate(self.request, username=username, password=password)

        if not usuario:
            messages.error(self.request, 'Desculpe! Usuário ou senha inválidos.')
            return redirect('perfil:criar')


        login(self.request, user=usuario)

        messages.success(self.request, 'Login efetuado com sucesso.')

        return redirect('produto:carrinho')

class Logout(View):
    def get(self, *args, **kwargs):
        carrinho = copy.deepcopy(self.request.session.get('carrinho'))
        logout(self.request)
        self.request.session['carrinho'] = carrinho
        self.request.session.save()
        return redirect('produto:lista')