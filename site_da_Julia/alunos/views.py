from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_autentica
from django.contrib.auth.decorators import login_required

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        nome_do_aluno = request.POST.get('username')
        email_do_aluno = request.POST.get('email')
        senha_do_aluno = request.POST.get('password')

        aluno = User.objects.filter(username=nome_do_aluno).first()

        if aluno:
            return HttpResponse('Aluno já cadastrado')
        
        aluno = User.objects.create_user(nome_do_aluno, email_do_aluno, senha_do_aluno)
        aluno.save()

        return HttpResponse('Usuario criado com sucesso')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha_do_aluno = request.POST.get('password')
        
        aluno = authenticate(request, username=username, password=senha_do_aluno)
        
        if aluno:
            login_autentica(request, aluno)

            return HttpResponse('Aluno logado com sucesso')
        else:
            return HttpResponse('Aluno não cadastrado')
        
@login_required
def home(request):
        return HttpResponse('Voce precisa estar logado para acessar essa pagina')

