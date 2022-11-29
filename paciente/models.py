from django.db import models

# Create your models here.
class Convenio(models.Model):
    nome = models.CharField(max_length=50)
    n_carteira = models.CharField(max_length=10)
    validade = models.DateField
    
    def __str__(self) -> str:
        return self.nome
    
class Paciente(models.Model):
    nome = models.CharField(max_length=60)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=12)
    email = models.EmailField(default='')
    telefone = models.CharField(max_length=12)
    endereco = models.CharField(max_length=200, default='')
    convenio = models.ForeignKey(Convenio,null=True, on_delete=models.SET_NULL, default='')
    
    def __str__(self) -> str:
        return self.nome
