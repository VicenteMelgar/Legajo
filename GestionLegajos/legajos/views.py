from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from datetime import date
from django.views.generic.edit import CreateView
from .models import DatosPersonales, ServiciosPrestados, AusenciasMeritosDemeritos, BonificacionPersonal, TiempodeServicios, PensionistaSobreviviente, EstudiosRealizados
from .forms import DatosPersonalesForm, ServiciosPrestadosForm, EstudiosRealizadosForm, AusenciasMeritosDemeritosForm, BonificacionPersonalForm, TiempodeServiciosForm, PensionistaSobrevivienteForm

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
    
    def form_valid(self, form):
        # Guarda el formulario
        self.object = form.save()

        # Maneja la acción según el botón presionado
        action = self.request.POST.get('action')
        if action == 'save_and_add_more':
            # Redirige a la misma página para seguir agregando
            empleado_id = self.kwargs.get('empleado_id')
            return redirect('legajos:servicio_crear', empleado_id=empleado_id)
        elif action == 'save_and_exit':
            # Redirige a info_personal
            return super().form_valid(form)

        return super().form_valid(form)

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
class AusenciasCrearView(CreateView):
    model = AusenciasMeritosDemeritos
    form_class = AusenciasMeritosDemeritosForm
    template_name = 'ausencias_crear.html'

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
        # Asociar la ausencia al empleado automáticamente
        empleado_id = self.kwargs.get('empleado_id')
        if empleado_id:
            form.instance.empleado = DatosPersonales.objects.get(id=empleado_id)

        # Manejo de la acción del botón
        action = self.request.POST.get('action')
        self.object = form.save()
        if action == 'save_and_add_more':
            return redirect('legajos:ausencias_crear', empleado_id=empleado_id)
        elif action == 'save_and_exit':
            return super().form_valid(form)

        return super().form_valid(form)

#Editar Ausencias, Méritos y Demeritos 
def ausencias_editar(request, ausencia_id, empleado_id=None):
    ausencia = get_object_or_404(AusenciasMeritosDemeritos, id=ausencia_id)

    # Obtener el empleado relacionado, si no está en la URL
    if not empleado_id:
        empleado = ausencia.empleado
        empleado_id = empleado.id if empleado else None

    if request.method == 'POST':
        form = AusenciasMeritosDemeritosForm(request.POST, request.FILES, instance=ausencia)
        if form.is_valid():
            ausencia = form.save(commit=False)
            ausencia.save()
            return redirect('legajos:info_personal', empleado_id=empleado_id)
    else:
        form = AusenciasMeritosDemeritosForm(instance=ausencia)
        # Configurar inicialización de fechas si es necesario
        if ausencia.desde:
            form.fields['desde'].initial = ausencia.desde
        if ausencia.hasta:
            form.fields['hasta'].initial = ausencia.hasta

    context = {
        'form': form,
        'ausencia': ausencia,
        'empleado_preseleccionado': empleado_id,
    }
    return render(request, 'ausencias_edit.html', context)

# Agregar Bonificación Personal
class BonificacionCrearView(CreateView):
    model = BonificacionPersonal
    form_class = BonificacionPersonalForm
    template_name = 'bonificacion_crear.html'

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
        # Asociar la bonificación al empleado automáticamente
        empleado_id = self.kwargs.get('empleado_id')
        if empleado_id:
            form.instance.empleado = DatosPersonales.objects.get(id=empleado_id)

        # Manejo de la acción del botón
        action = self.request.POST.get('action')
        self.object = form.save()
        if action == 'save_and_add_more':
            return redirect('legajos:bonificacion_crear', empleado_id=empleado_id)
        elif action == 'save_and_exit':
            return super().form_valid(form)

        return super().form_valid(form)

#Editar Bonificación Personal
def bonificacion_editar(request, bonificacion_id, empleado_id=None):
    bonificacion = get_object_or_404(BonificacionPersonal, id=bonificacion_id)

    # Obtener el empleado relacionado, si no está en la URL
    if not empleado_id:
        empleado = bonificacion.empleado
        empleado_id = empleado.id if empleado else None

    if request.method == 'POST':
        form = BonificacionPersonalForm(request.POST, request.FILES, instance=bonificacion)
        if form.is_valid():
            bonificacion = form.save(commit=False)
            bonificacion.save()
            return redirect('legajos:info_personal', empleado_id=empleado_id)
    else:
        form = BonificacionPersonalForm(instance=bonificacion)
        # Configurar inicialización de datos si es necesario
        if bonificacion.fecha:
            form.fields['fecha'].initial = bonificacion.fecha

    context = {
        'form': form,
        'bonificacion': bonificacion,
        'empleado_preseleccionado': empleado_id,
    }
    return render(request, 'bonificacion_edit.html', context)

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