from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import Cadastrar

def index(request):
    return render(request, 'app_academia/index.html')

def home(request):
    return render(request, 'app_academia/home.html')

def treinos(request):
    return render(request, 'app_academia/treinos.html')

def cadastrar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        # Validações simples
        if not nome or not email or not senha:
            return render(request, 'app_academia/cadastrar.html', {'error': 'Todos os campos são obrigatórios.'})
        
        # Criptografar senha
        senha_hashed = make_password(senha)

        # Criar novo usuário
        usuario = Cadastrar.objects.create(nome=nome, email=email, senha=senha_hashed)
        
        return redirect('home')
    
    return render(request, 'app_academia/cadastrar.html')
