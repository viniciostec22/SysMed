from django.shortcuts import render, HttpResponse

def cadastra_medico(request):
    return render(request, 'medico/cadastra_medico.html')