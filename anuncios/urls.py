from django.urls import path
from .views import home, cadastrar_anuncio, meus_anuncios

app_name = 'anuncios'

urlpatterns = [
    path('', home, name='home'),
    path('cadastrar_anuncio/', cadastrar_anuncio, name='cadastrar_anuncio'),
    path('meus_anuncios/', meus_anuncios, name='meus_anuncios')
]
