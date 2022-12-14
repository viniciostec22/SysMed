from pyexpat import model
from django.db import models

# Create your models here.
class Especialidades(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.nome
    
class Medico(models.Model):
  
    nome = models.CharField(max_length=50)
    especialidades = models.ForeignKey(Especialidades,  on_delete=models.CASCADE)
    crm = models.CharField(max_length=12)
    cpf = models.CharField(max_length=11)
    dta_nascimento = models.DateField()
    tel = models.CharField(max_length=11)
    endereco = models.CharField(max_length=150)
    
    def __str__(self) -> str:
        return self.nome