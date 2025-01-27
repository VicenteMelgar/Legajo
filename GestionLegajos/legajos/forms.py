from django import forms
from .models import DatosPersonales, InfoPersonal, Seleccion, Vinculo, Induccion, Prueba, Colegiatura, EstudiosRealizados, Curso, Experiencia, Movimientos, Retencion, Compensaciones, Evaluacion, Progresion, Desplazamiento, Reconocimiento, Laboral, Seguridad, Desvinculacion

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

class InfoPersonalForm(forms.ModelForm):
    class Meta:
        model = InfoPersonal
        fields = ['empleado', 'tipo_documento', 'pdf']
        widgets = {
          'empleado': forms.Select(attrs={'class': 'form-select'}),
          'tipo_documento': forms.Select(attrs={'class': 'form-select'}),
          'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class SeleccionForm(forms.ModelForm):
    class Meta:
        model = Seleccion
        fields = ['empleado', 'tipo_documento', 'descripcion', 'pdf']
        widgets = {
          'empleado': forms.SelectMultiple(attrs={'class': 'form-select'}),
          'tipo_documento': forms.Select(attrs={'class': 'form-select'}),
          'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
          'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
                
class VinculoForm(forms.ModelForm):
    class Meta:
        model = Vinculo
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
          'cargo': forms.SelectMultiple(attrs={'class': 'form-select'}),
          'nivel': forms.SelectMultiple(attrs={'class': 'form-select'}),
          'plaza': forms.SelectMultiple(attrs={'class': 'form-select'}),
          'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
 
class InduccionForm(forms.ModelForm):
  class Meta:
    model = Induccion
    fields = ['empleado', 'tipo_documento', 'pdf']
    widgets = {
      'empleado': forms.SelectMultiple(attrs={'class': 'form-select'}),
      'tipo_documento': forms.Select(attrs={'class': 'form-select'}),
      'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
    }

class PruebaForm(forms.ModelForm):
  class Meta:
    model = Prueba
    fields = ['empleado', 'tipo_documento', 'pdf']
    widgets = {
      'empleado': forms.Select(attrs={'class': 'form-select'}),
      'tipo_documento': forms.Select(attrs={'class': 'form-select'}),
      'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
    }
         
class ColegiaturaForm(forms.ModelForm):
  class Meta:
    model = Colegiatura
    fields = ['empleado', 'tipo_documento', 'fecha_emision', 'pdf']
    widgets = {
      'empleado': forms.Select(attrs={'class': 'form-select'}),
      'tipo_documento': forms.Select(attrs={'class': 'form-select'}),
      'fecha_emision': forms.DateInput(attrs={'class': 'form-control'}),
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

class CursoForm(forms.ModelForm):
  class Meta:
    model = Curso
    fields = ['empleado', 'tipo_documento', 'inicio', 'fin', 'descripcion', 'duracion_horas', 'fecha_expedicion', 'pdf']
    widgets = {
      'empleado': forms.Select(attrs={'class': 'form-select'}),
      'tipo_documento': forms.Select(attrs={'class': 'form-select'}),
      'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
      'inicio': forms.DateInput(attrs={'class': 'form-control'}),
      'fin': forms.DateInput(attrs={'class': 'form-control'}),
      'duracion_horas': forms.TextInput(attrs={'class': 'form-control'}),
      'fecha_expedicion': forms.DateInput(attrs={'class': 'form-control'}),
      'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
    }
     
class ExperienciaForm(forms.ModelForm):
  class Meta:
    model = Experiencia
    fields = ['empleado', 'tipo_documento', 'descripcion', 'inicio', 'fin', 'fecha_expedicion', 'pdf']
    widgets = {
      'empleado': forms.Select(attrs={'class': 'form-select'}),
      'tipo_documento': forms.Select(attrs={'class': 'form-select'}),
      'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
      'inicio': forms.DateInput(attrs={'class': 'form-control'}),
      'fin': forms.DateInput(attrs={'class': 'form-control'}),
      'fecha_expedicion': forms.DateInput(attrs={'class': 'form-control'}),
      'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
    }
      
class MovimientosForm(forms.ModelForm):
    class Meta:
        model = Movimientos
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

class RetencionForm(forms.ModelForm):
    class Meta:
        model = Retencion
        fields = ['empleado', 'tipo_documento', 'pdf']
        widgets = {
          'empleado': forms.Select(attrs={'class': 'form-select'}),
          'tipo_documento': forms.Select(attrs={'class': 'form-select'}),
          'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class CompensacionesForm(forms.ModelForm):
    class Meta:
        model = Compensaciones
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

class EvaluacionForm(forms.ModelForm):
    class Meta:
        model = Evaluacion
        fields = ['empleado', 'tipo_documento', 'pdf']
        widgets = {
          'empleado': forms.Select(attrs={'class': 'form-select'}),
          'tipo_documento': forms.Select(attrs={'class': 'form-select'}),
          'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class ProgresionForm(forms.ModelForm):
    class Meta:
        model = Progresion
        fields = ['empleado', 'tipo_documento', 'fecha', 'nivel', 'pdf']
        widgets = {
          'empleado': forms.Select(attrs={'class': 'form-select'}),
          'tipo_documento': forms.Select(attrs={'class': 'form-select'}),
          'fecha': forms.DateInput(attrs={'class': 'form-control'}),
          'nivel': forms.SelectMultiple(attrs={'class': 'form-select'}),
          'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class DesplazamientoForm(forms.ModelForm):
    class Meta:
        model = Desplazamiento
        fields = '__all__'
        widgets = {
          'empleado': forms.Select(attrs={'class': 'form-select'}),
          'documento': forms.Select(attrs={'class': 'form-select'}),
          'numero': forms.TextInput(attrs={'class': 'form-control'}),
          'tipo': forms.Select(attrs={'class': 'form-select'}),
          'asunto': forms.TextInput(attrs={'class': 'form-control'}),
          'fecha': forms.DateInput(attrs={'class': 'form-control'}),
          'fecha_vigencia': forms.DateInput(attrs={'class': 'form-control'}),
          'cargo': forms.SelectMultiple(attrs={'class': 'form-select'}),
          'nivel': forms.SelectMultiple(attrs={'class': 'form-select'}),
          'plaza': forms.SelectMultiple(attrs={'class': 'form-select'}),
          'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        
class ReconocimientoForm(forms.ModelForm):
    class Meta:
        model = Reconocimiento
        fields = '__all__'
        widgets = {
          'empleado': forms.Select(attrs={'class': 'form-select'}),
          'tipo_documento': forms.Select(attrs={'class': 'form-select'}),
          'documento': forms.Select(attrs={'class': 'form-select'}),
          'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
          'fecha': forms.DateInput(attrs={'class': 'form-control'}),
          'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class LaboralForm(forms.ModelForm):
    class Meta:
        model = Laboral
        fields = '__all__'
        widgets = {
          'empleado': forms.Select(attrs={'class': 'form-select'}),
          'tipo_documento': forms.Select(attrs={'class': 'form-select'}),
          'documento': forms.Select(attrs={'class': 'form-select'}),
          'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
          'fecha': forms.DateInput(attrs={'class': 'form-control'}),
          'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        
class SeguridadForm(forms.ModelForm):
    class Meta:
        model = Seguridad
        fields = '__all__'
        widgets = {
          'empleado': forms.Select(attrs={'class': 'form-select'}),
          'tipo_documento': forms.Select(attrs={'class': 'form-select'}),
          'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
          'fecha': forms.DateInput(attrs={'class': 'form-control'}),
          'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        
class DesvinculacionForm(forms.ModelForm):
    class Meta:
        model = Desvinculacion
        fields = '__all__'
        widgets = {
          'empleado': forms.Select(attrs={'class': 'form-select'}),
          'tipo_documento': forms.Select(attrs={'class': 'form-select'}),
          'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
          'fecha': forms.DateInput(attrs={'class': 'form-control'}),
          'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }