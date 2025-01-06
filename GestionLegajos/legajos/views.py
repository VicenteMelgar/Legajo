from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from datetime import date
from django.db.models import Q
from django.views.generic.edit import CreateView
from .models import DatosPersonales, Seleccion, Vinculo, Induccion, Movimientos, Compensaciones, TiempodeServicios, PensionistaSobreviviente, EstudiosRealizados, InfoPersonal
from .forms import DatosPersonalesForm, VinculoForm, EstudiosRealizadosForm, MovimientosForm, CompensacionesForm, TiempodeServiciosForm, PensionistaSobrevivienteForm

def datospersonales_lista(request):
  query = request.GET.get('searchorders', '')  # Obtén el texto ingresado en el buscador
  filters = Q(apellido_paterno__icontains=query) | Q(apellido_materno__icontains=query) | Q(nombres__icontains=query)

  empleados_cas = DatosPersonales.objects.filter(filters, modalidad='CAS')
  empleados_nombrados = DatosPersonales.objects.filter(filters, modalidad='Nombrado')
  empleados_cesantes = DatosPersonales.objects.filter(filters, modalidad='Cesante')
  todos_empleados = DatosPersonales.objects.filter(filters)

  # Preparar contexto
  context = {
    'empleados_cas': empleados_cas,
    'empleados_nombrados': empleados_nombrados,
    'empleados_cesantes': empleados_cesantes,
    'todos_empleados': todos_empleados,
    'query': query  # Para mantener el texto en el campo de búsqueda
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
  
def info_general(request, empleado_id):
    empleado = get_object_or_404(DatosPersonales, id=empleado_id)
    informacion_personal = InfoPersonal.objects.filter(empleado=empleado)
    selecciones = Seleccion.objects.filter(empleado=empleado)
    vinculos = Vinculo.objects.filter(empleado=empleado)
    inducciones = Induccion.objects.filter(empleado=empleado)
    movimientos = Movimientos.objects.filter(empleado=empleado)
    compensaciones = Compensaciones.objects.filter(empleado=empleado)
    tiempos_servicio = TiempodeServicios.objects.filter(empleado=empleado)
    pensionistas = PensionistaSobreviviente.objects.filter(empleado=empleado)
    estudios = EstudiosRealizados.objects.filter(empleado=empleado)
    
    context = {
        'empleado': empleado,
        'informacion_personal':informacion_personal,
        'selecciones': selecciones,
        'vinculos': vinculos,
        'inducciones': inducciones,
        'movimientos': movimientos,
        'compensaciones': compensaciones,
        'tiempos_servicio': tiempos_servicio,
        'pensionistas': pensionistas,
        'estudios': estudios,
    }
    return render(request, 'info_general.html', context)

class VinculoCrearView(CreateView):
    model = Vinculo
    form_class = VinculoForm
    template_name = 'vinculo_crear.html'

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
        return reverse('legajos:info_general', kwargs={'empleado_id': empleado_id})
    
    def form_valid(self, form):
        # Guarda el formulario
        self.object = form.save()

        # Maneja la acción según el botón presionado
        action = self.request.POST.get('action')
        if action == 'save_and_add_more':
            # Redirige a la misma página para seguir agregando
            empleado_id = self.kwargs.get('empleado_id')
            return redirect('legajos:vinculo_crear', empleado_id=empleado_id)
        elif action == 'save_and_exit':
            # Redirige a info_personal
            return super().form_valid(form)

        return super().form_valid(form)

def vinculo_editar(request, vinculo_id, empleado_id=None):
    vinculo = get_object_or_404(Vinculo, id=vinculo_id)

    if not empleado_id:
        empleado = vinculo.empleado.first()
        empleado_id = empleado.id if empleado else None

    if request.method == 'POST':
        form = VinculoForm(request.POST, request.FILES, instance=vinculo)
        if form.is_valid():
            vinculo = form.save(commit=False)
            vinculo.save()
            form.save_m2m()
            return redirect('legajos:info_general', empleado_id=empleado_id)
    else:
        form = VinculoForm(instance=vinculo)
        # Corrección: Asignar el objeto date directamente
        if vinculo.fecha:
            form.fields['fecha'].initial = vinculo.fecha
        if vinculo.fecha_vigencia:
            form.fields['fecha_vigencia'].initial = vinculo.fecha_vigencia

    context = {
        'form': form,
        'vinculo': vinculo,
        'empleado_preseleccionado': empleado_id,
    }
    return render(request, 'vinculo_edit.html', context)

# Agregar Estudios Realizados
class EstudiosCrearView(CreateView):
  model = EstudiosRealizados
  form_class = EstudiosRealizadosForm
  template_name = 'estudios_crear.html'

  def get_initial(self):
      # Preseleccionar el empleado con el id proporcionado en la URL
      empleado_id = self.kwargs.get('empleado_id')
      initial = super().get_initial()
      if empleado_id:
          initial['empleado'] = empleado_id
      return initial

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      empleado_id = self.kwargs.get('empleado_id')
      if empleado_id:
          context['empleado_preseleccionado'] = DatosPersonales.objects.get(id=empleado_id)
      return context

  def get_success_url(self):
      # Redirigir a la página de detalles del empleado luego de guardar
      empleado_id = self.kwargs.get('empleado_id')
      return reverse('legajos:info_personal', kwargs={'empleado_id': empleado_id})

  def form_valid(self, form):
      # Asociar el estudio al empleado automáticamente
      empleado_id = self.kwargs.get('empleado_id')
      if empleado_id:
          form.instance.empleado = DatosPersonales.objects.get(id=empleado_id)

      # Manejo de la acción del botón
      action = self.request.POST.get('action')
      self.object = form.save()
      if action == 'save_and_add_more':
          return redirect('legajos:estudios_crear', empleado_id=empleado_id)
      elif action == 'save_and_exit':
          return super().form_valid(form)

      return super().form_valid(form)
    
# Editar Estudios Realizados
def estudios_editar(request, estudio_id, empleado_id=None):
    estudio = get_object_or_404(EstudiosRealizados, id=estudio_id)

    # Obtener el empleado relacionado, si no está en la URL
    if not empleado_id:
        empleado = estudio.empleado
        empleado_id = empleado.id if empleado else None

    if request.method == 'POST':
        form = EstudiosRealizadosForm(request.POST, request.FILES, instance=estudio)
        if form.is_valid():
            estudio = form.save(commit=False)
            estudio.save()
            return redirect('legajos:info_personal', empleado_id=empleado_id)
    else:
        form = EstudiosRealizadosForm(instance=estudio)
        # Configurar inicialización de fechas si es necesario (opcional)
        if estudio.inicio:
            form.fields['inicio'].initial = estudio.inicio
        if estudio.fin:
            form.fields['fin'].initial = estudio.fin
        if estudio.fecha_expedicion:
            form.fields['fecha_expedicion'].initial = estudio.fecha_expedicion

    context = {
        'form': form,
        'estudio': estudio,
        'empleado_preseleccionado': empleado_id,
    }
    return render(request, 'estudios_edit.html', context)

#Agregar Ausencias, Méritos y Demeritos 
class MovimientosCrearView(CreateView):
    model = Movimientos
    form_class = MovimientosForm
    template_name = 'movimientos_crear.html'

    def get_initial(self):
        # Preseleccionar el empleado con el ID proporcionado en la URL
        empleado_id = self.kwargs.get('empleado_id')
        initial = super().get_initial()
        if empleado_id:
            initial['empleado'] = empleado_id
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        empleado_id = self.kwargs.get('empleado_id')
        if empleado_id:
            context['empleado_preseleccionado'] = DatosPersonales.objects.get(id=empleado_id)
        return context

    def get_success_url(self):
        # Redirigir a la página de detalles del empleado luego de guardar
        empleado_id = self.kwargs.get('empleado_id')
        return reverse('legajos:info_general', kwargs={'empleado_id': empleado_id})

    def form_valid(self, form):
        # Asociar la ausencia al empleado automáticamente
        empleado_id = self.kwargs.get('empleado_id')
        if empleado_id:
            form.instance.empleado = DatosPersonales.objects.get(id=empleado_id)

        # Manejo de la acción del botón
        action = self.request.POST.get('action')
        self.object = form.save()
        if action == 'save_and_add_more':
            return redirect('legajos:movimientos_crear', empleado_id=empleado_id)
        elif action == 'save_and_exit':
            return super().form_valid(form)

        return super().form_valid(form)

#Editar Ausencias, Méritos y Demeritos 
def movimientos_editar(request, movimiento_id, empleado_id=None):
    movimiento = get_object_or_404(Movimientos, id=movimiento_id)

    # Obtener el empleado relacionado, si no está en la URL
    if not empleado_id:
        empleado = movimiento.empleado
        empleado_id = empleado.id if empleado else None

    if request.method == 'POST':
        form = MovimientosForm(request.POST, request.FILES, instance=movimiento)
        if form.is_valid():
            ausencia = form.save(commit=False)
            ausencia.save()
            return redirect('legajos:info_general', empleado_id=empleado_id)
    else:
        form = MovimientosForm(instance=movimiento)
        # Configurar inicialización de fechas si es necesario
        if movimiento.desde:
            form.fields['desde'].initial = movimiento.desde
        if ausencia.hasta:
            form.fields['hasta'].initial = movimiento.hasta

    context = {
        'form': form,
        'movimiento': movimiento,
        'empleado_preseleccionado': empleado_id,
    }
    return render(request, 'movimientos_edit.html', context)

# Agregar Bonificación Personal
class CompensacionesCrearView(CreateView):
    model = Compensaciones
    form_class = CompensacionesForm
    template_name = 'compensaciones_crear.html'

    def get_initial(self):
        # Preseleccionar el empleado con el ID proporcionado en la URL
        empleado_id = self.kwargs.get('empleado_id')
        initial = super().get_initial()
        if empleado_id:
            initial['empleado'] = empleado_id
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        empleado_id = self.kwargs.get('empleado_id')
        if empleado_id:
            context['empleado_preseleccionado'] = DatosPersonales.objects.get(id=empleado_id)
        return context

    def get_success_url(self):
        # Redirigir a la página de detalles del empleado luego de guardar
        empleado_id = self.kwargs.get('empleado_id')
        return reverse('legajos:info_general', kwargs={'empleado_id': empleado_id})

    def form_valid(self, form):
        # Asociar la bonificación al empleado automáticamente
        empleado_id = self.kwargs.get('empleado_id')
        if empleado_id:
            form.instance.empleado = DatosPersonales.objects.get(id=empleado_id)

        # Manejo de la acción del botón
        action = self.request.POST.get('action')
        self.object = form.save()
        if action == 'save_and_add_more':
            return redirect('legajos:compensaciones_crear', empleado_id=empleado_id)
        elif action == 'save_and_exit':
            return super().form_valid(form)

        return super().form_valid(form)

#Editar Bonificación Personal
def compensaciones_editar(request, compensaciones_id, empleado_id=None):
    compensaciones = get_object_or_404(Compensaciones, id=compensaciones_id)

    # Obtener el empleado relacionado, si no está en la URL
    if not empleado_id:
        empleado = compensaciones.empleado
        empleado_id = empleado.id if empleado else None

    if request.method == 'POST':
        form = CompensacionesForm(request.POST, request.FILES, instance=compensaciones)
        if form.is_valid():
            compensaciones = form.save(commit=False)
            compensaciones.save()
            return redirect('legajos:info_general', empleado_id=empleado_id)
    else:
        form = CompensacionesForm(instance=compensaciones)
        # Configurar inicialización de datos si es necesario
        if compensaciones.fecha:
            form.fields['fecha'].initial = compensaciones.fecha

    context = {
        'form': form,
        'compensaciones': compensaciones,
        'empleado_preseleccionado': empleado_id,
    }
    return render(request, 'compensaciones_edit.html', context)

# Agregar Tiempo de Servicios
class TiempoCrearView(CreateView):
    model = TiempodeServicios
    form_class = TiempodeServiciosForm
    template_name = 'tiempo_crear.html'

    def get_initial(self):
        # Preseleccionar el empleado con el ID proporcionado en la URL
        empleado_id = self.kwargs.get('empleado_id')
        initial = super().get_initial()
        if empleado_id:
            initial['empleado'] = empleado_id
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        empleado_id = self.kwargs.get('empleado_id')
        if empleado_id:
            context['empleado_preseleccionado'] = DatosPersonales.objects.get(id=empleado_id)
        return context

    def get_success_url(self):
        # Redirigir a la página de detalles del empleado luego de guardar
        empleado_id = self.kwargs.get('empleado_id')
        return reverse('legajos:info_personal', kwargs={'empleado_id': empleado_id})

    def form_valid(self, form):
        # Asociar el tiempo de servicio al empleado automáticamente
        empleado_id = self.kwargs.get('empleado_id')
        if empleado_id:
            form.instance.empleado = DatosPersonales.objects.get(id=empleado_id)

        # Manejo de la acción del botón
        action = self.request.POST.get('action')
        self.object = form.save()
        if action == 'save_and_add_more':
            return redirect('legajos:tiempo_crear', empleado_id=empleado_id)
        elif action == 'save_and_exit':
            return super().form_valid(form)

        return super().form_valid(form)

#Editar Tiempo de Servicios
def tiempo_editar(request, tiempo_id, empleado_id=None):
    tiempo = get_object_or_404(TiempodeServicios, id=tiempo_id)

    # Obtener el empleado relacionado, si no está en la URL
    if not empleado_id:
        empleado = tiempo.empleado
        empleado_id = empleado.id if empleado else None

    if request.method == 'POST':
        form = TiempodeServiciosForm(request.POST, request.FILES, instance=tiempo)
        if form.is_valid():
            tiempo = form.save(commit=False)
            tiempo.save()
            return redirect('legajos:info_personal', empleado_id=empleado_id)
    else:
        form = TiempodeServiciosForm(instance=tiempo)
        # Configurar inicialización de fechas si es necesario
        if tiempo.desde:
            form.fields['desde'].initial = tiempo.desde
        if tiempo.hasta:
            form.fields['hasta'].initial = tiempo.hasta

    context = {
        'form': form,
        'tiempo': tiempo,
        'empleado_preseleccionado': empleado_id,
    }
    return render(request, 'tiempo_edit.html', context)
  
  #Agregar Pensionista
class PensionistaCrearView(CreateView):
  model = PensionistaSobreviviente
  form_class = PensionistaSobrevivienteForm
  template_name = 'pensionista_crear.html'

  def get_initial(self):
      # Preseleccionar el empleado con el ID proporcionado en la URL
      empleado_id = self.kwargs.get('empleado_id')
      initial = super().get_initial()
      if empleado_id:
          initial['empleado'] = empleado_id
      return initial

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      empleado_id = self.kwargs.get('empleado_id')
      if empleado_id:
          context['empleado_preseleccionado'] = DatosPersonales.objects.get(id=empleado_id)
      return context

  def get_success_url(self):
      # Redirigir a la página de detalles del empleado luego de guardar
      empleado_id = self.kwargs.get('empleado_id')
      return reverse('legajos:info_personal', kwargs={'empleado_id': empleado_id})

  def form_valid(self, form):
      # Asociar el pensionista al empleado automáticamente
      empleado_id = self.kwargs.get('empleado_id')
      if empleado_id:
          form.instance.empleado = DatosPersonales.objects.get(id=empleado_id)

      # Manejo de la acción del botón
      action = self.request.POST.get('action')
      self.object = form.save()
      if action == 'save_and_add_more':
          return redirect('legajos:pensionista_crear', empleado_id=empleado_id)
      elif action == 'save_and_exit':
          return super().form_valid(form)

      return super().form_valid(form)

#Editar Pensionista
def pensionista_editar(request, pensionista_id, empleado_id=None):
    pensionista = get_object_or_404(PensionistaSobreviviente, id=pensionista_id)

    # Obtener el empleado relacionado, si no está en la URL
    if not empleado_id:
        empleado = pensionista.empleado
        empleado_id = empleado.id if empleado else None

    if request.method == 'POST':
        form = PensionistaSobrevivienteForm(request.POST, request.FILES, instance=pensionista)
        if form.is_valid():
            pensionista = form.save(commit=False)
            pensionista.save()
            return redirect('legajos:info_personal', empleado_id=empleado_id)
    else:
        form = PensionistaSobrevivienteForm(instance=pensionista)

    context = {
        'form': form,
        'pensionista': pensionista,
        'empleado_preseleccionado': empleado_id,
    }
    return render(request, 'pensionista_edit.html', context)

def documentos(request):
    return render(request, 'documentos.html')

def dashboard(request):
    return render(request, 'dashboard.html')