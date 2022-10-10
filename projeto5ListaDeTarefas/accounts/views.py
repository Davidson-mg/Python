import copy
from django.shortcuts import render
from django.views.generic import View
from django.views.generic.list import ListView, View
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from principal import urls




class BasePerfil(View):
    pass
    # def setup(self, request, *args, **kwargs):
    #     super().setup(*args, **kwargs)
    #     self.lista = copy.deepcopy(self.request.session.get('lista',{}))

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



class Cadastro (View):
    model = User
    context_object_name = 'cadastro'
    template_name = 'accounts/cadastro.html'




class Logout(View):
    def get(self, *args, **kwargs):
        logout(self.request)
        return redirect('principal:index')