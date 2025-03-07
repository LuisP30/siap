from django.urls import path
from .views import home, cadastrar_anuncio, meus_anuncios, cadastrar_seguimento, planos, remover_anuncio, editar_anuncio
from django.conf import settings
from django.conf.urls.static import static

app_name = 'anuncios'

urlpatterns = [
    path('', home, name='home'),
    path('cadastrar_anuncio/', cadastrar_anuncio, name='cadastrar_anuncio'),
    path('remover_anuncio/<int:id>', remover_anuncio, name="remover_anuncio"),
    path('editar_anuncio/<int:id>', editar_anuncio, name="editar_anuncio"),
    path('meus_anuncios/', meus_anuncios, name='meus_anuncios'),
    path('cadastrar_seguimento/', cadastrar_seguimento, name='cadastrar_seguimento'),
    path('planos/', planos, name='planos'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)