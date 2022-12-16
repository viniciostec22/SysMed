from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
import consulta
from paciente.models import Paciente
from medico.models import Medico
from django.db.models import Q
from .models import MarcarConsulta
from django.contrib.messages import constants
from django.contrib import messages
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def cadastrar_consulta(request):
        pacientes = Paciente.objects.all()
        medicos = Medico.objects.all()
        consulta = MarcarConsulta.objects.all()
        if request.method == 'GET':
               
                return render(request, 'consulta/cadastrar_consulta.html', {'pacientes':pacientes, 'medicos':medicos, 'consulta':consulta})
        elif request.method == 'POST':
                
                paciente = request.POST.get('paciente')
                if paciente == '':
                        messages.add_message(request, constants.ERROR, 'Campo Nome do paciente é obrigatorio!!')
                        return redirect(reverse('cadastrar_consulta'))
                paciente = Paciente.objects.get(nome=paciente)
                medico = request.POST.get('medico')
                if medico== '':
                        messages.add_message(request, constants.ERROR, 'Campo Medico Obrigatorio!!')
                        return redirect(reverse('cadastrar_consulta'))
                medico = Medico.objects.get(nome = medico)
        
                
                valor = request.POST.get('valor')
                horario = request.POST.get('hora')
                descricao = request.POST.get('descricao')
                
                if not  valor or not horario or not descricao: 
                        messages.add_message(request, constants.ERROR, 'Não pode deixar campos em Branco!!')
                        return redirect(reverse('cadastrar_consulta'))
                
                if MarcarConsulta.objects.filter(medico=medico, horario=horario):
                        messages.add_message(request, constants.ERROR, 'Horario não esta disponivel para o medico!!')
                        return redirect(reverse('cadastrar_consulta'))
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
@login_required
def editar_consulta(request, id):
        
        pacientes = Paciente.objects.filter(id=id)
        consulta = get_object_or_404(MarcarConsulta, id=id)
        return render(request, 'consulta/editar_consulta.html', {'pacientes':pacientes,'consulta':consulta})
@login_required                
def update_consulta(request, id):
        paciente = request.POST.get('paciente')
        if paciente == '':
                messages.add_message(request, constants.ERROR, 'Campo Nome do paciente é obrigatorio!!')
                return redirect(f'/consulta/editar_consulta/{id}')
        paciente = Paciente.objects.get(nome=paciente)
    
        medico = request.POST.get('medico')
        if medico== '':
                messages.add_message(request, constants.ERROR, 'Campo Medico Obrigatorio!!')
                return redirect(reverse('editar_consulta'))
        medico = Medico.objects.get(nome = medico)
        
                
        valor = request.POST.get('valor')
        horario = request.POST.get('hora')
        descricao = request.POST.get('descricao')
        
        consulta = MarcarConsulta.objects.get(id=id)
        
        consulta.paciente_id = paciente
        consulta.medico_id = medico
        consulta.valor = valor
        consulta.horario = horario
        consulta.descricao = descricao
        
        if not  valor or not horario or not descricao: 
                messages.add_message(request, constants.ERROR, 'Não pode deixar campos em Branco!!')
                return redirect(f'/consulta/editar_consulta/{id}')
        if MarcarConsulta.objects.filter(medico=medico, horario=horario):
                messages.add_message(request, constants.ERROR, 'Horario não esta disponivel para o medico!!')
                return redirect(f'/consulta/editar_consulta/{id}')
        consulta.save()
        messages.add_message(request, constants.SUCCESS, 'Consulta auterada com sucesso!!')        
        return redirect(reverse('listar_consultas'))
@login_required
def listar_consultas(request):

      if request.GET.get('termo'):
              termo = request.GET.get('termo')
              consultas = MarcarConsulta.objects.filter(Q(paciente__nome__icontains=termo) | 
                                                        Q(medico__nome__icontains=termo)|
                                                        Q(data__icontains=termo))
      else:
              consultas = MarcarConsulta.objects.order_by('-id', '-paciente')
      paginator = Paginator(consultas, 10)  
      page = request.GET.get('page')
      consultas = paginator.get_page(page)
      return render(request, 'consulta/consultas.html', {'consultas':consultas})
@login_required
def excluir_consulta(request, id):
        consulta = get_object_or_404(MarcarConsulta, id=id)
        consulta.delete()
        messages.add_message(request, constants.SUCCESS, 'Consulta Excluida Sucesso!!')
        return redirect('listar_consultas')