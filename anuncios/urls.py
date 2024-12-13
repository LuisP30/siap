from django.urls import path
from .views import home, cadastro_anunciante, anuncio_cadastro, meus_anuncios

urlpatterns = [
    path('', home, name='home'),
    path('cadastro_anunciante/', cadastro_anunciante, name='cadastro_anunciante'),
    path('anuncio_cadastro', anuncio_cadastro, name='anuncio_cadastro'),
    path('meus_anuncios/', meus_anuncios, name='meus_anuncios')
]
