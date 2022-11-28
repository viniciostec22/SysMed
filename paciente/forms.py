from django import forms 
from .models import Paciente, Convenio
from django.forms.widgets import ClearableFileInput

class PacienteModelForm(forms.ModelForm):
    #requerid_css_class = 'requerid'
    #img = forms.ImageField(widget=ClearableFileInput, required=False)
    class Meta:
        model = Paciente
        fields = '__all__'