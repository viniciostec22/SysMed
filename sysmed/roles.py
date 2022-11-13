import imp
from rolepermissions.roles import AbstractUserRole

class Gerente(AbstractUserRole):
    available_permissions = {
        'cadastrar_usuarios':True,
        'cadastrar_medico':True,
        'cadastrar_recpcionista':True,
    }
    
class Recepcionista(AbstractUserRole):
    available_permissions = {
        'agendar_consulta':True,
    }
    
class Medico(AbstractUserRole):
    available_permissions = {
        'cadastrar_diagnostico':True,
    }