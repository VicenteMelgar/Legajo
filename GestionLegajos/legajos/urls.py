from django.urls import path
from .import views

app_name='legajos'

urlpatterns = [
  path('', views.datospersonales_lista_creada, name='datos_personales')
]