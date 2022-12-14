from unicodedata import name
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from rolepermissions.decorators import has_permission_decorator
from .models import Users, Cargo
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants
from django.contrib import messages
from .models import Cargo
from django.core.validators import validate_email
from django.core.paginator import Paginator
from django.db.models import Q


@has_permission_decorator('cadastrar_recepcionista')
def cadastro_usuario(request):
        
    if request.method == 'GET':
        cargo = Cargo.objects.all()
        users = Users.objects.all()
        if request.GET.get('termo'):
            termo = request.GET.get('termo')
            print(termo)
            users = Users.objects.filter(Q(username__icontains=termo)|Q(email__icontains=termo)|Q(first_name__icontains=termo))
            return render(request, 'cadastro_usuario.html', {'users': users})
        else:
                users = Users.objects.order_by('-first_name')
        users = Users.objects.all()
        paginator = Paginator(users, 5)  
        page = request.GET.get('page')
        users = paginator.get_page(page)
        #return render(request, 'cadastro_usuario.html', {'users': users})
        return render(request, 'cadastro_usuario.html', {'users': users, 'cargo':cargo})
    elif request.method == 'POST':
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        data_nascimento = request.POST.get('data_nascimento')
        cpf = request.POST.get('cpf')
        senha = request.POST.get('senha')
        cargo = request.POST.get('cargo')
        
        user = Users.objects.filter(username=usuario)
        if not usuario or not email or not nome or not sobrenome or not data_nascimento or not cpf or not senha or not cargo:
            messages.add_message(request, constants.ERROR, 'Não pode deixar campos em Branco!!') 
            
        elif user.exists():
            messages.add_message(request, constants.ERROR, 'Nome de Usuario em uso tento outro!!') 
            return redirect('cadastrar_usuario')
        
        elif Users.objects.filter(cpf=cpf):
            messages.add_message(request, constants.ERROR, 'CPF já cadastrado') 
            return redirect('cadastrar_usuario')
        
        try:
            validate_email(email)
        except:
            messages.add_message(request, constants.ERROR, 'Email invalido')
            return redirect('cadastrar_usuario')
        
        if Users.objects.filter(email=email):
            messages.add_message(request, constants.ERROR, 'Email já está em uso') 
            return redirect('cadastrar_usuario')
        
        
        user = Users.objects.create_user(username=usuario, email=email, first_name=nome, last_name=sobrenome, password=senha, cargo_id=cargo, data_nascimento=data_nascimento, cpf=cpf)  # type: ignore
        messages.add_message(request, constants.SUCCESS, 'Usuario cadastrado com sucesso!') 
        return redirect('cadastrar_usuario')
        
def login(request):
    
    if request.method == "POST":
        login = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user = auth.authenticate(username=login, password=senha)
        
        if not user:
            messages.add_message(request, constants.ERROR, 'Email ou senha Incorreto!!') 
            return redirect(reverse('login'))
        
        auth.login(request, user)
        messages.add_message(request, constants.SUCCESS, 'Login efetuado com sucesso')
        return render(request,'plataforma.html',{'user':user})
    return redirect(reverse('plataforma'))
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

@login_required
def editar_usuario(request, id):
    user = Users.objects.filter(id=id)
    if request.method == 'GET':
          return render(request, 'editar_usuario.html', {'user': user})

@login_required
def add_cargo(request):
    if request.method == "GET":
        return render(request, 'cadastro_usuario.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        
        if Cargo.objects.filter(nome = nome).exists():
             messages.add_message(request, constants.ERROR, 'Cargo já cadastrado!!')
             return redirect('cadastrar_usuario')
        cargo = Cargo(
            nome = nome
        )
        cargo.save()
        messages.add_message(request, constants.SUCCESS, 'Cargo criado Com sucesso!!')
        return redirect('cadastrar_usuario')

