from django.shortcuts import render

def cadastro(request):
    if request.method == 'POST':
        pass
    return render(request, 'cadastro_anunciante.html')

def login(request):
    pass