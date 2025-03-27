from django import forms
from .models import Empleado, OficinaHistorial, Legajo, Resolucion, InfoPersonal, Seleccion, Vinculo, Induccion, Prueba, Habilitacion, Serum, EstudiosRealizados, Curso, Experiencia, Movimientos, Retencion, Compensaciones, Evaluacion, Reconocimiento, Laboral, Seguridad, Desvinculacion, Subespecialidad, Otro

class EmpleadoForm(forms.ModelForm):
  class Meta:
    model = Empleado
    fields = '__all__'
    widgets = {
            'apellido_paterno': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_materno': forms.TextInput(attrs={'class': 'form-control'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'documento_identidad': forms.Select(attrs={'class': 'form-select'}),
            'numero_documento': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-select'}),
            'estado_civil': forms.Select(attrs={'class': 'form-select'}),
            'departamento': forms.Select(attrs={'class': 'form-select'}),
            'provincia': forms.TextInput(attrs={'class': 'form-control'}),
            'distrito': forms.TextInput(attrs={'class': 'form-control'}),
            'domicilio': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
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
    fields = '__all__'
    widgets = {
      'legajo': forms.Select(attrs={'class': 'form-select'}),
      'documento': forms.Select(attrs={'class': 'form-select'}),
      'documento_otro': forms.TextInput(attrs={'class': 'form-control'}),
      'fecha': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
      'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
    }

class ResolucionForm(forms.ModelForm):
  class Meta:
    model = Resolucion
    fields = '__all__'
    widgets = {
      'documento': forms.Select(attrs={'class': 'form-select'}),
      'numero': forms.TextInput(attrs={'class': 'form-control'}),
      'tipo': forms.Select(attrs={'class': 'form-select'}),
      'otro': forms.TextInput(attrs={'class': 'form-control'}),
      'fecha': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
      'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
    }

class OficinaHistorialForm(forms.ModelForm):
  class Meta:
    model = OficinaHistorial
    fields = '__all__'
    widgets = {
      'empleado': forms.Select(attrs={'class': 'form-select'}),
      'resolucion': forms.Select(attrs={'class': 'form-select'}),
      'denominacion': forms.Select(attrs={'class': 'form-control'}),
      'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
      'fecha_fin': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
    }

class SeleccionForm(forms.ModelForm):
    class Meta:
        model = Seleccion
        fields = ['legajo', 'documento', 'documento_otro', 'descripcion', 'fecha', 'pdf']
        widgets = {
          'legajo': forms.SelectMultiple(attrs={'class': 'form-select'}),
          'documento': forms.Select(attrs={'class': 'form-select'}),
          'documento_otro': forms.TextInput(attrs={'class': 'form-control'}),
          'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
          'fecha': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
          'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
                
class VinculoForm(forms.ModelForm):
    class Meta:
        model = Vinculo
        fields = '__all__'
        widgets = {
          'legajo': forms.Select(attrs={'class': 'form-select'}),
          'tipo': forms.Select(attrs={'class': 'form-select'}),
          'resolucion': forms.Select(attrs={'class': 'form-select'}),
          'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        }
 
class InduccionForm(forms.ModelForm):
  class Meta:
    model = Induccion
    fields = ['legajo', 'documento', 'fecha', 'pdf']
    widgets = {
      'legajo': forms.SelectMultiple(attrs={'class': 'form-select'}),
      'documento': forms.Select(attrs={'class': 'form-select'}),
      'fecha': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
      'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
    }

class PruebaForm(forms.ModelForm):
  class Meta:
    model = Prueba
    fields = ['legajo', 'documento', 'fecha', 'pdf']
    widgets = {
      'legajo': forms.Select(attrs={'class': 'form-select'}),
      'documento': forms.Select(attrs={'class': 'form-select'}),
      'fecha': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
      'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
    }
         
class HabilitacionForm(forms.ModelForm):
  class Meta:
    model = Habilitacion
    fields = '__all__'
    widgets = {
      'legajo': forms.Select(attrs={'class': 'form-select'}),
      'registro': forms.TextInput(attrs={'class': 'form-select'}),
      'fecha_emision': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
      'fecha_vigencia': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
      'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
    }
              
class EstudiosRealizadosForm(forms.ModelForm):
    class Meta:
        model = EstudiosRealizados
        fields = '__all__'
        widgets = {
          'legajo': forms.Select(attrs={'class': 'form-select'}),
          'centro': forms.TextInput(attrs={'class': 'form-control'}),
          'inicio': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
          'fin': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
          'grado_instruccion': forms.Select(attrs={'class': 'form-select'}),
          'especialidad': forms.TextInput(attrs={'class': 'form-control'}),         
          'fecha_expedicion': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
          'colegiatura': forms.TextInput(attrs={'class': 'form-control'}),
          'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class SerumForm(forms.ModelForm):
  class Meta:
    model = Serum
    fields = '__all__'
    widgets = {
      'legajo': forms.Select(attrs={'class': 'form-select'}),
      'registro': forms.TextInput(attrs={'class': 'form-select'}),
      'fecha_emision': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
      'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
    }
    
class SubespecialidadForm(forms.ModelForm):
    class Meta:
        model = Subespecialidad
        fields = '__all__'
        widgets = {
          'legajo': forms.Select(attrs={'class': 'form-select'}),
          'centro': forms.TextInput(attrs={'class': 'form-control'}),
          'inicio': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
          'fin': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
          'documento': forms.Select(attrs={'class': 'form-select'}),
          'mencion': forms.TextInput(attrs={'class': 'form-control'}),
          'cod_especialidad': forms.TextInput(attrs={'class': 'form-control'}),
          'fecha_expedicion': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
          'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class CursoForm(forms.ModelForm):
  class Meta:
    model = Curso
    fields = '__all__'
    widgets = {
      'legajo': forms.Select(attrs={'class': 'form-select'}),
      'centro': forms.TextInput(attrs={'class': 'form-control'}),
      'documento': forms.Select(attrs={'class': 'form-select'}),
      'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
      'inicio': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
      'fin': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
      'horas': forms.TextInput(attrs={'class': 'form-control'}),
      'creditos': forms.TextInput(attrs={'class': 'form-control'}),
      'fecha_expedicion': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
      'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
    }
     
class ExperienciaForm(forms.ModelForm):
  class Meta:
    model = Experiencia
    fields = '__all__'
    widgets = {
      'legajo': forms.Select(attrs={'class': 'form-select'}),
      'institucion': forms.TextInput(attrs={'class': 'form-control'}),
      'documento': forms.Select(attrs={'class': 'form-select'}),
      'numero': forms.TextInput(attrs={'class': 'form-control'}),
      'cargo': forms.TextInput(attrs={'class': 'form-control'}),
      'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
      'fecha_fin': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
      'cargo2': forms.TextInput(attrs={'class': 'form-control'}),
      'fecha_inicio2': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
      'fecha_fin2': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
      'cargo3': forms.TextInput(attrs={'class': 'form-control'}),
      'fecha_inicio3': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
      'fecha_fin3': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
      'cargo4': forms.TextInput(attrs={'class': 'form-control'}),
      'fecha_inicio4': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
      'fecha_fin4': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
      'cargo5': forms.TextInput(attrs={'class': 'form-control'}),
      'fecha_inicio5': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
      'fecha_fin5': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
      'fecha_expedicion': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
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
          'desde': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
          'hasta': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
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
          'fecha': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
          'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class CompensacionesForm(forms.ModelForm):
    class Meta:
        model = Compensaciones
        fields = '__all__'
        widgets = {
          'legajo': forms.Select(attrs={'class': 'form-select'}),
          'documento': forms.Select(attrs={'class': 'form-select'}),
          'numero': forms.TextInput(attrs={'class': 'form-control'}),
          'motivo': forms.TextInput(attrs={'class': 'form-control'}),
          'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
          'fecha': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
          'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class EvaluacionForm(forms.ModelForm):
    class Meta:
        model = Evaluacion
        fields = '__all__'
        widgets = {
          'legajo': forms.Select(attrs={'class': 'form-select'}),
          'periodo': forms.Select(attrs={'class': 'form-control'}),
          'anio': forms.TextInput(attrs={'class': 'form-control'}),
          'puntaje': forms.TextInput(attrs={'class': 'form-control'}),
          'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
"""
class ProgresionForm(forms.ModelForm):
    class Meta:
        model = Progresion
        fields = '__all__'
        widgets = {
          'legajo': forms.Select(attrs={'class': 'form-select'}),
          'documento': forms.Select(attrs={'class': 'form-select'}),
          'numero': forms.TextInput(attrs={'class': 'form-control'}),
          'motivo': forms.TextInput(attrs={'class': 'form-control'}),
          'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
          'fecha': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
          'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
          'cargo': forms.Select(attrs={'class': 'form-select'}),
          'nivel': forms.Select(attrs={'class': 'form-select'}),
          'plaza': forms.TextInput(attrs={'class': 'form-control'}),
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
          'fecha': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
          'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
          'fecha_fin': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
          'condicion_laboral': forms.Select(attrs={'class': 'form-select'}),
          'grupo_ocupacional': forms.Select(attrs={'class': 'form-select'}),
          'cargo': forms.Select(attrs={'class': 'form-select'}),
          'nivel': forms.Select(attrs={'class': 'form-select'}),
          'plaza': forms.TextInput(attrs={'class': 'form-control'}),
          'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        } """
        
class ReconocimientoForm(forms.ModelForm):
    class Meta:
        model = Reconocimiento
        fields = '__all__'
        widgets = {
          'legajo': forms.Select(attrs={'class': 'form-select'}),
          'documento_reconocimiento': forms.Select(attrs={'class': 'form-select'}),
          'documento': forms.Select(attrs={'class': 'form-select'}),
          'numero': forms.TextInput(attrs={'class': 'form-control'}),
          'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
          'fecha': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
          'desde': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
          'hasta': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
          'total_dias': forms.TextInput(attrs={'class': 'form-control'}),
          'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class LaboralForm(forms.ModelForm):
    class Meta:
        model = Laboral
        fields = '__all__'
        widgets = {
          'legajo': forms.Select(attrs={'class': 'form-select'}),
          'documento': forms.TextInput(attrs={'class': 'form-control'}),
          'documento_laboral': forms.Select(attrs={'class': 'form-select'}),
          'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
          'fecha': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
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
          'fecha': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
          'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
          'fecha_fin': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
          'total_dias': forms.TextInput(attrs={'class': 'form-control'}),
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
          'fecha': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
          'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
  
"""        
class FinalForm(forms.ModelForm):
    class Meta:
        model = Final
        fields = '__all__'
        widgets = {
          'legajo': forms.SelectMultiple(attrs={'class': 'form-select'}),
          'documento': forms.Select(attrs={'class': 'form-select'}),
          'numero': forms.TextInput(attrs={'class': 'form-control'}),
          'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
          'fecha': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
          'fecha_fin': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
          'condicion_laboral': forms.Select(attrs={'class': 'form-select'}),
          'grupo_ocupacional': forms.Select(attrs={'class': 'form-select'}),
          'cargo': forms.Select(attrs={'class': 'form-select'}),
          'nivel': forms.Select(attrs={'class': 'form-select'}),
          'plaza': forms.TextInput(attrs={'class': 'form-control'}),
          'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        } """
        
class OtroForm(forms.ModelForm):
    class Meta:
        model = Otro
        fields = '__all__'
        widgets = {
          'legajo': forms.Select(attrs={'class': 'form-select'}),
          'documento': forms.TextInput(attrs={'class': 'form-control'}),
          'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
          'fecha': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
          'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        