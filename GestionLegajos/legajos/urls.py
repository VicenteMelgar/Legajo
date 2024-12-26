from django.urls import path
from .import views 
from .views import ServicioCrearView, EstudiosCrearView, AusenciasCrearView, BonificacionCrearView, TiempoCrearView, PensionistaCrearView

app_name='legajos'

urlpatterns = [
  path('', views.datospersonales_lista, name='datos_personales'),
  path('empleado_crear/', views.empleado_crear, name='empleado_crear'),
  path('info_personal/<int:empleado_id>', views.info_personal, name='info_personal'),
  path('info_personal/<int:empleado_id>/servicio_crear/', ServicioCrearView.as_view(), name='servicio_crear'),
  path('servicios/editar/<int:servicio_id>/', views.servicio_editar, name='servicio_editar'),
  path('estudios/crear/<int:empleado_id>/', EstudiosCrearView.as_view(), name='estudios_crear'),
  path('estudios/editar/<int:estudio_id>/', views.estudios_editar, name='estudios_editar'),
  path('ausencias/crear/<int:empleado_id>/', AusenciasCrearView.as_view(), name='ausencias_crear'),
  path('ausencias/editar/<int:ausencia_id>/', views.ausencias_editar, name='ausencias_editar'),
  path('bonificacion/crear/<int:empleado_id>/', BonificacionCrearView.as_view(), name='bonificacion_crear'),
  path('bonificacion/editar/<int:bonificacion_id>/', views.bonificacion_editar, name='bonificacion_editar'),
  path('tiempo/crear/<int:empleado_id>/', TiempoCrearView.as_view(), name='tiempo_crear'),
  path('tiempo/editar/<int:tiempo_id>/', views.tiempo_editar, name='tiempo_editar'),
  path('pensionista/crear/<int:empleado_id>/', PensionistaCrearView.as_view(), name='pensionista_crear'),
  path('pensionista/editar/<int:pensionista_id>/', views.pensionista_editar, name='pensionista_editar'),
  path('documentos/', views.documentos, name='documentos'),
  path('dashboard/', views.dashboard, name='dashboard'),
]

