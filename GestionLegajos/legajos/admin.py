from django.contrib import admin
from .models import (
    Empleado,
    Resolucion,
    OficinaHistorial,
    CondicionHistorial,
    GrupoHistorial,
    CargoHistorial,
    NivelHistorial,
    PlazaHistorial,
    Legajo,
    InfoPersonal,
    Seleccion,
    Vinculo,
    Induccion,
    Movimientos,
    Compensaciones,
    EstudiosRealizados,
    Prueba,
    Habilitacion,
    Serum,
    Curso,
    Experiencia,
    Retencion,
    Evaluacion,
    Reconocimiento,
    Laboral,
    Seguridad,
    Desvinculacion,
    Otro,
)

admin.site.site_header = "DASHBOARD LEGAJO"
admin.site.site_title = "Panel de Administración"
admin.site.index_title = "Bienvenido al Sistema de Administración"
 
@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('apellido_paterno', 'apellido_materno', 'nombres', 'numero_documento', 'email')
    search_fields = ('apellido_paterno', 'apellido_materno', 'nombres', 'numero_documento')

@admin.register(Resolucion)
class ResolucionAdmin(admin.ModelAdmin):
    list_display = ('documento', 'numero', 'tipo', 'fecha')
    search_fields = ('documento', 'numero', 'tipo', 'fecha')

@admin.register(OficinaHistorial)
class OficinaHistorialAdmin(admin.ModelAdmin):
    list_display = ('empleado_numero_documento', 'empleado_apellido_paterno', 'empleado_apellido_materno', 'empleado_nombres', 'denominacion', 'fecha_inicio', 'fecha_fin')
    search_fields = ('denominacion',)
    
    def empleado_numero_documento(self, obj):
        return obj.empleado.numero_documento
    empleado_numero_documento.short_description = 'DNI'
    
    def empleado_apellido_paterno(self, obj):
        return obj.empleado.apellido_paterno
    empleado_apellido_paterno.short_description = 'Apellido Paterno'

    def empleado_apellido_materno(self, obj):
        return obj.empleado.apellido_materno
    empleado_apellido_materno.short_description = 'Apellido Materno'

    def empleado_nombres(self, obj):
        return obj.empleado.nombres
    empleado_nombres.short_description = 'Nombres'

@admin.register(CondicionHistorial)
class CondicionHistorialAdmin(admin.ModelAdmin):
    list_display = ('empleado_numero_documento', 'empleado_apellido_paterno', 'empleado_apellido_materno', 'empleado_nombres', 'denominacion', 'fecha_inicio', 'fecha_fin')
    search_fields = ('denominacion',)
    
    def empleado_numero_documento(self, obj):
        return obj.empleado.numero_documento
    empleado_numero_documento.short_description = 'DNI'
    
    def empleado_apellido_paterno(self, obj):
        return obj.empleado.apellido_paterno
    empleado_apellido_paterno.short_description = 'Apellido Paterno'

    def empleado_apellido_materno(self, obj):
        return obj.empleado.apellido_materno
    empleado_apellido_materno.short_description = 'Apellido Materno'

    def empleado_nombres(self, obj):
        return obj.empleado.nombres
    empleado_nombres.short_description = 'Nombres'

@admin.register(GrupoHistorial)
class GrupoHistorialAdmin(admin.ModelAdmin):
    list_display = ('empleado_numero_documento', 'empleado_apellido_paterno', 'empleado_apellido_materno', 'empleado_nombres', 'denominacion', 'fecha_inicio', 'fecha_fin')
    search_fields = ('denominacion',)
    
    def empleado_numero_documento(self, obj):
        return obj.empleado.numero_documento
    empleado_numero_documento.short_description = 'DNI'
    
    def empleado_apellido_paterno(self, obj):
        return obj.empleado.apellido_paterno
    empleado_apellido_paterno.short_description = 'Apellido Paterno'

    def empleado_apellido_materno(self, obj):
        return obj.empleado.apellido_materno
    empleado_apellido_materno.short_description = 'Apellido Materno'

    def empleado_nombres(self, obj):
        return obj.empleado.nombres
    empleado_nombres.short_description = 'Nombres'
    
