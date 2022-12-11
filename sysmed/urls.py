
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('paciente/', include('paciente.urls')),
    path("consulta/", include('consulta.urls')),
    path('medico/', include('medico.urls')),
    path('agenda/', include('agenda.urls')),
   
]
