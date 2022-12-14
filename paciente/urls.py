from django.urls import path


from . import views

urlpatterns = [
   path('cadastrar_paciente/', views.cadastrar_paciente, name='cadastrar_paciente'),
   path('listar_pacientes/', views.lista_pacientes, name='listar_pacientes'),
   path('delete_paciente/<int:id>', views.delete_paciente, name="deleta_paciente"),
   path('editar_paceinte/<int:id>', views.editar_paciente, name="editar_paciente"),
   path('update_paceinte/<int:id>', views.update, name="update_paciente"),
  
]
