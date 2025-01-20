from django.urls import path
from .views import cadastro, logar, sair, planos

app_name = 'autenticacao'

urlpatterns = [
    path('cadastro/', cadastro, name='cadastro'),
    path('login/', logar, name='login'),
    path('logout/', sair, name='logout'),
]
