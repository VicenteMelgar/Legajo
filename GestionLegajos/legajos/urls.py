from django.urls import path
from .import views 
from .views import VinculoCrearView, EstudiosCrearView, MovimientosCrearView, CompensacionesCrearView, TiempoCrearView, PensionistaCrearView

app_name='legajos'

urlpatterns = [
  path('', views.datospersonales_lista, name='datos_personales'),
  path('empleado_crear/', views.empleado_crear, name='empleado_crear'),
  path('info_general/<int:empleado_id>', views.info_general, name='info_general'),
  path('info_general/<int:empleado_id>/vinculo_crear/', VinculoCrearView.as_view(), name='vinculo_crear'),
  path('vinculo/editar/<int:vinculo_id>/', views.vinculo_editar, name='vinculo_editar'),
  path('estudios/crear/<int:empleado_id>/', EstudiosCrearView.as_view(), name='estudios_crear'),
  path('estudios/editar/<int:estudio_id>/', views.estudios_editar, name='estudios_editar'),
  path('movimientos/crear/<int:empleado_id>/', MovimientosCrearView.as_view(), name='movimientos_crear'),
  path('movimientos/editar/<int:movimiento_id>/', views.movimientos_editar, name='movimientos_editar'),
  path('compensaciones/crear/<int:empleado_id>/', CompensacionesCrearView.as_view(), name='compensaciones_crear'),
  path('compensaciones/editar/<int:compensaciones_id>/', views.compensaciones_editar, name='compensaciones_editar'),
  path('tiempo/crear/<int:empleado_id>/', TiempoCrearView.as_view(), name='tiempo_crear'),
  path('tiempo/editar/<int:tiempo_id>/', views.tiempo_editar, name='tiempo_editar'),
  path('pensionista/crear/<int:empleado_id>/', PensionistaCrearView.as_view(), name='pensionista_crear'),
  path('pensionista/editar/<int:pensionista_id>/', views.pensionista_editar, name='pensionista_editar'),
  path('documentos/', views.documentos, name='documentos'),
  path('dashboard/', views.dashboard, name='dashboard'),
]

