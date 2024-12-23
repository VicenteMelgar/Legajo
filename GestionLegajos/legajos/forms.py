from django import forms
from .models import DatosPersonales, ServiciosPrestados, AusenciasMeritosDemeritos, BonificacionPersonal, TiempodeServicios, PensionistaSobreviviente, EstudiosRealizados

class DatosPersonalesForm(forms.ModelForm):
  class Meta:
    model = DatosPersonales
    fields = '__all__'
    widgets = {
            'apellido_paterno': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_materno': forms.TextInput(attrs={'class': 'form-control'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'carnet_extranjeria': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-select'}),
            'estado_civil': forms.Select(attrs={'class': 'form-select'}),
            'modalidad': forms.Select(attrs={'class': 'form-select'}),
            'departamento': forms.Select(attrs={'class': 'form-select'}),
            'provincia': forms.TextInput(attrs={'class': 'form-control'}),
            'distrito': forms.TextInput(attrs={'class': 'form-control'}),
            'domicilio': forms.TextInput(attrs={'class': 'form-control'}),
            'cipss': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class ServiciosPrestadosForm(forms.ModelForm):
    class Meta:
        model = ServiciosPrestados
        fields = ['empleado', 'documento', 'numero', 'tipo', 'asunto', 'fecha', 'fecha_vigencia', 'dependencia', 
                  'cargo', 'nivel', 'plaza', 'pdf']
        widgets = {
          'empleado': forms.SelectMultiple(attrs={'class': 'form-select'}),
          'documento': forms.Select(attrs={'class': 'form-select'}),
          'numero': forms.TextInput(attrs={'class': 'form-control'}),
          'tipo': forms.Select(attrs={'class': 'form-select'}),
          'asunto': forms.TextInput(attrs={'class': 'form-control'}),
          'fecha': forms.DateInput(attrs={'class': 'form-control'}),
          'fecha_vigencia': forms.DateInput(attrs={'class': 'form-control'}),
          'dependencia': forms.Select(attrs={'class': 'form-select'}),
          'cargo': forms.SelectMultiple(attrs={'class': 'form-select'}),
          'nivel': forms.SelectMultiple(attrs={'class': 'form-select'}),
          'plaza': forms.SelectMultiple(attrs={'class': 'form-select'}),
          'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        
class AusenciasMeritosDemeritosForm(forms.ModelForm):
    class Meta:
        model = AusenciasMeritosDemeritos
        fields = '__all__'

class BonificacionPersonalForm(forms.ModelForm):
    class Meta:
        model = BonificacionPersonal
        fields = '__all__'

class TiempodeServiciosForm(forms.ModelForm):
    class Meta:
        model = TiempodeServicios
        fields = '__all__'

class PensionistaSobrevivienteForm(forms.ModelForm):
    class Meta:
        model = PensionistaSobreviviente
        fields = '__all__'

class EstudiosRealizadosForm(forms.ModelForm):
    class Meta:
        model = EstudiosRealizados
        fields = '__all__'