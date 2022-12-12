import imp
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Users
from rolepermissions.roles import assign_role

@receiver(post_save, sender=Users)
def define_permissoes(sender, instance, created, **kwargs):
    if created:
        if instance.cargo__nome == "Recepcionista":
            assign_role(instance, 'Recepcionista')
        elif instance.cargo__nome == "Gerente":
            assign_role(instance, 'gerenete')
        elif instance.cargo__nome == "medico":
            assign_role(instance, 'medico')