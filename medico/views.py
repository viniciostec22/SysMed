from django.shortcuts import render, HttpResponse, redirect
from .models import Medico
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required #type:ignore
def cadastra_medico(request):
    if request.method == 'GET':
        return render(request, 'medico/cadastra_medico.html')
    elif request.method == 'POST':
        nome            = request.POST.get('nome')
        especialidade   = request.POST.get('especialidade')
        crm             = request.POST.get('crm')
        cpf             = request.POST.get('cpf')
        data_nascimento = request.POST.get('data_nascimento')
        telefone        = request.POST.get('telefone')
        endereco        = request.POST.get('endereco')
        
        if not nome or not especialidade or not crm or not cpf or not data_nascimento or not telefone or not endereco:
            messages.add_message(request, constants.ERROR, 'Não pode deixar campos em Branco!!')
            return redirect('cadastra_medico')
        
        elif Medico.objects.filter(cpf=cpf).exists():
            messages.add_message(request, constants.ERROR, 'CPF já cadastrado!!')
            return redirect('cadastra_medico')
        elif Medico.objects.filter(crm = crm).exists():
            messages.add_message(request, constants.ERROR, 'CRM já cadastrado!!')
            return redirect('cadastra_medico')
        medico = Medico(
            nome           = nome,
            especialidades = especialidade,
            crm            = crm,
            cpf            = cpf,
            dta_nascimento = data_nascimento,
            tel            = telefone,
            endereco       = endereco
        )
        medico.save()
        messages.add_message(request, constants.SUCCESS, 'Medico cadastrado com sucesso!!')
        return redirect('cadastra_medico')
    