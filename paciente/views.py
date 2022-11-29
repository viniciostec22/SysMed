from django.shortcuts import render, HttpResponse, redirect
from .forms import PacienteModelForm
from . models import Paciente, Convenio

def cadastrar_paciente(request):
    if request.method == 'GET':
        forms = PacienteModelForm()
        return render(request, 'paciente/cadastro_paciente.html', {'forms':forms})
    elif request.method == 'POST':
        nome            = request.POST.get('nome')
        email           = request.POST.get('email')
        data_nascimento = request.POST.get('data_nascimento')
        cpf             = request.POST.get('cpf')
        telefone        = request.POST.get('telefone')
        convenio        = request.POST.get('convenio')
        endereco        = request.POST.get('endereco')
        
        
        
        paciente = Paciente(
            nome = nome,
            data_nascimento = data_nascimento,
            cpf = cpf,
            email = email,
            telefone = telefone,
            endereco = endereco,
            convenio_id = convenio
            
            
        )
        paciente.save()
        return redirect('cadastrar_paciente')