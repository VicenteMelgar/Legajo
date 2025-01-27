from django.contrib import admin
from .models import (
    DatosPersonales,
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
    
@admin.register(DatosPersonales)
class DatosPersonalesAdmin(admin.ModelAdmin):
    list_display = ('apellido_paterno', 'apellido_materno', 'nombres', 'dni', 'carnet_extranjeria', 'email')
    search_fields = ('apellido_paterno', 'apellido_materno', 'nombres', 'dni')

@admin.register(InfoPersonal)
class InfoPersonalAdmin(admin.ModelAdmin):
    list_display = ('tipo_documento', 'ver_pdf', 'fecha_carga')
    list_filter = ('empleado', 'tipo_documento')
    search_fields = ('tipo_documento', 'empleado__nombres', 'empleado__apellido_paterno', 'empleado__apellido_materno', 'empleado__dni')
    
@admin.register(Seleccion)
class SeleccionAdmin(admin.ModelAdmin):
    list_display = ('tipo_documento', 'descripcion', 'ver_pdf', 'fecha_carga')
    list_filter = ('empleado', 'tipo_documento')
    search_fields = ('tipo_documento', 'empleado__nombres', 'empleado__apellido_paterno', 'empleado__apellido_materno', 'empleado__dni')
    filter_horizontal = ('empleado',)
    
@admin.register(Vinculo)
class VinculoAdmin(admin.ModelAdmin):
    list_display = ('documento', 'numero', 'tipo', 'asunto', 'fecha_vigencia', 'ver_pdf')
    list_filter = ('empleado', 'tipo')
    search_fields = ('documento', 'empleado__nombres', 'empleado__apellido_paterno', 'empleado__apellido_materno', 'empleado__dni')
    filter_horizontal = ('empleado',)

@admin.register(Induccion)
class InduccionAdmin(admin.ModelAdmin):
    list_display = ('tipo_documento', 'ver_pdf', 'fecha_carga')
    list_filter = ('empleado', 'tipo_documento')
    search_fields = ('tipo_documento', 'empleado__nombres', 'empleado__apellido_paterno', 'empleado__apellido_materno', 'empleado__dni')
    
@admin.register(EstudiosRealizados)
class EstudiosRealizadosAdmin(admin.ModelAdmin):
    list_display = ('grado_instruccion', 'especialidad', 'inicio', 'fin', 'ver_pdf')
    list_filter = ('empleado',) 
    search_fields = ('grado_instruccion',)
       
@admin.register(Movimientos)
class MovimientosAdmin(admin.ModelAdmin):
    list_display = ('resolucion', 'motivo', 'asunto', 'desde', 'hasta', 'ver_pdf')
    list_filter = ('empleado',)
    search_fields = ('resolucion',)
    
@admin.register(Compensaciones)
class CompensacionesAdmin(admin.ModelAdmin):
    list_display = ('resolucion', 'fecha', 'motivo', 'porcentaje', 'anios', 'meses', 'dias', 'ver_pdf')
    list_filter = ('empleado',)
    search_fields = ('resolucion',)
