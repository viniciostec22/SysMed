from django.db import models
from users.models import Users
from paciente.models import Paciente
from medico.models import Medico

# Create your models here.
class MarcarConsulta(models.Model):
    
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    data  = models.DateField()
    descricao = models.TextField()
    valor = models.FloatField()
      
    HORARIOS = (
        ("1", "07:00 ás 08:00"),
        ("2", "08:00 ás 09:00"),
        ("3", "09:00 ás 10:00"),
        ("4", "10:00 ás 11:00"),
        ("5", "11:00 ás 12:00"),
    )
    horario = models.CharField(max_length=10, choices=HORARIOS) # type: ignore  
   
    def __str__(self) -> str:
        return self.paciente.nome