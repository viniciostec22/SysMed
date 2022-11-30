from django.urls import path


from . import views

urlpatterns = [
   path('cadastrar_consulta/', views.cadastrar_consulta, name='cadastrar_consulta')
  
]
