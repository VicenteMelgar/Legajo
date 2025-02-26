from django import forms
from .models import Empleado, Legajo, InfoPersonal, Seleccion, Vinculo, Induccion, Prueba, Colegiatura, EstudiosRealizados, Curso, Experiencia, Movimientos, Retencion, Compensaciones, Evaluacion, Progresion, Desplazamiento, Reconocimiento, Laboral, Seguridad, Desvinculacion, Subespecialidad

class EmpleadoForm(forms.ModelForm):
  class Meta:
    model = Empleado
    fields = '__all__'
    widgets = {
            'apellido_paterno': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_materno': forms.TextInput(attrs={'class': 'form-control'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'carnet_extranjeria': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-select'}),
            'estado_civil': forms.Select(attrs={'class': 'form-select'}),
            'departamento': forms.Select(attrs={'class': 'form-select'}),
            'provincia': forms.TextInput(attrs={'class': 'form-control'}),
            'distrito': forms.TextInput(attrs={'class': 'form-control'}),
            'domicilio': forms.TextInput(attrs={'class': 'form-control'}),
            'cipss': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class LegajoForm(forms.ModelForm):
    class Meta:
        model = Legajo
        fields = ['empleado', 'regimen_laboral', 'activo']
        widgets = {
            'empleado': forms.Select(attrs={'class': 'form-control'}),
            'regimen_laboral': forms.Select(attrs={'class': 'form-control'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class InfoPersonalForm(forms.ModelForm):
    class Meta:
        model = InfoPersonal
        fields = ['legajo', 'documento', 'fecha', 'pdf']
        widgets = {
          'legajo': forms.Select(attrs={'class': 'form-select'}),
          'documento': forms.Select(attrs={'class': 'form-select'}),
          'fecha': forms.DateInput(attrs={'class': 'form-control'}),
          'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class SeleccionForm(forms.ModelForm):
    class Meta:
        model = Seleccion
        fields = ['legajo', 'documento', 'fecha', 'descripcion', 'pdf']
        widgets = {
          'legajo': forms.SelectMultiple(attrs={'class': 'form-select'}),
          'documento': forms.Select(attrs={'class': 'form-select'}),
          'fecha': forms.DateInput(attrs={'class': 'form-control'}),
          'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
          'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
                
class VinculoForm(forms.ModelForm):
    class Meta:
        model = Vinculo
        fields = '__all__'
        widgets = {
          'legajo': forms.SelectMultiple(attrs={'class': 'form-select'}),
          'documento': forms.Select(attrs={'class': 'form-select'}),
          'numero': forms.TextInput(attrs={'class': 'form-control'}),
          'tipo': forms.Select(attrs={'class': 'form-select'}),
          'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
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
    fields = ['legajo', 'documento', 'fecha', 'pdf']
    widgets = {
      'legajo': forms.SelectMultiple(attrs={'class': 'form-select'}),
      'documento': forms.Select(attrs={'class': 'form-select'}),
      'fecha': forms.DateInput(attrs={'class': 'form-control'}),
      'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
    }

class PruebaForm(forms.ModelForm):
  class Meta:
    model = Prueba
    fields = ['legajo', 'documento', 'fecha', 'pdf']
    widgets = {
      'legajo': forms.Select(attrs={'class': 'form-select'}),
      'documento': forms.Select(attrs={'class': 'form-select'}),
      'fecha': forms.DateInput(attrs={'class': 'form-control'}),
      'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
    }
         
class ColegiaturaForm(forms.ModelForm):
  class Meta:
    model = Colegiatura
    fields = ['legajo', 'documento', 'fecha_emision', 'fecha_vigencia', 'pdf']
    widgets = {
      'legajo': forms.Select(attrs={'class': 'form-select'}),
      'documento': forms.Select(attrs={'class': 'form-select'}),
      'fecha_emision': forms.DateInput(attrs={'class': 'form-control'}),
      'fecha_vigencia': forms.DateInput(attrs={'class': 'form-control'}),
      'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
    }
              
class EstudiosRealizadosForm(forms.ModelForm):
    class Meta:
        model = EstudiosRealizados
        fields = '__all__'
        widgets = {
          'legajo': forms.Select(attrs={'class': 'form-select'}),
          'inicio': forms.DateInput(attrs={'class': 'form-control'}),
          'fin': forms.DateInput(attrs={'class': 'form-control'}),
          'grado_instruccion': forms.Select(attrs={'class': 'form-select'}),
          'especialidad': forms.TextInput(attrs={'class': 'form-control'}),
          'cod_especialidad': forms.TextInput(attrs={'class': 'form-control'}),
          'fecha_expedicion': forms.DateInput(attrs={'class': 'form-control'}),
          'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class SubespecialidadForm(forms.ModelForm):
    class Meta:
        model = Subespecialidad
        fields = '__all__'
        widgets = {
          'legajo': forms.Select(attrs={'class': 'form-select'}),
          'inicio': forms.DateInput(attrs={'class': 'form-control'}),
          'fin': forms.DateInput(attrs={'class': 'form-control'}),
          'documento': forms.Select(attrs={'class': 'form-select'}),
          'mencion': forms.TextInput(attrs={'class': 'form-control'}),
          'cod_especialidad': forms.TextInput(attrs={'class': 'form-control'}),
          'fecha_expedicion': forms.DateInput(attrs={'class': 'form-control'}),
          'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class CursoForm(forms.ModelForm):
  class Meta:
    model = Curso
    fields = ['legajo', 'documento', 'inicio', 'fin', 'descripcion', 'duracion', 'fecha_expedicion', 'pdf']
    widgets = {
      'legajo': forms.Select(attrs={'class': 'form-select'}),
      'documento': forms.Select(attrs={'class': 'form-select'}),
      'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
      'inicio': forms.DateInput(attrs={'class': 'form-control'}),
      'fin': forms.DateInput(attrs={'class': 'form-control'}),
      'duracion': forms.TextInput(attrs={'class': 'form-control'}),
      'fecha_expedicion': forms.DateInput(attrs={'class': 'form-control'}),
      'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
    }
     
class ExperienciaForm(forms.ModelForm):
  class Meta:
    model = Experiencia
    fields = ['legajo', 'institucion', 'documento', 'cargo', 'descripcion', 'fecha_inicio', 'fecha_fin', 'fecha_expedicion', 'pdf']
    widgets = {
      'legajo': forms.Select(attrs={'class': 'form-select'}),
      'institucion': forms.TextInput(attrs={'class': 'form-control'}),
      'documento': forms.Select(attrs={'class': 'form-select'}),
      'cargo': forms.TextInput(attrs={'class': 'form-control'}),
      'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
      'fecha_inicio': forms.DateInput(attrs={'class': 'form-control'}),
      'fecha_fin': forms.DateInput(attrs={'class': 'form-control'}),
      'fecha_expedicion': forms.DateInput(attrs={'class': 'form-control'}),
      'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
    }
      
class MovimientosForm(forms.ModelForm):
    class Meta:
        model = Movimientos
        fields = '__all__'
        widgets = {
          'legajo': forms.Select(attrs={'class': 'form-select'}),
          'documento': forms.TextInput(attrs={'class': 'form-control'}),
          'tipo': forms.Select(attrs={'class': 'form-select'}),
          'motivo': forms.TextInput(attrs={'class': 'form-control'}),
          'asunto': forms.TextInput(attrs={'class': 'form-control'}),
          'desde': forms.DateInput(attrs={'class': 'form-control'}),
          'hasta': forms.DateInput(attrs={'class': 'form-control'}),
          'total_dias': forms.TextInput(attrs={'class': 'form-control'}),
          'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class RetencionForm(forms.ModelForm):
    class Meta:
        model = Retencion
        fields = ['legajo', 'documento', 'fecha', 'pdf']
        widgets = {
          'legajo': forms.Select(attrs={'class': 'form-select'}),
          'documento': forms.Select(attrs={'class': 'form-select'}),
          'fecha': forms.DateInput(attrs={'class': 'form-control'}),
          'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class CompensacionesForm(forms.ModelForm):
    class Meta:
        model = Compensaciones
        fields = '__all__'
        widgets = {
          'legajo': forms.Select(attrs={'class': 'form-select'}),
          'resolucion': forms.TextInput(attrs={'class': 'form-control'}),
          'fecha': forms.DateInput(attrs={'class': 'form-control'}),
          'motivo': forms.Select(attrs={'class': 'form-select'}),
          'porcentaje': forms.TextInput(attrs={'class': 'form-control'}),
          'anios': forms.TextInput(attrs={'class': 'form-control'}),
          'meses': forms.TextInput(attrs={'class': 'form-control'}),
          'dias': forms.TextInput(attrs={'class': 'form-control'}),
          'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class EvaluacionForm(forms.ModelForm):
    class Meta:
        model = Evaluacion
        fields = ['legajo', 'periodo', 'fecha', 'documento', 'puntaje', 'pdf']
        widgets = {
          'legajo': forms.Select(attrs={'class': 'form-select'}),
          'periodo': forms.TextInput(attrs={'class': 'form-control'}),
          'fecha': forms.DateInput(attrs={'class': 'form-control'}),
          'documento': forms.Select(attrs={'class': 'form-select'}),
          'puntaje': forms.TextInput(attrs={'class': 'form-control'}),
          'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class ProgresionForm(forms.ModelForm):
    class Meta:
        model = Progresion
        fields = ['legajo', 'documento', 'numero', 'motivo', 'fecha', 'nivel', 'pdf']
        widgets = {
          'legajo': forms.Select(attrs={'class': 'form-select'}),
          'documento': forms.Select(attrs={'class': 'form-select'}),
          'numero': forms.TextInput(attrs={'class': 'form-control'}),
          'motivo': forms.Select(attrs={'class': 'form-select'}),
          'fecha': forms.DateInput(attrs={'class': 'form-control'}),
          'nivel': forms.SelectMultiple(attrs={'class': 'form-select'}),
          'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class DesplazamientoForm(forms.ModelForm):
    class Meta:
        model = Desplazamiento
        fields = '__all__'
        widgets = {
          'legajo': forms.Select(attrs={'class': 'form-select'}),
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
          'legajo': forms.Select(attrs={'class': 'form-select'}),
          'documento_reconocimiento': forms.Select(attrs={'class': 'form-select'}),
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
          'legajo': forms.Select(attrs={'class': 'form-select'}),
          'documento_laboral': forms.Select(attrs={'class': 'form-select'}),
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
          'legajo': forms.Select(attrs={'class': 'form-select'}),
          'documento': forms.Select(attrs={'class': 'form-select'}),
          'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
          'fecha': forms.DateInput(attrs={'class': 'form-control'}),
          'fecha_vigencia': forms.DateInput(attrs={'class': 'form-control'}),
          'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        
class DesvinculacionForm(forms.ModelForm):
    class Meta:
        model = Desvinculacion
        fields = '__all__'
        widgets = {
          'legajo': forms.Select(attrs={'class': 'form-select'}),
          'documento': forms.Select(attrs={'class': 'form-select'}),
          'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
          'fecha': forms.DateInput(attrs={'class': 'form-control'}),
          'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }