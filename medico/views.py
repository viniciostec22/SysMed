from django.shortcuts import render, HttpResponse, redirect
from .models import Medico, Especialidades
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q


@login_required #type:ignore
def cadastra_medico(request):
    if request.method == 'GET':
        medico = Medico.objects.all()
        especialidades = Especialidades.objects.all()
        if request.GET.get('termo'):
            termo = request.GET.get('termo')
            medico = Medico.objects.filter(Q(nome__icontains=termo)|Q(especialidades__nome__icontains=termo)|Q(crm__icontains=termo))
            return render(request, 'medico/cadastra_medico.html', { 'medico':medico})
        else:
                medico = Medico.objects.order_by('-nome')
        medico = Medico.objects.all()
        paginator = Paginator(medico, 5)  
        page = request.GET.get('page')
        medico = paginator.get_page(page)
     #return render(request, 'medico/cadastra_medico.html', { 'medico':medico})
        return render(request, 'medico/cadastra_medico.html', { 'medico':medico, 'especialidades':especialidades})
   
    elif request.method == 'POST':
        nome            = request.POST.get('nome')
        especialidade   = request.POST.get('especialidade')
        crm             = request.POST.get('crm')
        cpf             = request.POST.get('cpf')
        data_nascimento = request.POST.get('data_nascimento')
        telefone        = request.POST.get('telefone')
        endereco        = request.POST.get('endereco')
        print(especialidade)
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
            especialidades_id = especialidade,
            crm            = crm,
            cpf            = cpf,
            dta_nascimento = data_nascimento,
            tel            = telefone,
            endereco       = endereco
        )
        medico.save()
        messages.add_message(request, constants.SUCCESS, 'Medico cadastrado com sucesso!!')
        return redirect('cadastra_medico')
    
