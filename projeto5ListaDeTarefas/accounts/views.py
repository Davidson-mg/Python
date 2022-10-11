import copy
from django.shortcuts import render
from django.views.generic import View
from django.views.generic import ListView, View, UpdateView, RedirectView
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.core.validators import validate_email
from django.contrib.auth.models import User
from principal import urls




# class BasePerfil(View):
#     def setup(self, request, *args, **kwargs):
#         super().setup(*args, **kwargs)
#         self.lista = copy.deepcopy(self.request.session.get('lista',{}))


class Login(ListView):

    model = User
    context_object_name = 'pedidos'
    template_name = 'accounts/login.html'

    def post(self, *args, **kwargs):

        username = self.request.POST.get('username')
        password = self.request.POST.get('password')

        if not username or not password:
            messages.error(self.request, 'Usuário ou senha inválidos')
            return redirect('accounts:login')

        usuario = authenticate(self.request, username=username, password=password)

        if not usuario:
            messages.error(self.request, 'Usuário ou senha inválidos')
            return redirect('accounts:login')

        login(self.request, user=usuario)

        messages.success(self.request, 'login efetuado com sucesso')

        return redirect('principal:listadetarefas')



class Cadastro (ListView):
    model = User
    context_object_name = 'cadastro'
    template_name = 'accounts/cadastro.html'

    def post(self, *args, **kwargs):
        if self.request.method != 'POST':
            return redirect(self.request, 'accounts/cadastro.html')

        nome = self.request.POST.get('nome')
        sobrenome = self.request.POST.get('sobrenome')
        usuario = self.request.POST.get('usuario')
        email = self.request.POST.get('email')
        senha1 = self.request.POST.get('senha1')
        senha2 = self.request.POST.get('senha2')

        if not nome or not sobrenome or not usuario or not email or not senha1 or not senha2:
            messages.error(self.request, 'Nenhum campo pode estar vazio')
            return redirect('accounts:cadastro')

        try:
            validate_email(email)
        except:
            messages.error(self.request, 'E-mail invalido.')
            return redirect('accounts:cadastro')

        if senha1 != senha2:
            messages.error(self.request, 'Senhas são diferentes')
            return redirect('accounts:cadastro')

        if User.objects.filter(username=usuario).exists():
            messages.error(self.request, 'Usuário já existe')
            return redirect('accounts:cadastro')

        messages.success(self.request, 'Cadastro realizado com sucesso! Faça seu login.')

        user = User.objects.create_user(username=usuario, email=email, password=senha1, first_name=nome, last_name=sobrenome)
        user.save()

        return redirect('accounts:login')



class Logout(View):
    def get(self, *args, **kwargs):
        logout(self.request)
        return redirect('principal:index')