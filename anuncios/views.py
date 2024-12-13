from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request,'index.html')

def cadastro_anunciante(request):
    return render (request, 'cadastro_anunciante.html')

def anuncio_cadastro(request):
    return render(request, 'anuncio_cadastro.html')

def meus_anuncios(request):
    return render(request, 'meus_anuncios.html')