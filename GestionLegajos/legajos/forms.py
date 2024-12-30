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
        fields = '__all__'
        widgets = {
          'empleado': forms.SelectMultiple(attrs={'class': 'form-select'}),
          'documento': forms.Select(attrs={'class': 'form-select'}),
          'numero': forms.TextInput(attrs={'class': 'form-control'}),
          'tipo': forms.Select(attrs={'class': 'form-select'}),
          'asunto': forms.TextInput(attrs={'class': 'form-control'}),
          'fecha': forms.DateInput(attrs={'class': 'form-control'}),
          'fecha_vigencia': forms.DateInput(attrs={'class': 'form-control'}),
          'fecha_fin': forms.DateInput(attrs={'class': 'form-control'}),
          'dependencia': forms.Select(attrs={'class': 'form-select'}),
          'cargo': forms.SelectMultiple(attrs={'class': 'form-select'}),
          'nivel': forms.SelectMultiple(attrs={'class': 'form-select'}),
          'plaza': forms.SelectMultiple(attrs={'class': 'form-select'}),
          'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        
class EstudiosRealizadosForm(forms.ModelForm):
    class Meta:
        model = EstudiosRealizados
        fields = '__all__'
        widgets = {
          'empleado': forms.Select(attrs={'class': 'form-select'}),
          'inicio': forms.DateInput(attrs={'class': 'form-control'}),
          'fin': forms.DateInput(attrs={'class': 'form-control'}),
          'grado_instruccion': forms.TextInput(attrs={'class': 'form-control'}),
          'especialidad': forms.TextInput(attrs={'class': 'form-control'}),
          'sub_especialidad': forms.TextInput(attrs={'class': 'form-control'}),
          'cod_especialidad': forms.TextInput(attrs={'class': 'form-control'}),
          'fecha_expedicion': forms.DateInput(attrs={'class': 'form-control'}),
          'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        
class AusenciasMeritosDemeritosForm(forms.ModelForm):
    class Meta:
        model = AusenciasMeritosDemeritos
        fields = '__all__'
        widgets = {
          'empleado': forms.Select(attrs={'class': 'form-select'}),
          'resolucion': forms.TextInput(attrs={'class': 'form-control'}),
          'motivo': forms.TextInput(attrs={'class': 'form-control'}),
          'asunto': forms.TextInput(attrs={'class': 'form-control'}),
          'desde': forms.DateInput(attrs={'class': 'form-control'}),
          'hasta': forms.DateInput(attrs={'class': 'form-control'}),
          'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class BonificacionPersonalForm(forms.ModelForm):
    class Meta:
        model = BonificacionPersonal
        fields = '__all__'
        widgets = {
          'empleado': forms.Select(attrs={'class': 'form-select'}),
          'resolucion': forms.TextInput(attrs={'class': 'form-control'}),
          'fecha': forms.DateInput(attrs={'class': 'form-control'}),
          'motivo': forms.TextInput(attrs={'class': 'form-control'}),
          'porcentaje': forms.TextInput(attrs={'class': 'form-control'}),
          'anios': forms.TextInput(attrs={'class': 'form-control'}),
          'meses': forms.TextInput(attrs={'class': 'form-control'}),
          'dias': forms.TextInput(attrs={'class': 'form-control'}),
          'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class TiempodeServiciosForm(forms.ModelForm):
    class Meta:
        model = TiempodeServicios
        fields = '__all__'
        widgets = {
          'empleado': forms.Select(attrs={'class': 'form-select'}),
          'resolucion': forms.TextInput(attrs={'class': 'form-control'}),
          'desde': forms.DateInput(attrs={'class': 'form-control'}),
          'hasta': forms.DateInput(attrs={'class': 'form-control'}),
          'anios': forms.TextInput(attrs={'class': 'form-control'}),
          'meses': forms.TextInput(attrs={'class': 'form-control'}),
          'dias': forms.TextInput(attrs={'class': 'form-control'}),
          'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class PensionistaSobrevivienteForm(forms.ModelForm):
    class Meta:
        model = PensionistaSobreviviente
        fields = '__all__'
        widgets = {
          'empleado': forms.Select(attrs={'class': 'form-select'}),
          'resolucion': forms.TextInput(attrs={'class': 'form-control'}),
          'fecha': forms.DateInput(attrs={'class': 'form-control'}),
          'apellido_paterno': forms.TextInput(attrs={'class': 'form-control'}),
          'apellido_materno': forms.TextInput(attrs={'class': 'form-control'}),
          'nombres': forms.TextInput(attrs={'class': 'form-control'}),
          'dni': forms.TextInput(attrs={'class': 'form-control'}),
          'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

