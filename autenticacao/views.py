from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.contrib.messages import constants
from .models import Anunciante

def cadastro(request):
    
    if request.method == 'POST':
        
        # Capturando dados da requisição
        email = request.POST.get('email')
        
        if Anunciante.objects.filter(email=email).exists():
            messages.add_message(request, constants.ERROR, 'Já existe um anunciante com este e-mail!')
            return render(request, 'cadastro_anunciante.html')
            
        password = request.POST.get('senha')
        username = request.POST.get('nome')
        if Anunciante.objects.filter(username=username).exists():
            messages.add_message(request, constants.ERROR, 'Já existe um anunciante com este nome!')
            return render(request, 'cadastro_anunciante.html')
        
        cnpj = request.POST.get('cnpj')
        if Anunciante.objects.filter(cnpj=cnpj).exists():
            messages.add_message(request, constants.ERROR, 'Já existe um anunciante com este CNPJ!')
            return render(request, 'cadastro_anunciante.html')
        
        endereco = request.POST.get('endereco')
        telefone = request.POST.get('telefone')
        whatsapp = request.POST.get('whatsapp')
        if Anunciante.objects.filter(whatsapp=whatsapp).exists():
            messages.add_message(request, constants.ERROR, 'Já existe um anunciante com este whatsapp!')
            return render(request, 'cadastro_anunciante.html')
        instagram = request.POST.get('instagram')
        
        # Salvando anunciante no banco de dados
        anunciante = Anunciante.objects.create_user(
            email=email,
            password=password,
            username=username,
            cnpj=cnpj,
            endereco=endereco,
            telefone=telefone,
            whatsapp=whatsapp,
            instagram=instagram
        )
        messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucesso!')
        return redirect('anuncios:planos')
    return render(request, 'cadastro_anunciante.html')

def logar(request):
    if request.user.is_authenticated:
        return redirect('anuncios:planos')
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        usuario = authenticate(request, email=email, password=senha)
        print(usuario)
        if usuario:
            login(request, usuario)
            return redirect(request.GET.get('next', 'anuncios:meus_anuncios'))
        else:
            messages.add_message(request, constants.ERROR, 'E-mail ou Senha incorretos')
            return redirect('autenticacao:login')
    return render(request, 'login.html')

def sair(request):
    logout(request)
    return redirect('anuncios:home')

