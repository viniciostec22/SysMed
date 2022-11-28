from django.urls import path


from . import views

urlpatterns = [
   path('cadastrar_paciente/', views.cadastrar_paciente, name='cadastrar_paciente')
  
]
