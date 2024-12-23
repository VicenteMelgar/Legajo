from django.urls import path
from .import views
from .views import ServicioCrearView

app_name='legajos'

urlpatterns = [
  path('', views.datospersonales_lista, name='datos_personales'),
  path('empleado_crear/', views.empleado_crear, name='empleado_crear'),
  path('info_personal/<int:empleado_id>', views.info_personal, name='info_personal'),
  path('info_personal/<int:empleado_id>/servicio_crear/', ServicioCrearView.as_view(), name='servicio_crear'),
  path('servicios/editar/<int:servicio_id>/', views.servicio_editar, name='servicio_editar'),
]