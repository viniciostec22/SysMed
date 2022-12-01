from django.shortcuts import render, HttpResponse
from paciente.models import Paciente
from django.db.models import Q

# Create your views here.
def cadastrar_consulta(request):
    
        paciente = Paciente.objects.all()
        return render(request, 'consulta/cadastrar_consulta.html',{'paciente':paciente})
    
   