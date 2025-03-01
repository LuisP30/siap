from django.shortcuts import render, redirect
from .models import Anuncio, Seguimento
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages

# Create your views here.
def home(request):
    query = request.GET.get('q', '')
    if query:
        anuncios = Anuncio.objects.filter(
            Q(titulo__icontains=query) | Q(anunciante__username__icontains=query)
        )
        return render(request,'index.html', context={
        'anuncios': anuncios
        })

    anuncios = Anuncio.objects.all()
    return render (request,'index.html', context={
        'anuncios': anuncios
    })

def planos(request):
    return render(request, 'planos.html')

# VIEWS PARA ANUNCIOS

@login_required(login_url='autenticacao:login')
def cadastrar_anuncio(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        foto = request.FILES.get('foto')
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
        return redirect('anuncios:meus_anuncios')
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
def remover_anuncio(request, id):
    anuncio = Anuncio.objects.get(id=id)
    anuncio.delete()
    messages.add_message(request, messages.constants.ERROR, 'Anúncio excluído')
    return redirect('anuncios:meus_anuncios')

@login_required(login_url='autenticacao:login')
def editar_anuncio(request, id):
    anuncio = Anuncio.objects.get(id=id)
    seguimentos = Seguimento.objects.all()
    anuncio.preco_anterior = "{:.2f}".format(anuncio.preco_anterior)
    anuncio.preco_atual = "{:.2f}".format(anuncio.preco_atual)
    
    if request.method == 'POST':
        anuncio.titulo = request.POST.get('titulo')
        anuncio.descricao = request.POST.get('descricao')
        anuncio.preco_anterior = request.POST.get('preco-sem-desconto')
        anuncio.preco_atual = request.POST.get('preco-com-desconto')
        anuncio.validade = request.POST.get('data-validade')
        id_seguimento = request.POST.get('seguimento')   
        anuncio.seguimento = Seguimento.objects.get(id=id_seguimento)
        if request.FILES.get('foto'):
            foto = request.FILES.get('foto')
            anuncio.foto = foto
        anuncio.save()
            
        messages.add_message(request, messages.constants.INFO, 'Anúncio editado com sucesso')
        return redirect('anuncios:meus_anuncios')
        
    return render(request, 'perfil_anuncio.html', context={
        'anuncio': anuncio,
        'seguimentos': seguimentos
    })

# VIEWS PARA SEGUIMENTOS

@login_required(login_url='autenticacao:login')
def cadastrar_seguimento(request):
    if request.method == 'POST':
        nome_seguimento = request.POST.get('seguimento')
        Seguimento.objects.create(nome=nome_seguimento)
        messages.add_message(request, messages.constants.INFO, 'Um novo seguimento foi criado')
        return redirect('anuncios:cadastrar_anuncio')
    return render(request, 'cadastrar_seguimento.html')