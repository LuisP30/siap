from django.shortcuts import render
from .models import Anuncio, Seguimento
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def home(request):
    anuncios = Anuncio.objects.all()
    return render (request,'index.html', context={
        'anuncios': anuncios
    })

def planos(request):
    return render(request, 'planos.html')

@login_required(login_url='autenticacao:login')
def cadastrar_anuncio(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        foto = request.POST.get('foto')
        preco_anterior = request.POST.get('preco-sem-desconto')
        preco_atual = request.POST.get('preco-com-desconto')
        validade = request.POST.get('data-validade')
        id_seguimento = request.POST.get('seguimento')
        anunciante = request.user
        
        seguimento = Seguimento.objects.filter(id=int(id_seguimento)).get()
        anuncio = Anuncio.objects.create(
            titulo=titulo,
            descricao=descricao,
            preco_anterior=preco_anterior,
            preco_atual=preco_atual,
            validade=validade,
            anunciante=anunciante,
            seguimento=seguimento,
            foto=foto
        )
        messages.add_message(request, messages.constants.SUCCESS, 'Anúncio criado com sucesso')
    seguimentos = Seguimento.objects.all()
    return render(request, 'cadastrar_anuncio.html', context={
        'seguimentos': seguimentos
    })

@login_required(login_url='autenticacao:login')
def meus_anuncios(request):
    anuncios = Anuncio.objects.filter(anunciante__id=request.user.id)
    return render(request, 'meus_anuncios.html', context={
        'anuncios': anuncios
    })

@login_required(login_url='autenticacao:login')
def cadastrar_seguimento(request):
    if request.method == 'POST':
        nome_seguimento = request.POST.get('seguimento')
        Seguimento.objects.create(nome=nome_seguimento)
        messages.add_message(request, messages.constants.INFO, 'Um novo seguimento foi criado')
    return render(request, 'cadastrar_seguimento.html')