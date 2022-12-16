from django.urls import path


from . import views

urlpatterns = [
   path('cadastrar_consulta/', views.cadastrar_consulta, name='cadastrar_consulta'),
   path('listar_consultas/', views.listar_consultas, name='listar_consultas'),
   path('editar_consulta/<int:id>', views.editar_consulta, name='editar_consulta'),
   path('excluir_consulta/<int:id>', views.excluir_consulta, name='excluir_consulta'),
   path('update_consulta/<int:id>', views.update_consulta, name='update_consulta'),
  
]
