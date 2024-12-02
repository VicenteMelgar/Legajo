from django.contrib import admin
from django.utils.html import format_html
from django.contrib.admin import AdminSite
from .models import (
    DatosPersonales,
    ServiciosPrestados,
    Programa,
    AusenciasMeritosDemeritos,
    BonificacionPersonal,
    TiempodeServicios,
    PensionistaSobreviviente,
    EstudiosRealizados,
)

admin.site.site_header = "Gestión de Legajos"
admin.site.site_title = "Panel de Administración"
admin.site.index_title = "Bienvenido al Sistema de Administración"

@admin.register(DatosPersonales)
class DatosPersonalesAdmin(admin.ModelAdmin):
    list_display = ('apellido_paterno', 'apellido_materno', 'nombres', 'dni', 'carnet_extranjeria', 'email')
    search_fields = ('apellido_paterno', 'apellido_materno', 'nombres', 'dni')

@admin.register(ServiciosPrestados)
class ServiciosPrestadosAdmin(admin.ModelAdmin):
    list_display = ('resolucion', 'tipo', 'asunto', 'fecha', 'ver_pdf')
    list_filter = ('empleado', 'fecha')
    search_fields = ('resolucion', 'empleado__nombres', 'empleado__apellido_paterno', 'empleado__apellido_materno', 'empleado__dni')
    filter_horizontal = ('empleado',)
    
@admin.register(PensionistaSobreviviente)
class PensionistaSobrevivienteAdmin(admin.ModelAdmin):
    list_display = ('resolucion', 'fecha', 'ver_pdf')
    list_filter = ('empleado',) 
    search_fields = ('resolucion', 'empleado__nombres', 'empleado__apellido_paterno', 'empleado__apellido_materno', 'empleado__dni')
    