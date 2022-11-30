from importlib.abc import PathEntryFinder
from django.shortcuts import render, HttpResponse, redirect
from .forms import PacienteModelForm
from . models import Paciente, Convenio
from django.contrib.messages import constants
from django.contrib import messages

def cadastrar_paciente(request):
    if request.method == 'GET':
        return render(request, 'paciente/cadastro_paciente.html')
    
    elif request.method == 'POST':
        nome            = request.POST.get('nome')
        email           = request.POST.get('email')
        data_nascimento = request.POST.get('data_nascimento')
        cpf             = request.POST.get('cpf')
        telefone        = request.POST.get('telefone')        
        endereco        = request.POST.get('endereco')            
        
        if Paciente.objects.filter(cpf=cpf).exists():
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