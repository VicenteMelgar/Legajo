from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from datetime import date
from django.views.generic.edit import CreateView
from .models import DatosPersonales, ServiciosPrestados, AusenciasMeritosDemeritos, BonificacionPersonal, TiempodeServicios, PensionistaSobreviviente, EstudiosRealizados
from .forms import DatosPersonalesForm, ServiciosPrestadosForm

def datospersonales_lista(request):
  
  empleados_cas = DatosPersonales.objects.filter(modalidad='CAS')
  empleados_nombrados = DatosPersonales.objects.filter(modalidad='Nombrado')
  empleados_cesantes = DatosPersonales.objects.filter(modalidad='Cesante')
  todos_empleados = DatosPersonales.objects.all()
  
    # Preparar contexto
  context = {
      'empleados_cas': empleados_cas,
      'empleados_nombrados': empleados_nombrados,
      'empleados_cesantes': empleados_cesantes,
      'todos_empleados': todos_empleados,
    }
  
  return render(request, 'empleados.html', context)

def empleado_crear(request):
    if request.method == 'POST':
        form = DatosPersonalesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('legajos:datos_personales')  # Cambia por el nombre de tu vista de lista
    else:
        form = DatosPersonalesForm()
    return render(request, 'empleado_crear.html', {'form': form})
  
def info_personal(request, empleado_id):
    empleado = get_object_or_404(DatosPersonales, id=empleado_id)
    servicios = ServiciosPrestados.objects.filter(empleado=empleado)
    ausencias = AusenciasMeritosDemeritos.objects.filter(empleado=empleado)
    bonificaciones = BonificacionPersonal.objects.filter(empleado=empleado)
    tiempos_servicio = TiempodeServicios.objects.filter(empleado=empleado)
    pensionistas = PensionistaSobreviviente.objects.filter(empleado=empleado)
    estudios = EstudiosRealizados.objects.filter(empleado=empleado)
    
    context = {
        'empleado': empleado,
        'servicios': servicios,
        'ausencias': ausencias,
        'bonificaciones': bonificaciones,
        'tiempos_servicio': tiempos_servicio,
        'pensionistas': pensionistas,
        'estudios': estudios,
    }
    return render(request, 'info_personal.html', context)

class ServicioCrearView(CreateView):
    model = ServiciosPrestados
    form_class = ServiciosPrestadosForm
    template_name = 'servicio_crear.html'

    def get_initial(self):
        empleado_id = self.kwargs.get('empleado_id')
        initial = super().get_initial()
        if empleado_id:
            initial['empleado'] = [empleado_id]
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        empleado_id = self.kwargs.get('empleado_id')
        if empleado_id:
            context['empleado_preseleccionado'] = DatosPersonales.objects.get(id=empleado_id)
        return context

    def get_success_url(self):
        empleado_id = self.kwargs.get('empleado_id')
        return reverse('legajos:info_personal', kwargs={'empleado_id': empleado_id})

def servicio_editar(request, servicio_id, empleado_id=None):
    servicio = get_object_or_404(ServiciosPrestados, id=servicio_id)

    if not empleado_id:
        empleado = servicio.empleado.first()
        empleado_id = empleado.id if empleado else None

    if request.method == 'POST':
        form = ServiciosPrestadosForm(request.POST, request.FILES, instance=servicio)
        if form.is_valid():
            servicio = form.save(commit=False)
            servicio.save()
            form.save_m2m()
            return redirect('legajos:info_personal', empleado_id=empleado_id)
    else:
        form = ServiciosPrestadosForm(instance=servicio)
        # Corrección: Asignar el objeto date directamente
        if servicio.fecha:
            form.fields['fecha'].initial = servicio.fecha
        if servicio.fecha_vigencia:
            form.fields['fecha_vigencia'].initial = servicio.fecha_vigencia

    context = {
        'form': form,
        'servicio': servicio,
        'empleado_preseleccionado': empleado_id,
    }
    return render(request, 'servicio_edit.html', context)