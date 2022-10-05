import copy
from django.shortcuts import render
from django.views.generic import View

class BasePerfil(View):
    def setup(self, request, *args, **kwargs):
        super().setup(*args, **kwargs)
        self.lista = copy.deepcopy(self.request.session.get('lista',{}))

class Cadastro (BasePerfil):
    pass
