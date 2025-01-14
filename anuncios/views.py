from django.shortcuts import render
from .models import Anuncio

# Create your views here.
def home(request):
    return render (request,'index.html', context={
        
    })

def anuncio_cadastro(request):
    if request.method == 'POST':
        pass
    return render(request, 'anuncio_cadastro.html')

def meus_anuncios(request):
    return render(request, 'meus_anuncios.html', context={
        
    })