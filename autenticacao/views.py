from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .models import Anunciante

def cadastro(request):
    
    if request.method == 'POST':
        
        # Capturando dados da requisição
        email = request.POST.get('email')
        password = request.POST.get('senha')
        username = request.POST.get('nome')
        cnpj = request.POST.get('cnpj')
        endereco = request.POST.get('endereco')
        telefone = request.POST.get('telefone')
        whatsapp = request.POST.get('whatsapp')
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
        return redirect('autenticacao:login')
    return render(request, 'cadastro_anunciante.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        usuario = authenticate(request, email=email, password=senha)
        print('teste')
        if usuario:
            print('Autenticado')
            pass
    return render(request, 'login.html')