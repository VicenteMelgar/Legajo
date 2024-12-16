from django import forms
from .models import DatosPersonales

class DatosPersonalesForm(forms.ModelForm):
  class Meta:
    model = DatosPersonales
    fields = ('apellido_paterno', 'apellido_materno', 'nombres', 'dni')