@admin.register(CargoHistorial)
class CargoHistorialAdmin(admin.ModelAdmin):
    list_display = ('empleado_numero_documento', 'empleado_apellido_paterno', 'empleado_apellido_materno', 'empleado_nombres', 'denominacion', 'fecha_inicio', 'fecha_fin')
    search_fields = ('denominacion',)
    
    def empleado_numero_documento(self, obj):
        return obj.empleado.numero_documento
    empleado_numero_documento.short_description = 'DNI'
    
    def empleado_apellido_paterno(self, obj):
        return obj.empleado.apellido_paterno
    empleado_apellido_paterno.short_description = 'Apellido Paterno'

    def empleado_apellido_materno(self, obj):
        return obj.empleado.apellido_materno
    empleado_apellido_materno.short_description = 'Apellido Materno'

    def empleado_nombres(self, obj):
        return obj.empleado.nombres
    empleado_nombres.short_description = 'Nombres'
    
@admin.register(NivelHistorial)
class NivelHistorialAdmin(admin.ModelAdmin):
    list_display = ('empleado_numero_documento', 'empleado_apellido_paterno', 'empleado_apellido_materno', 'empleado_nombres', 'denominacion', 'fecha_inicio', 'fecha_fin')
    search_fields = ('denominacion',)
    
    def empleado_numero_documento(self, obj):
        return obj.empleado.numero_documento
    empleado_numero_documento.short_description = 'DNI'
    
    def empleado_apellido_paterno(self, obj):
        return obj.empleado.apellido_paterno
    empleado_apellido_paterno.short_description = 'Apellido Paterno'

    def empleado_apellido_materno(self, obj):
        return obj.empleado.apellido_materno
    empleado_apellido_materno.short_description = 'Apellido Materno'

    def empleado_nombres(self, obj):
        return obj.empleado.nombres
    empleado_nombres.short_description = 'Nombres'

@admin.register(PlazaHistorial)
class PlazaHistorialAdmin(admin.ModelAdmin):
    list_display = ('empleado_numero_documento', 'empleado_apellido_paterno', 'empleado_apellido_materno', 'empleado_nombres', 'denominacion', 'fecha_inicio', 'fecha_fin')
    search_fields = ('denominacion',)
    
    def empleado_numero_documento(self, obj):
        return obj.empleado.numero_documento
    empleado_numero_documento.short_description = 'DNI'
    
    def empleado_apellido_paterno(self, obj):
        return obj.empleado.apellido_paterno
    empleado_apellido_paterno.short_description = 'Apellido Paterno'

    def empleado_apellido_materno(self, obj):
        return obj.empleado.apellido_materno
    empleado_apellido_materno.short_description = 'Apellido Materno'

    def empleado_nombres(self, obj):
        return obj.empleado.nombres
    empleado_nombres.short_description = 'Nombres'
    
@admin.register(Legajo)
class LegajoAdmin(admin.ModelAdmin):
    list_display = ('empleado_apellido_paterno', 'empleado_apellido_materno', 'empleado_nombres', 'empleado_numero_documento', 'regimen_laboral', 'activo')
    search_fields = ('empleado__apellido_paterno', 'empleado__apellido_materno', 'empleado__nombres', 'empleado__numero_documento', 'regimen_laboral')

    def empleado_apellido_paterno(self, obj):
        return obj.empleado.apellido_paterno
    empleado_apellido_paterno.short_description = 'Apellido Paterno'

    def empleado_apellido_materno(self, obj):
        return obj.empleado.apellido_materno
    empleado_apellido_materno.short_description = 'Apellido Materno'

    def empleado_nombres(self, obj):
        return obj.empleado.nombres
    empleado_nombres.short_description = 'Nombres'

    def empleado_numero_documento(self, obj):
        return obj.empleado.numero_documento
    empleado_numero_documento.short_description = 'DNI'
    
