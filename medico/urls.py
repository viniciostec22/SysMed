from django.urls import path


from . import views

urlpatterns = [
 path('medico/', views.cadastra_medico, name='cadastra_medico'),
 
  
]
