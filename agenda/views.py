from django.shortcuts import render, HttpResponse
from consulta.models import MarcarConsulta
from medico.models import Medico

# Create your views here.
def agenda(request):
    if request.method == 'GET':
        medico = Medico.objects.all()
        horario = MarcarConsulta.objects.all().order_by('-medico','horario')
        return render(request, 'agendamentos.html', {'medico':medico, 'horario':horario})