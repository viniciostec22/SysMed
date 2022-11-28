from unicodedata import name
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from rolepermissions.decorators import has_permission_decorator
from .models import Users
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants
from django.contrib import messages
from .models import Cargo

@has_permission_decorator('cadastrar_recepcionista')
def cadastro_usuario(request):
    cargo = Cargo.objects.all()
    if request.method == 'GET':
        users = Users.objects.all()
        return render(request, 'cadastro_usuario.html', {'users': users, 'cargo':cargo})
    elif request.method == 'POST':
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        senha = request.POST.get('senha')
        cargo = request.POST.get('cargo')
       
        user = Users.objects.filter(username=usuario)
        
        if user.exists():
            messages.add_message(request, constants.ERROR, 'Usuario já existente!!') 
            return redirect('cadastrar_usuario')
        
        user = Users.objects.create_user(username=usuario, email=email, first_name=nome, last_name=sobrenome, password=senha, cargo_id=cargo)  # type: ignore
        messages.add_message(request, constants.SUCCESS, 'Usuario cadastrado com sucesso!') 
        return redirect('cadastrar_usuario')
        

def login(request):
    
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(reverse('plataforma'))
        
        return render(request, 'login.html')
    elif request.method == "POST":
        login = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user = auth.authenticate(username=login, password=senha)
        
        if not user:
            messages.add_message(request, constants.ERROR, 'Email ou senha Incorreto!!') 
            return redirect(reverse('login'))
        
        auth.login(request, user)
        messages.add_message(request, constants.SUCCESS, 'Login efetuado com sucesso')
        return render(request,'plataforma.html',{'user':user})
@login_required
def plataforma(request):
    
    return render(request,'plataforma.html')  
  

def logout(request):
    request.session.flush()
    return redirect(reverse('login'))

@has_permission_decorator('cadastrar_vendedor')
def exluir_usuario(request, id):
    users = get_object_or_404(Users, id=id)
    users.delete()
    messages.add_message(request, constants.SUCCESS, f'Usuario {users.first_name.upper()} exluido com sucesso')
    return redirect(reverse('cadastrar_usuario'))
    
