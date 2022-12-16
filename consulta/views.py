from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
import consulta
from paciente.models import Paciente
from medico.models import Medico
from django.db.models import Q
from .models import MarcarConsulta
from .forms import MarcaConsultaModelForm
from django.contrib.messages import constants
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.

def cadastrar_consulta(request):
        pacientes = Paciente.objects.all()
        medicos = Medico.objects.all()
        consulta = MarcarConsulta.objects.all()
        if request.method == 'GET':
               
                return render(request, 'consulta/cadastrar_consulta.html', {'pacientes':pacientes, 'medicos':medicos, 'consulta':consulta})
        elif request.method == 'POST':
                paciente = request.POST.get('paciente')
                paciente = Paciente.objects.get(nome=paciente)
                medico = request.POST.get('medico')
                medico = Medico.objects.get(nome = medico)
                print(paciente)
                tipo_consulta = request.POST.get('tipo_consulta')
                valor = request.POST.get('valor')
                horario = request.POST.get('hora')
                descricao = request.POST.get('descricao')
                
                if not paciente or not medico or not valor or horario or not descricao: 
                        print('aqui')
                        messages.add_message(request, constants.ERROR, 'Não pode deixar campos em Branco!!')
                        return redirect('cadastrar_consulta')
                
                nova_consulta = MarcarConsulta(
                        paciente_id = paciente.id,
                        medico_id = medico.id,
                        valor = valor,
                        descricao = descricao,
                        horario = horario
                )
               
                nova_consulta.save()
                messages.add_message(request, constants.SUCCESS, 'Consulta Marcada com Sucesso!!')
                return render(request, 'consulta/cadastrar_consulta.html', {'pacientes':pacientes, 'medicos':medicos})
# def cadastrar_consulta(request):
#         if request.method == 'GET':
#                 forms = MarcaConsultaModelForm()  
#                 return render(request, 'consulta/cadastrar_consulta.html',
#                               {'forms':forms})
                
#         elif request.method == 'POST':
#                 forms = MarcaConsultaModelForm(request.POST) 
               
#                 if forms.is_valid():
#                         #if Medico.objects.filter(medico.horario)
#                         forms.save() 
#                         messages.add_message(request, constants.SUCCESS, 'Consulta Marcada com Sucesso!!')
#                         return redirect('cadastrar_consulta')
#                 else:
#                         return render(request, 'consulta/cadastrar_consulta.html',{'forms':forms})
# @login_required
# def editar_consulta(request, id):
#         consuta = MarcarConsulta.objects.get(id=id)
#         if request.method == 'POST':
#                 forms = MarcaConsultaModelForm(request.POST or None, instance=consuta)
#                 if forms.is_valid():
#                         forms.save()
#                         messages.add_message(request, constants.SUCCESS, 'Consulta editada Sucesso!!')
#                         return redirect('cadastrar_consulta')
#         else:
#                 forms = MarcaConsultaModelForm(instance=consuta)
#         return render(request, 'consulta/cadastrar_consulta.html',{'forms':forms, 'consulta':consulta})
# @login_required
# def listar_consultas(request):

#       if request.GET.get('termo'):
#               termo = request.GET.get('termo')
#               consultas = MarcarConsulta.objects.filter(Q(paciente__nome__icontains=termo) | 
#                                                         Q(medico__nome__icontains=termo)|
#                                                         Q(data__icontains=termo))
#       else:
#               consultas = MarcarConsulta.objects.order_by('-id', '-paciente')
#       paginator = Paginator(consultas, 10)  
#       page = request.GET.get('page')
#       consultas = paginator.get_page(page)
#       return render(request, 'consulta/consultas.html', {'consultas':consultas})
# @login_required
# def excluir_consulta(request, id):
#         consulta = get_object_or_404(MarcarConsulta, id=id)
#         consulta.delete()
#         messages.add_message(request, constants.SUCCESS, 'Consulta Excluida Sucesso!!')
#         return redirect('listar_consultas')