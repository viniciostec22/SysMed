from django.shortcuts import render, HttpResponse
from paciente.models import Paciente
from django.db.models import Q

# Create your views here.
def cadastrar_consulta(request):
        if request.method == 'POST':
                nome = request.POST.get('coisa')
                nome = str(nome).split(" ")[0]
                print(nome)
        paciente = Paciente.objects.all()
        return render(request, 'consulta/cadastrar_consulta.html',{'paciente':paciente})
    
        