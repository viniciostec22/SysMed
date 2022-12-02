from django.shortcuts import render, HttpResponse
from paciente.models import Paciente
from django.db.models import Q

# Create your views here.
def cadastrar_consulta(request):
        pacienteunico=''
        if request.method == 'POST':
                pacienteunico = request.POST.get('paciente')
                id= request.POST.get('id')
                #paciente = str(paciente).split(" ")[0]
                print(id)
                
        paciente = Paciente.objects.all()
        return render(request, 'consulta/cadastrar_consulta.html',{'paciente':paciente, 'pacienteunico':pacienteunico})
    
        