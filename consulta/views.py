from django.shortcuts import render, HttpResponse

# Create your views here.
def cadastrar_consulta(request):
    return render(request, 'consulta/cadastrar_consulta.html')