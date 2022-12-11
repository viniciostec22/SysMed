from django.shortcuts import render, HttpResponse, redirect
from paciente.models import Paciente
from medico.models import Medico
from django.db.models import Q
from .models import MarcarConsulta
from .forms import MarcaConsultaModelForm
from django.contrib.messages import constants
from django.contrib import messages

# Create your views here.
def cadastrar_consulta(request):
        if request.method == 'GET':
                form = MarcaConsultaModelForm()  
                return render(request, 'consulta/cadastrar_consulta.html',
                              {'form':form})
                
        elif request.method == 'POST':
                form = MarcaConsultaModelForm(request.POST) 
               
                if form.is_valid():
                        form.save() 
                        messages.add_message(request, constants.SUCCESS, 'Consulta Marcada com Sucesso!!')
                        return redirect('cadastrar_consulta')
                else:
                        return render(request, 'consulta/cadastrar_consulta.html',{'form':form})
                        
      
      
        
