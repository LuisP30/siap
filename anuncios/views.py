from django.shortcuts import render
from .models import Anuncio
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render (request,'index.html', context={
        
    })

@login_required(login_url='autenticacao:login')
def cadastrar_anuncio(request):
    if request.method == 'POST':
        pass
    return render(request, 'cadastrar_anuncio.html')

def meus_anuncios(request):
    return render(request, 'meus_anuncios.html', context={
        
    })