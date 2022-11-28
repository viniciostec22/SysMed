from django.shortcuts import render, HttpResponse
from .forms import PacienteModelForm

def cadastrar_paciente(request):
    if request.method == 'GET':
        forms = PacienteModelForm()
        return render(request, 'paciente/cadastro_paciente.html', {'forms':forms})