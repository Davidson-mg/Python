from django.urls import path
from . import views

urlpatterns = [
    path('', views.Cadastro.as_view(), name='cadastro')
]