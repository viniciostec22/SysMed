from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser

class Cargo(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome
    
class Users(AbstractUser):
    #choices_cargo = (('R', 'Recepcionista'), ('M', 'Medico'), ('G', 'Gerente'))
    
    #cargo = models.CharField(max_length=1, choices=choices_cargo)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, null=True)
    cpf = models.CharField(max_length=12, blank=True)
    data_nascimento = models.DateField(blank=True, null=True)