from django.shortcuts import render, redirect # "render" Biblioteca que mostra a página, "redirect" permite redirecionar para outra página.

from django.contrib.auth import authenticate, login, logout # "authenticate" Serve para verificar as credencias, "login" Serve para registrar o usuario na sessão do django.
# "logout" para sair da conta

from django.contrib.auth.models import User # Permite criar usúarios no banco de dados.

from django.contrib import messages # Permite mostrar mensagens de erro ou sucesso.

from django.contrib.auth.decorators import login_required # Não deixa o usuario entrar em uma página sem estar logado 
 


def inicio(request):
    return render(request, 'principal/index.html') # Função que traz o arquivo index para renderizar inicialmente.

@login_required
def aula(request):
    return render(request, 'aula/aulas.html' )

@login_required
def computador(request):
    return render(request, 'aula/computador/pc.html') 

@login_required
def progresso(request):
    return render(request, 'perfil/progresso.html' )

@login_required
def logica(request):
    return render(request, 'aula/logica/logica.html')

@login_required
def front(request):
    return render(request, 'aula/front/front.html')

@login_required
def ia(request):
    return render(request, 'aula/IA/ia.html')

@login_required
def hacker(request):
    return render(request, 'aula/hacker/hacker.html')

@login_required
def python(request):
    return render(request, 'aula/python/python.html')


def entrar(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        usuario = authenticate(request,username=email, password=senha)
        
        if usuario:
            login(request, usuario)
            return redirect('inicio')
            
        else:
            messages.error(request, 'E-mail ou senha incorretos')  
        
    return render(request, 'principal/entrar.html' )

def cadastro(request):

    if request.method == 'POST':

        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        # Verifica se o e-mail já existe
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Este e-mail já está cadastrado.')

        else:
            usuario = User.objects.create_user(
                username=email,
                first_name=nome,
                email=email,
                password=senha
            )

            login(request, usuario, backend='cursos.autenticacao.EmailBackend')
            return redirect('inicio')

    return render(request, 'principal/cadastro.html')

from django.views.decorators.http import require_POST

@require_POST
def sair(request):
    logout(request)
    return redirect('inicio')