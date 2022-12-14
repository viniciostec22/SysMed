from django.urls import path


from . import views

urlpatterns = [
 path('medico/', views.cadastra_medico, name='cadastra_medico'),
 path('editar_medico/<int:id>', views.editar_medico, name='editar_medico'),
 path('update_medico/<int:id>', views.medico_update, name='update_medico'),
 path('deletar_medico/<int:id>', views.deletar_medico, name='deletar_medico'),
 path('add-especialidade', views.add_especialidade, name='add_especialidade'),
 
  
]
