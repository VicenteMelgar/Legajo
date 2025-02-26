from django.contrib import admin
from .models import (
    Empleado,
    Legajo,
    InfoPersonal,
    Seleccion,
    Vinculo,
    Induccion,
    Movimientos,
    Compensaciones,
    EstudiosRealizados,
    Nivel,
    Cargo,
    Plaza,
    Prueba,
    Colegiatura,
    Curso,
    Experiencia,
    Retencion,
    Evaluacion,
    Progresion,
    Desplazamiento,
    Reconocimiento,
    Laboral,
    Seguridad,
    Desvinculacion,
)

admin.site.site_header = "DASHBOARD LEGAJO"
admin.site.site_title = "Panel de Administración"
admin.site.index_title = "Bienvenido al Sistema de Administración"

@admin.register(Nivel)
class NivelAdmin(admin.ModelAdmin):
    list_display = ('denominacion',)
    
@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('denominacion',)
    
@admin.register(Plaza)
class PlazaAdmin(admin.ModelAdmin):
    list_display = ('denominacion',)
    
@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('apellido_paterno', 'apellido_materno', 'nombres', 'dni', 'carnet_extranjeria', 'email')
    search_fields = ('apellido_paterno', 'apellido_materno', 'nombres', 'dni')

@admin.register(Legajo)
class LegajoAdmin(admin.ModelAdmin):
    list_display = ('empleado_apellido_paterno', 'empleado_apellido_materno', 'empleado_nombres', 'empleado_dni', 'regimen_laboral', 'activo')
    search_fields = ('empleado__apellido_paterno', 'empleado__apellido_materno', 'empleado__nombres', 'empleado__dni', 'regimen_laboral')

    def empleado_apellido_paterno(self, obj):
        return obj.empleado.apellido_paterno
    empleado_apellido_paterno.short_description = 'Apellido Paterno'

    def empleado_apellido_materno(self, obj):
        return obj.empleado.apellido_materno
    empleado_apellido_materno.short_description = 'Apellido Materno'

    def empleado_nombres(self, obj):
        return obj.empleado.nombres
    empleado_nombres.short_description = 'Nombres'

    def empleado_dni(self, obj):
        return obj.empleado.dni
    empleado_dni.short_description = 'DNI'
    
@admin.register(InfoPersonal)
class InfoPersonalAdmin(admin.ModelAdmin):
    list_display = ('documento', 'fecha', 'ver_pdf')
    list_filter = ('documento',)
    search_fields = ('documento',)
    
@admin.register(Seleccion)
class SeleccionAdmin(admin.ModelAdmin):
    list_display = ('documento', 'descripcion', 'ver_pdf', 'fecha')
    list_filter = ('legajo', 'documento')
    search_fields = ('documento',)
    filter_horizontal = ('legajo',)
    
@admin.register(Vinculo)
class VinculoAdmin(admin.ModelAdmin):
    list_display = ('documento', 'numero', 'tipo', 'descripcion', 'fecha_vigencia', 'ver_pdf')
    list_filter = ('tipo',)
    search_fields = ('documento',)
    filter_horizontal = ('legajo',)

@admin.register(Induccion)
class InduccionAdmin(admin.ModelAdmin):
    list_display = ('documento', 'ver_pdf', 'fecha')
    list_filter = ('documento',)
    search_fields = ('documento',)
    
@admin.register(Prueba)
class PruebaAdmin(admin.ModelAdmin):
    list_display = ('documento', 'ver_pdf', 'fecha')
    list_filter = ('documento',)
    search_fields = ('documento',)
    
@admin.register(Colegiatura)
class ColegiaturaAdmin(admin.ModelAdmin):
    list_display = ('documento', 'fecha_emision', 'fecha_vigencia', 'ver_pdf')
    list_filter = ('documento',)
    search_fields = ('documento',)

@admin.register(EstudiosRealizados)
class EstudiosRealizadosAdmin(admin.ModelAdmin):
    list_display = ('grado_instruccion', 'especialidad', 'inicio', 'fin', 'ver_pdf')
    search_fields = ('grado_instruccion',)
       
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('documento', 'descripcion', 'inicio', 'fin', 'duracion', 'fecha_expedicion', 'ver_pdf')
    list_filter = ('documento',)
    search_fields = ('documento',)

@admin.register(Experiencia)
class ExperienciaAdmin(admin.ModelAdmin):
    list_display = ('documento', 'descripcion', 'cargo', 'fecha_inicio', 'fecha_fin', 'fecha_expedicion', 'ver_pdf')
    list_filter = ('documento',)
    search_fields = ('documento',)

@admin.register(Movimientos)
class MovimientosAdmin(admin.ModelAdmin):
    list_display = ('documento', 'motivo', 'asunto', 'desde', 'hasta', 'total_dias', 'ver_pdf')
    list_filter = ('legajo',)
    search_fields = ('documento',)
    
@admin.register(Retencion)
class RetencionAdmin(admin.ModelAdmin):
    list_display = ('documento', 'fecha', 'ver_pdf')
    list_filter = ('documento',)
    search_fields = ('documento',)
    
@admin.register(Evaluacion)
class EvaluacionAdmin(admin.ModelAdmin):
    list_display = ('periodo', 'fecha', 'documento', 'puntaje', 'ver_pdf')
    list_filter = ('documento',)
    search_fields = ('documento',)
    
@admin.register(Progresion)
class ProgresionAdmin(admin.ModelAdmin):
    list_display = ('documento', 'numero', 'fecha', 'ver_pdf', 'fecha_carga')
    list_filter = ('documento',)
    search_fields = ('documento',)
    
@admin.register(Desplazamiento)
class DesplazamientoAdmin(admin.ModelAdmin):
    list_display = ('documento', 'tipo', 'asunto', 'ver_pdf')
    list_filter = ('documento',)
    search_fields = ('documento',)
    
@admin.register(Reconocimiento)
class ReconocimientoAdmin(admin.ModelAdmin):
    list_display = ('documento_reconocimiento', 'documento', 'descripcion', 'fecha', 'ver_pdf', 'fecha_carga')
    list_filter = ('documento_reconocimiento', 'documento')
    search_fields = ('documento',)
    
@admin.register(Laboral)
class LaboralAdmin(admin.ModelAdmin):
    list_display = ('documento', 'documento', 'descripcion', 'fecha', 'ver_pdf', 'fecha_carga')
    list_filter = ('documento',)
    search_fields = ('documento',)
    
@admin.register(Seguridad)
class SeguridadAdmin(admin.ModelAdmin):
    list_display = ('documento', 'descripcion', 'fecha', 'ver_pdf', 'fecha_carga')
    list_filter = ('documento',)
    search_fields = ('documento',)
    
@admin.register(Compensaciones)
class CompensacionesAdmin(admin.ModelAdmin):
    list_display = ('resolucion', 'fecha', 'motivo', 'porcentaje', 'anios', 'meses', 'dias', 'ver_pdf')
    list_filter = ('legajo',)
    search_fields = ('resolucion',)
    
@admin.register(Desvinculacion)
class DesviculacionAdmin(admin.ModelAdmin):
    list_display = ('documento', 'descripcion', 'fecha', 'ver_pdf', 'fecha_carga')
    list_filter = ('documento',)
    search_fields = ('documento',)
