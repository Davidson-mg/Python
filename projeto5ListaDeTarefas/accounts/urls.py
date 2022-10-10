from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [

    path('', views.Login.as_view(), name='login'),
    path('cadastro/', views.Cadastro.as_view(), name='cadastro'),
    path('logout/', views.Logout.as_view(), name='logout')

]