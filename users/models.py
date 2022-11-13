from calendar import c
from random import choices
from django.db import models
from django.contrib.auth.models import AbstractUser



class Users(AbstractUser):
    choices_cargo = (('R', 'Recepcionista'), ('M', 'Medico'), ('G', 'Gerente'))
    
    cargo = models.CharField(max_length=1, choices=choices_cargo)