@admin.register(InfoPersonal)
class InfoPersonalAdmin(admin.ModelAdmin):
    list_display = ('documento', 'documento_otro', 'fecha', 'ver_pdf')
    list_filter = ('documento',)
    search_fields = ('documento',)
    
@admin.register(Seleccion)
class SeleccionAdmin(admin.ModelAdmin):
    list_display = ('documento', 'descripcion', 'ver_pdf', 'fecha')
    list_filter = ('documento', )
    search_fields = ('documento',)
    filter_horizontal = ('legajo',)
    
@admin.register(Vinculo)
class VinculoAdmin(admin.ModelAdmin):
    list_display = ('legajo', 'tipo', 'resolucion', 'descripcion',)
    search_fields = ('descripcion',)

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
    
@admin.register(Habilitacion)
class HabilitacionAdmin(admin.ModelAdmin):
    list_display = ('registro', 'fecha_emision', 'fecha_vigencia', 'ver_pdf')
    list_filter = ('registro',)
    search_fields = ('registro',)
    
@admin.register(Serum)
class SerumAdmin(admin.ModelAdmin):
    list_display = ('registro', 'fecha_emision', 'ver_pdf')
    list_filter = ('registro',)
    search_fields = ('registro',)

@admin.register(EstudiosRealizados)
class EstudiosRealizadosAdmin(admin.ModelAdmin):
    list_display = ('grado_instruccion', 'especialidad', 'inicio', 'fin', 'ver_pdf')
    search_fields = ('grado_instruccion',)
       
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('documento', 'descripcion', 'inicio', 'fin', 'horas', 'creditos', 'fecha_expedicion', 'ver_pdf')
    list_filter = ('documento',)
    search_fields = ('documento',)

@admin.register(Experiencia)
class ExperienciaAdmin(admin.ModelAdmin):
    list_display = ('documento', 'numero', 'cargo', 'fecha_inicio', 'fecha_fin', 'fecha_expedicion', 'ver_pdf')
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
    list_display = ('periodo', 'anio', 'puntaje', 'ver_pdf')
    list_filter = ('anio',)
    search_fields = ('anio',)
    
@admin.register(Reconocimiento)
class ReconocimientoAdmin(admin.ModelAdmin):
    list_display = ('documento_reconocimiento', 'documento', 'descripcion', 'fecha', 'ver_pdf')
    list_filter = ('documento_reconocimiento', 'documento')
    search_fields = ('documento',)
    
@admin.register(Laboral)
class LaboralAdmin(admin.ModelAdmin):
    list_display = ('documento', 'documento', 'descripcion', 'fecha', 'ver_pdf', 'fecha_carga')
    list_filter = ('documento',)
    search_fields = ('documento',)
    
@admin.register(Seguridad)
class SeguridadAdmin(admin.ModelAdmin):
    list_display = ('documento', 'descripcion', 'fecha', 'ver_pdf')
    list_filter = ('documento',)
    search_fields = ('documento',)
    
@admin.register(Compensaciones)
class CompensacionesAdmin(admin.ModelAdmin):
    list_display = ('documento', 'numero', 'motivo', 'descripcion', 'fecha', 'ver_pdf')
    list_filter = ('documento',)
    search_fields = ('documento',)
    
@admin.register(Desvinculacion)
class DesviculacionAdmin(admin.ModelAdmin):
    list_display = ('documento', 'descripcion', 'fecha', 'ver_pdf')
    list_filter = ('documento',)
    search_fields = ('documento',)
    
@admin.register(Otro)
class OtroAdmin(admin.ModelAdmin):
    list_display = ('documento', 'descripcion', 'fecha', 'ver_pdf')
    list_filter = ('documento',)
    search_fields = ('documento',)