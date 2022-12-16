from django.db import models
from users.models import Users
from paciente.models import Paciente
from medico.models import Medico

# Create your models here.
class MarcarConsulta(models.Model):
    
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    #data  = models.DateField(blank=True, null=True)
    descricao = models.TextField()
    valor = models.FloatField()
      
    
    horario = models.DateTimeField() 
   
    def __str__(self) -> str:
        return self.paciente.nome