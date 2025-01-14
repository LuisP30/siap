from django.urls import path
from .views import home, anuncio_cadastro, meus_anuncios

urlpatterns = [
    path('', home, name='home'),
    path('anuncio_cadastro', anuncio_cadastro, name='anuncio_cadastro'),
    path('meus_anuncios/', meus_anuncios, name='meus_anuncios')
]
