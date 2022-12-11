from dataclasses import field
from pyexpat import model
from django.core.exceptions import ValidationError
from django import forms

from medico.models import Medico
from .models import MarcarConsulta

class MarcaConsultaModelForm(forms.ModelForm):
    class Meta:
        model = MarcarConsulta
        fields = '__all__'
        
    def clean_horario(self):
        horario = self.cleaned_data['horario']
        
        if MarcarConsulta.objects.filter(horario=horario).exists():
            raise ValidationError('Horario indisponivel')
        else:
            return horario
    

    
    