from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import PacienteModelForm
from .models import Paciente, Convenio
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q



def lista_pacientes(request):
    if request.GET.get('termo'):
            termo = request.GET.get('termo')
            pacientes = Paciente.objects.filter(Q(nome__icontains=termo)|Q(email__icontains=termo)|Q(cpf__icontains=termo)|Q(telefone__icontains=termo))
            return render(request, 'paciente/cadastro_paciente.html', {'pacientes':pacientes})
    else:
            pacientes = Paciente.objects.order_by('-nome')
            pacientes = Paciente.objects.all()
            paginator = Paginator(pacientes, 5)  
            page = request.GET.get('page')
            pacientes = paginator.get_page(page)
            return render(request, 'paciente/cadastro_paciente.html', {'pacientes':pacientes})
            
    
@login_required #type:ignore
def cadastrar_paciente(request):
    pacientes = Paciente.objects.all()
    if request.method == 'GET':
        return render(request, 'paciente/cadastro_paciente.html', {'pacientes':pacientes})
 
    elif request.method == 'POST':
        nome            = request.POST.get('nome')
        email           = request.POST.get('email')
        data_nascimento = request.POST.get('data_nascimento')
        cpf             = request.POST.get('cpf')
        telefone        = request.POST.get('telefone')        
        endereco        = request.POST.get('endereco')            
        
        if not nome or not email or not cpf or not telefone or not endereco:
             messages.add_message(request, constants.ERROR, 'Não pode aver campos em Branco!!')
             return redirect('cadastrar_paciente')
         
        elif Paciente.objects.filter(cpf=cpf).exists():
             messages.add_message(request, constants.ERROR, 'CPF já cadastrado!!')
             return redirect('cadastrar_paciente')
         
        elif Paciente.objects.filter(email=email).exists():
            messages.add_message(request, constants.ERROR, 'E-mail já cadastrado!!')
            return redirect('cadastrar_paciente')
        
        paciente = Paciente(
            nome = nome,
            data_nascimento = data_nascimento,
            cpf = cpf,
            email = email,
            telefone = telefone,
            endereco = endereco,
            
        )
        paciente.save()
        messages.add_message(request, constants.SUCCESS, 'Paciente salvo Com sucesso!!')
        return redirect('cadastrar_paciente')
@login_required    
def delete_paciente(request, id):
    paciente = get_object_or_404(Paciente, id = id)
    paciente.delete()
    messages.add_message(request, constants.SUCCESS, 'Paciente excluido Com sucesso!!')
    return redirect('cadastrar_paciente')
@login_required  
def editar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id = id)
    return render(request, 'paciente/editar_paciente.html', {'paciente':paciente})
@login_required  
def update(request, id):
    nome            = request.POST.get('nome')
    email           = request.POST.get('email')
    data_nascimento = request.POST.get('data_nascimento')
    cpf             = request.POST.get('cpf')
    telefone        = request.POST.get('telefone')        
    endereco        = request.POST.get('endereco') 
    
    paciente = Paciente.objects.get(id=id)
    
    paciente.nome = nome
    paciente.data_nascimento = data_nascimento
    paciente.cpf = cpf
    paciente.email = email
    paciente.telefone = telefone
    paciente.endereco = endereco
    paciente.save()
    messages.add_message(request, constants.SUCCESS, 'Paciente editado Com sucesso!!')
    return redirect('cadastrar_paciente')
   