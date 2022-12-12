from django.shortcuts import render, HttpResponse, redirect,get_object_or_404
import consulta
from paciente.models import Paciente
from medico.models import Medico
from django.db.models import Q
from .models import MarcarConsulta
from .forms import MarcaConsultaModelForm
from django.contrib.messages import constants
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.


def cadastrar_consulta(request):
        if request.method == 'GET':
                forms = MarcaConsultaModelForm()  
                return render(request, 'consulta/cadastrar_consulta.html',
                              {'forms':forms})
                
        elif request.method == 'POST':
                forms = MarcaConsultaModelForm(request.POST) 
               
                if forms.is_valid():
                        forms.save() 
                        messages.add_message(request, constants.SUCCESS, 'Consulta Marcada com Sucesso!!')
                        return redirect('cadastrar_consulta')
                else:
                        return render(request, 'consulta/cadastrar_consulta.html',{'forms':forms})
@login_required
def editar_consulta(request, id):
        consuta = MarcarConsulta.objects.get(id=id)
        if request.method == 'POST':
                forms = MarcaConsultaModelForm(request.POST, instance=consuta)
                if forms.is_valid():
                        forms.save()
                        messages.add_message(request, constants.SUCCESS, 'Consulta editada Sucesso!!')
                        return redirect('cadastrar_consulta')
        else:
                forms = MarcaConsultaModelForm(instance=consuta)
        return render(request, 'consulta/cadastrar_consulta.html',{'forms':forms, 'consulta':consulta})
@login_required
def listar_consultas(request):

      if request.GET.get('termo'):
              termo = request.GET.get('termo')
              print('1',termo)
              consultas = MarcarConsulta.objects.filter(Q(paciente__nome__icontains=termo) | 
                                                        Q(medico__nome__icontains=termo)|
                                                        Q(data__icontains=termo))
      else:
              consultas = MarcarConsulta.objects.order_by('-id', '-paciente')
      paginator = Paginator(consultas, 3)  
      page = request.GET.get('page')
      consultas = paginator.get_page(page)
      return render(request, 'consulta/consultas.html', {'consultas':consultas})
@login_required
def excluir_consulta(request, id):
        consulta = get_object_or_404(MarcarConsulta, id=id)
        consulta.delete()
        messages.add_message(request, constants.SUCCESS, 'Consulta Excluida Sucesso!!')
        return redirect('listar_consultas')