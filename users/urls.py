from django.urls import path


from . import views

urlpatterns = [
    path('cadastrar_usuario/', views.cadastro_usuario, name="cadastrar_usuario"),
    path('', views.login, name='login'),
    path('logout/', views.logout, name="logout"),
    path('home/', views.plataforma, name="plataforma"),
    path('excluir_usuario/<str:id>/', views.exluir_usuario, name="excluir_usuario"),
    path('editar_usuario/<str:id>/', views.editar_usuario, name="editar_usuario"),
    path('add_cargo/', views.add_cargo, name="add_cargo"),
   
  
]
