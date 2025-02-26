from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from datetime import date
from django.db.models import Q
from django.views.generic.edit import CreateView
from .models import Empleado, Seleccion, Vinculo, Seleccion, Induccion, Prueba, Colegiatura, Curso, Experiencia, Movimientos, Retencion, Compensaciones, Evaluacion, EstudiosRealizados, Subespecialidad, InfoPersonal, Progresion, Desplazamiento, Reconocimiento, Laboral, Seguridad, Desvinculacion, Legajo
from .forms import EmpleadoForm, LegajoForm, InfoPersonalForm, VinculoForm, SeleccionForm, InduccionForm, PruebaForm, ColegiaturaForm, EstudiosRealizadosForm, SubespecialidadForm, CursoForm, ExperienciaForm, MovimientosForm, RetencionForm, CompensacionesForm, EvaluacionForm, ProgresionForm, DesplazamientoForm, ReconocimientoForm, LaboralForm, SeguridadForm, DesvinculacionForm

def datospersonales_lista(request):
  query = request.GET.get('searchorders', '')  # Obtén el texto ingresado en el buscador
  filters = Q(apellido_paterno__icontains=query) | Q(apellido_materno__icontains=query) | Q(nombres__icontains=query)

  todos_empleados = Empleado.objects.filter(filters)

  # Preparar contexto
  context = {
    'todos_empleados': todos_empleados,
    'query': query  # Para mantener el texto en el campo de búsqueda
  }

  return render(request, 'empleados.html', context)

def legajos_lista(request):
    query = request.GET.get('buscar', '')  # Obtén el texto ingresado en el buscador
    filters = Q(regimen_laboral__icontains=query) | Q(empleado__apellido_paterno__icontains=query) | Q(empleado__apellido_materno__icontains=query) | Q(empleado__nombres__icontains=query)
    
    legajos = Legajo.objects.filter(filters)  # Obtén todos los legajos
    context = {
        'legajos': legajos,
        'query': query  # Para mantener el texto en el campo de búsqueda
    }
    return render(request, 'legajos_lista.html', context)

def empleado_crear(request):
  if request.method == 'POST':
    form = EmpleadoForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('legajos:datos_personales')  # Cambia por el nombre de tu vista de lista
  else:
    form = EmpleadoForm()
  return render(request, 'empleado_crear.html', {'form': form})

def empleado_editar(request, empleado_id):
  empleado = get_object_or_404(Empleado, id=empleado_id)
  
  if request.method == 'POST':
    form = EmpleadoForm(request.POST, instance=empleado)
    if form.is_valid():
      form.save()
      return redirect('legajos:info_general', empleado_id=empleado_id)  # Cambia por el nombre de tu vista de lista
  else:
    form = EmpleadoForm(instance=empleado)
  
  return render(request, 'empleado_editar.html', {'form': form, 'empleado': empleado})

# Vista para crear legajo  
def crear_legajo(request):
    if request.method == 'POST':
        form = LegajoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('legajos:legajos_lista')  # Reemplaza 'lista_legajos' con tu URL de lista
    else:
        form = LegajoForm()
    return render(request, 'crear_legajo.html', {'form': form})


def info_general(request, legajo_id):
    legajo = get_object_or_404(Legajo.objects.prefetch_related(
        'infopersonal_set',
        'seleccion_set',
        'vinculo_set',
        'induccion_set',
        'prueba_set',
        'colegiatura_set',
        'curso_set',
        'experiencia_set',
        'estudiosrealizados_set',
        'subespecialidad_set',
        'movimientos_set',
        'retencion_set',
        'compensaciones_set',
        'evaluacion_set',
        'progresion_set',
        'desplazamiento_set',
        'reconocimiento_set',
        'laboral_set',
        'seguridad_set',
        'desvinculacion_set'
    ), id=legajo_id)

    context = {
        'legajo': legajo,
        'informacion_personal': legajo.infopersonal_set.all(),
        'selecciones': legajo.seleccion_set.all(),
        'vinculos': legajo.vinculo_set.all(),
        'inducciones': legajo.induccion_set.all(),
        'pruebas': legajo.prueba_set.all(),
        'colegiaturas': legajo.colegiatura_set.all(),
        'cursos': legajo.curso_set.all(),
        'experiencias': legajo.experiencia_set.all(),
        'estudios': legajo.estudiosrealizados_set.all(),
        'subespecialidades': legajo.subespecialidad_set.all(),
        'movimientos': legajo.movimientos_set.all(),
        'retenciones': legajo.retencion_set.all(),
        'compensaciones': legajo.compensaciones_set.all(),
        'evaluaciones': legajo.evaluacion_set.all(),
        'progresiones': legajo.progresion_set.all(),
        'desplazamientos': legajo.desplazamiento_set.all(),
        'reconocimientos': legajo.reconocimiento_set.all(),
        'laborales': legajo.laboral_set.all(),
        'seguridades': legajo.seguridad_set.all(),
        'desvinculaciones': legajo.desvinculacion_set.all(),
    }
    return render(request, 'info_general.html', context)

# Vista para crear Información Personal
class InfoPersonalCrearView(CreateView):
  model = InfoPersonal
  form_class = InfoPersonalForm
  template_name = 'infopersonal_crear.html'
  
  def get_initial(self):
    legajo_id = self.kwargs.get('legajo_id')
    initial = super().get_initial()
    if legajo_id:
      initial['legajo'] = Legajo.objects.get(id=legajo_id)  # Obtener la instancia completa
    return initial

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    legajo_id = self.kwargs.get('legajo_id')
    if legajo_id:
      context['legajo_preseleccionado'] = Legajo.objects.get(id=legajo_id)
    return context

  def get_success_url(self):
    legajo_id = self.kwargs.get('legajo_id')
    return reverse('legajos:info_general', kwargs={'legajo_id': legajo_id})

  def form_valid(self, form):
    # Asociar la ausencia al legajo automáticamente
    legajo_id = self.kwargs.get('legajo_id')
    if legajo_id:
      form.instance.legajo = Legajo.objects.get(id=legajo_id)

    # Manejo de la acción del botón
    action = self.request.POST.get('action')
    self.object = form.save()
    if action == 'save_and_add_more':
      return redirect('legajos:infopersonal_crear', legajo_id=legajo_id)
    elif action == 'save_and_exit':
      return super().form_valid(form)

    return super().form_valid(form)

# Vista para editar Información Personal
def infopersonal_editar(request, infopersonal_id, legajo_id=None):
  infopersonal = get_object_or_404(InfoPersonal, id=infopersonal_id)

  if not legajo_id:
    legajo = infopersonal.legajo
    legajo_id = legajo.id if legajo else None

  if request.method == 'POST':
    form = InfoPersonalForm(request.POST, request.FILES, instance=infopersonal)
    if form.is_valid():
      infopersonal = form.save(commit=False)
      infopersonal.save()
      return redirect('legajos:info_general', legajo_id=legajo_id)
  else:
    form = InfoPersonalForm(instance=infopersonal)

  context = {
    'form': form,
    'infopersonal': infopersonal,
    'legajo_preseleccionado': legajo_id,
  }
  return render(request, 'infopersonal_edit.html', context)

# Vista para crear seleccion
class SeleccionCrearView(CreateView):
  model = Seleccion
  form_class = SeleccionForm
  template_name = 'seleccion_crear.html'

  def get_initial(self):
    legajo_id = self.kwargs.get('legajo_id')
    initial = super().get_initial()
    if legajo_id:
      initial['legajo'] = [legajo_id]
    return initial

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    legajo_id = self.kwargs.get('legajo_id')
    if legajo_id:
      context['legajo_preseleccionado'] = Legajo.objects.get(id=legajo_id)
    return context

  def get_success_url(self):
    legajo_id = self.kwargs.get('legajo_id')
    return reverse('legajos:info_general', kwargs={'legajo_id': legajo_id})
  
  def form_valid(self, form):
    # Guarda el formulario
    self.object = form.save()

    # Maneja la acción según el botón presionado
    action = self.request.POST.get('action')
    if action == 'save_and_add_more':
      # Redirige a la misma página para seguir agregando
      legajo_id = self.kwargs.get('legajo_id')
      return redirect('legajos:seleccion_crear', legajo_id=legajo_id)
    elif action == 'save_and_exit':
      # Redirige a info_general
      return super().form_valid(form)

    return super().form_valid(form)

def seleccion_editar(request, seleccion_id, legajo_id=None):
  seleccion = get_object_or_404(Seleccion, id=seleccion_id)

  if not legajo_id:
    legajo = seleccion.legajo.first()
    legajo_id = legajo.id if legajo else None

  if request.method == 'POST':
    form = SeleccionForm(request.POST, request.FILES, instance=seleccion)
    if form.is_valid():
      seleccion = form.save(commit=False)
      seleccion.save()
      form.save_m2m()
      return redirect('legajos:info_general', legajo_id=legajo_id)
  else:
    form = SeleccionForm(instance=seleccion)

  context = {
    'form': form,
    'seleccion': seleccion,
    'legajo_preseleccionado': legajo_id,
  }
  return render(request, 'seleccion_edit.html', context)

# Vista para crear Vínculo
class VinculoCrearView(CreateView):
  model = Vinculo
  form_class = VinculoForm
  template_name = 'vinculo_crear.html'

  def get_initial(self):
    legajo_id = self.kwargs.get('legajo_id')
    initial = super().get_initial()
    if legajo_id:
      initial['legajo'] = [legajo_id]
    return initial

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    legajo_id = self.kwargs.get('legajo_id')
    if legajo_id:
      context['legajo_preseleccionado'] = Legajo.objects.get(id=legajo_id)
    return context

  def get_success_url(self):
    legajo_id = self.kwargs.get('legajo_id')
    return reverse('legajos:info_general', kwargs={'legajo_id': legajo_id})

  def form_valid(self, form):
    # Guarda el formulario
    self.object = form.save()

    # Maneja la acción según el botón presionado
    action = self.request.POST.get('action')
    if action == 'save_and_add_more':
      # Redirige a la misma página para seguir agregando
      legajo_id = self.kwargs.get('legajo_id')
      return redirect('legajos:vinculo_crear', legajo_id=legajo_id)
    elif action == 'save_and_exit':
      # Redirige a info_personal
      return super().form_valid(form) 

    return super().form_valid(form)

def vinculo_editar(request, vinculo_id, legajo_id=None):
  vinculo = get_object_or_404(Vinculo, id=vinculo_id)

  if not legajo_id:
    legajo = vinculo.legajo.first()
    legajo_id = legajo.id if legajo else None

  if request.method == 'POST':
    form = VinculoForm(request.POST, request.FILES, instance=vinculo)
    if form.is_valid():
      vinculo = form.save(commit=False)
      vinculo.save()
      form.save_m2m()
      return redirect('legajos:info_general', legajo_id=legajo_id)
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
    'legajo_preseleccionado': legajo_id,
  }
  return render(request, 'vinculo_edit.html', context)

# Vista para crear Inducción del Personal
class InduccionCrearView(CreateView):
  model = Induccion
  form_class = InduccionForm
  template_name = 'induccion_crear.html'

  def get_initial(self):
    legajo_id = self.kwargs.get('legajo_id')
    initial = super().get_initial()
    if legajo_id:
      initial['legajo'] = [legajo_id]
    return initial

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    legajo_id = self.kwargs.get('legajo_id')
    if legajo_id:
      context['legajo_preseleccionado'] = Legajo.objects.get(id=legajo_id)
    return context

  def get_success_url(self):
    legajo_id = self.kwargs.get('legajo_id')
    return reverse('legajos:info_general', kwargs={'legajo_id': legajo_id})
  
  def form_valid(self, form):
    # Guarda el formulario
    self.object = form.save()

    # Maneja la acción según el botón presionado
    action = self.request.POST.get('action')
    if action == 'save_and_add_more':
      # Redirige a la misma página para seguir agregando
      legajo_id = self.kwargs.get('legajo_id')
      return redirect('legajos:induccion_crear', legajo_id=legajo_id)
    elif action == 'save_and_exit':
      # Redirige a info_personal
      return super().form_valid(form)

    return super().form_valid(form)

def induccion_editar(request, induccion_id, legajo_id=None):
  induccion = get_object_or_404(Induccion, id=induccion_id)

  if not legajo_id:
    legajo = induccion.legajo.first()
    legajo_id = legajo.id if legajo else None

  if request.method == 'POST':
    form = InduccionForm(request.POST, request.FILES, instance=induccion)
    if form.is_valid():
      induccion = form.save(commit=False)
      induccion.save()
      form.save_m2m()
      return redirect('legajos:info_general', legajo_id=legajo_id)
  else:
    form = InduccionForm(instance=induccion)

  context = {
    'form': form,
    'induccion': induccion,
    'legajo_preseleccionado': legajo_id,
  }
  return render(request, 'induccion_edit.html', context)

# Vista para crear Período de Prueba
class PruebaCrearView(CreateView):
  model = Prueba
  form_class = PruebaForm
  template_name = 'prueba_crear.html'
  
  def get_initial(self):
    legajo_id = self.kwargs.get('legajo_id')
    initial = super().get_initial()
    if legajo_id:
      initial['legajo'] = Legajo.objects.get(id=legajo_id)  # Obtener la instancia completa
    return initial

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    legajo_id = self.kwargs.get('legajo_id')
    if legajo_id:
      context['legajo_preseleccionado'] = Legajo.objects.get(id=legajo_id)
    return context

  def get_success_url(self):
    legajo_id = self.kwargs.get('legajo_id')
    return reverse('legajos:info_general', kwargs={'legajo_id': legajo_id})

  def form_valid(self, form):
    # Asociar la ausencia al legajo automáticamente
    legajo_id = self.kwargs.get('legajo_id')
    if legajo_id:
      form.instance.legajo = Legajo.objects.get(id=legajo_id)

    # Manejo de la acción del botón
    action = self.request.POST.get('action')
    self.object = form.save()
    if action == 'save_and_add_more':
      return redirect('legajos:prueba_crear', legajo_id=legajo_id)
    elif action == 'save_and_exit':
      return super().form_valid(form)

    return super().form_valid(form)

def prueba_editar(request, prueba_id, legajo_id=None):
  prueba = get_object_or_404(Prueba, id=prueba_id)

  if not legajo_id:
    legajo = prueba.legajo
    legajo_id = legajo.id if legajo else None

  if request.method == 'POST':
    form = PruebaForm(request.POST, request.FILES, instance=prueba)
    if form.is_valid():
      prueba = form.save(commit=False)
      prueba.save()
      return redirect('legajos:info_general', legajo_id=legajo_id)
  else:
    form = PruebaForm(instance=prueba)

  context = {
    'form': form,
    'prueba': prueba,
    'legajo_preseleccionado': legajo_id,
  }
  return render(request, 'prueba_edit.html', context)

# Vista para crear Colegiatura o Habilitación Profesional
class ColegiaturaCrearView(CreateView):
  model = Colegiatura
  form_class = ColegiaturaForm
  template_name = 'colegiatura_crear.html'
  
  def get_initial(self):
    legajo_id = self.kwargs.get('legajo_id')
    initial = super().get_initial()
    if legajo_id:
      initial['legajo'] = Legajo.objects.get(id=legajo_id)  # Obtener la instancia completa
    return initial

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    legajo_id = self.kwargs.get('legajo_id')
    if legajo_id:
      context['legajo_preseleccionado'] = Legajo.objects.get(id=legajo_id)
    return context

  def get_success_url(self):
    legajo_id = self.kwargs.get('legajo_id')
    return reverse('legajos:info_general', kwargs={'legajo_id': legajo_id})

  def form_valid(self, form):
    # Asociar la ausencia al legajo automáticamente
    legajo_id = self.kwargs.get('legajo_id')
    if legajo_id:
      form.instance.legajo = Legajo.objects.get(id=legajo_id)

    # Manejo de la acción del botón
    action = self.request.POST.get('action')
    self.object = form.save()
    if action == 'save_and_add_more':
      return redirect('legajos:colegiatura_crear', legajo_id=legajo_id)
    elif action == 'save_and_exit':
      return super().form_valid(form)

    return super().form_valid(form)

def colegiatura_editar(request, colegiatura_id, legajo_id=None):
  colegiatura = get_object_or_404(Colegiatura, id=colegiatura_id)

  if not legajo_id:
    legajo = colegiatura.legajo
    legajo_id = legajo.id if legajo else None

  if request.method == 'POST':
    form = ColegiaturaForm(request.POST, request.FILES, instance=colegiatura)
    if form.is_valid():
      colegiatura = form.save(commit=False)
      colegiatura.save()
      return redirect('legajos:info_general', legajo_id=legajo_id)
  else:
    form = ColegiaturaForm(instance=colegiatura)

  context = {
    'form': form,
    'colegiatura': colegiatura,
    'legajo_preseleccionado': legajo_id,
  }
  return render(request, 'colegiatura_edit.html', context)

# Agregar Estudios Realizados
class EstudiosCrearView(CreateView):
  model = EstudiosRealizados
  form_class = EstudiosRealizadosForm
  template_name = 'estudios_crear.html'

  def get_initial(self):
    # Preseleccionar el legajo con el id proporcionado en la URL
    legajo_id = self.kwargs.get('legajo_id')
    initial = super().get_initial()
    if legajo_id:
      initial['legajo'] = legajo_id
    return initial

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    legajo_id = self.kwargs.get('legajo_id')
    if legajo_id:
      context['legajo_preseleccionado'] = Legajo.objects.get(id=legajo_id)
    return context

  def get_success_url(self):
    # Redirigir a la página de detalles del legajo luego de guardar
    legajo_id = self.kwargs.get('legajo_id')
    return reverse('legajos:info_general', kwargs={'legajo_id': legajo_id})

  def form_valid(self, form):
    # Asociar el estudio al legajo automáticamente
    legajo_id = self.kwargs.get('legajo_id')
    if legajo_id:
      form.instance.legajo = Legajo.objects.get(id=legajo_id)

    # Manejo de la acción del botón
    action = self.request.POST.get('action')
    self.object = form.save()
    if action == 'save_and_add_more':
      return redirect('legajos:estudios_crear', legajo_id=legajo_id)
    elif action == 'save_and_exit':
      return super().form_valid(form)

    return super().form_valid(form)
    
# Editar Estudios Realizados
def estudios_editar(request, estudio_id, legajo_id=None):
  estudio = get_object_or_404(EstudiosRealizados, id=estudio_id)

  # Obtener el legajo relacionado, si no está en la URL
  if not legajo_id:
    legajo = estudio.legajo
    legajo_id = legajo.id if legajo else None

  if request.method == 'POST':
    form = EstudiosRealizadosForm(request.POST, request.FILES, instance=estudio)
    if form.is_valid():
      estudio = form.save(commit=False)
      estudio.save()
      return redirect('legajos:info_general', legajo_id=legajo_id)
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
    'legajo_preseleccionado': legajo_id,
  }
  return render(request, 'estudios_edit.html', context)

# Agregar Subespecialidad
class SubespecialidadCrearView(CreateView):
  model = Subespecialidad
  form_class = SubespecialidadForm
  template_name = 'subespecialidad_crear.html'

  def get_initial(self):
    # Preseleccionar el legajo con el id proporcionado en la URL
    legajo_id = self.kwargs.get('legajo_id')
    initial = super().get_initial()
    if legajo_id:
      initial['legajo'] = legajo_id
    return initial

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    legajo_id = self.kwargs.get('legajo_id')
    if legajo_id:
      context['legajo_preseleccionado'] = Legajo.objects.get(id=legajo_id)
    return context

  def get_success_url(self):
    # Redirigir a la página de detalles del legajo luego de guardar
    legajo_id = self.kwargs.get('legajo_id')
    return reverse('legajos:info_general', kwargs={'legajo_id': legajo_id})

  def form_valid(self, form):
    # Asociar el subespecialidad al legajo automáticamente
    legajo_id = self.kwargs.get('legajo_id')
    if legajo_id:
      form.instance.legajo = Legajo.objects.get(id=legajo_id)

    # Manejo de la acción del botón
    action = self.request.POST.get('action')
    self.object = form.save()
    if action == 'save_and_add_more':
      return redirect('legajos:subespecialidad_crear', legajo_id=legajo_id)
    elif action == 'save_and_exit':
      return super().form_valid(form)

    return super().form_valid(form)
    
# Editar Subespecialidad
def subespecialidad_editar(request, subespecialidad_id, legajo_id=None):
  subespecialidad = get_object_or_404(Subespecialidad, id=subespecialidad_id)

  # Obtener el legajo relacionado, si no está en la URL
  if not legajo_id:
    legajo = subespecialidad.legajo
    legajo_id = legajo.id if legajo else None

  if request.method == 'POST':
    form = SubespecialidadForm(request.POST, request.FILES, instance=subespecialidad)
    if form.is_valid():
      subespecialidad = form.save(commit=False)
      subespecialidad.save()
      return redirect('legajos:info_general', legajo_id=legajo_id)
  else:
    form = SubespecialidadForm(instance=subespecialidad)

  context = {
    'form': form,
    'estudio': subespecialidad,
    'legajo_preseleccionado': legajo_id,
  }
  return render(request, 'subespecialidad_edit.html', context)

# Vista para crear Cursos
class CursoCrearView(CreateView):
  model = Curso
  form_class = CursoForm
  template_name = 'curso_crear.html'
  
  def get_initial(self):
    legajo_id = self.kwargs.get('legajo_id')
    initial = super().get_initial()
    if legajo_id:
      initial['legajo'] = Legajo.objects.get(id=legajo_id)  # Obtener la instancia completa
    return initial

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    legajo_id = self.kwargs.get('legajo_id')
    if legajo_id:
      context['legajo_preseleccionado'] = Legajo.objects.get(id=legajo_id)
    return context

  def get_success_url(self):
    legajo_id = self.kwargs.get('legajo_id')
    return reverse('legajos:info_general', kwargs={'legajo_id': legajo_id})

  def form_valid(self, form):
    # Asociar la ausencia al legajo automáticamente
    legajo_id = self.kwargs.get('legajo_id')
    if legajo_id:
      form.instance.legajo = Legajo.objects.get(id=legajo_id)

    # Manejo de la acción del botón
    action = self.request.POST.get('action')
    self.object = form.save()
    if action == 'save_and_add_more':
      return redirect('legajos:curso_crear', legajo_id=legajo_id)
    elif action == 'save_and_exit':
      return super().form_valid(form)

    return super().form_valid(form)

def curso_editar(request, curso_id, legajo_id=None):
  curso = get_object_or_404(Curso, id=curso_id)

  if not legajo_id:
    legajo = curso.legajo
    legajo_id = legajo.id if legajo else None

  if request.method == 'POST':
    form = CursoForm(request.POST, request.FILES, instance=curso)
    if form.is_valid():
      curso = form.save(commit=False)
      curso.save()
      return redirect('legajos:info_general', legajo_id=legajo_id)
  else:
    form = CursoForm(instance=curso)

  context = {
    'form': form,
    'curso': curso,
    'legajo_preseleccionado': legajo_id,
  }
  return render(request, 'curso_edit.html', context)

# Vista para crear Experiencia
class ExperienciaCrearView(CreateView):
  model = Experiencia
  form_class = ExperienciaForm
  template_name = 'experiencia_crear.html'
  
  def get_initial(self):
    legajo_id = self.kwargs.get('legajo_id')
    initial = super().get_initial()
    if legajo_id:
      initial['legajo'] = Legajo.objects.get(id=legajo_id)  # Obtener la instancia completa
    return initial

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    legajo_id = self.kwargs.get('legajo_id')
    if legajo_id:
      context['legajo_preseleccionado'] = Legajo.objects.get(id=legajo_id)
    return context

  def get_success_url(self):
    legajo_id = self.kwargs.get('legajo_id')
    return reverse('legajos:info_general', kwargs={'legajo_id': legajo_id})

  def form_valid(self, form):
    # Asociar la experiencia al legajo automáticamente
    legajo_id = self.kwargs.get('legajo_id')
    if legajo_id:
      form.instance.legajo = Legajo.objects.get(id=legajo_id)

    # Manejo de la acción del botón
    action = self.request.POST.get('action')
    self.object = form.save()
    if action == 'save_and_add_more':
      return redirect('legajos:experiencia_crear', legajo_id=legajo_id)
    elif action == 'save_and_exit':
      return super().form_valid(form)

    return super().form_valid(form)

# Vista para editar Experiencia
def experiencia_editar(request, experiencia_id, legajo_id=None):
  experiencia = get_object_or_404(Experiencia, id=experiencia_id)

  if not legajo_id:
    legajo = experiencia.legajo
    legajo_id = legajo.id if legajo else None

  if request.method == 'POST':
    form = ExperienciaForm(request.POST, request.FILES, instance=experiencia)
    if form.is_valid():
      experiencia = form.save(commit=False)
      experiencia.save()
      return redirect('legajos:info_general', legajo_id=legajo_id)
  else:
    form = ExperienciaForm(instance=experiencia)

  context = {
    'form': form,
    'experiencia': experiencia,
    'legajo_preseleccionado': legajo_id,
  }
  return render(request, 'experiencia_edit.html', context)

#Agregar Movimientos de Personal
class MovimientosCrearView(CreateView):
  model = Movimientos
  form_class = MovimientosForm
  template_name = 'movimientos_crear.html'

  def get_initial(self):
    # Preseleccionar el legajo con el ID proporcionado en la URL
    legajo_id = self.kwargs.get('legajo_id')
    initial = super().get_initial()
    if legajo_id:
      initial['legajo'] = legajo_id
    return initial

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    legajo_id = self.kwargs.get('legajo_id')
    if legajo_id:
      context['legajo_preseleccionado'] = Legajo.objects.get(id=legajo_id)
    return context

  def get_success_url(self):
    # Redirigir a la página de detalles del legajo luego de guardar
    legajo_id = self.kwargs.get('legajo_id')
    return reverse('legajos:info_general', kwargs={'legajo_id': legajo_id})

  def form_valid(self, form):
    # Asociar el movimiento al legajo automáticamente
    legajo_id = self.kwargs.get('legajo_id')
    if legajo_id:
      form.instance.legajo = Legajo.objects.get(id=legajo_id)

    # Manejo de la acción del botón
    action = self.request.POST.get('action')
    self.object = form.save()
    if action == 'save_and_add_more':
      return redirect('legajos:movimientos_crear', legajo_id=legajo_id)
    elif action == 'save_and_exit':
      return super().form_valid(form)

    return super().form_valid(form)

#Editar Movimientos de Personal
def movimientos_editar(request, movimientos_id, legajo_id=None):
  movimientos = get_object_or_404(Movimientos, id=movimientos_id)

  # Obtener el legajo relacionado, si no está en la URL
  if not legajo_id:
    legajo = movimientos.legajo
    legajo_id = legajo.id if legajo else None

  if request.method == 'POST':
    form = MovimientosForm(request.POST, request.FILES, instance=movimientos)
    if form.is_valid():
      movimientos = form.save(commit=False)
      movimientos.save()
      return redirect('legajos:info_general', legajo_id=legajo_id)
  else:
    form = MovimientosForm(instance=movimientos)
    # Configurar inicialización de fechas si es necesario
    if movimientos.desde:
      form.fields['desde'].initial = movimientos.desde
    if movimientos.hasta:
      form.fields['hasta'].initial = movimientos.hasta

  context = {
    'form': form,
    'movimientos': movimientos,
    'legajo_preseleccionado': legajo_id,
  }
  return render(request, 'movimientos_edit.html', context)

# Vista para crear Exoneración de Retención
class RetencionCrearView(CreateView):
  model = Retencion
  form_class = RetencionForm
  template_name = 'retencion_crear.html'
  
  def get_initial(self):
    legajo_id = self.kwargs.get('legajo_id')
    initial = super().get_initial()
    if legajo_id:
      initial['legajo'] = Legajo.objects.get(id=legajo_id)  # Obtener la instancia completa
    return initial

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    legajo_id = self.kwargs.get('legajo_id')
    if legajo_id:
      context['legajo_preseleccionado'] = Legajo.objects.get(id=legajo_id)
    return context

  def get_success_url(self):
    legajo_id = self.kwargs.get('legajo_id')
    return reverse('legajos:info_general', kwargs={'legajo_id': legajo_id})

  def form_valid(self, form):
    # Asociar la ausencia al legajo automáticamente
    legajo_id = self.kwargs.get('legajo_id')
    if legajo_id:
      form.instance.legajo = Legajo.objects.get(id=legajo_id)

    # Manejo de la acción del botón
    action = self.request.POST.get('action')
    self.object = form.save()
    if action == 'save_and_add_more':
      return redirect('legajos:retencion_crear', legajo_id=legajo_id)
    elif action == 'save_and_exit':
      return super().form_valid(form)

    return super().form_valid(form)


def retencion_editar(request, retencion_id, legajo_id=None):
  retencion = get_object_or_404(Retencion, id=retencion_id)

  if not legajo_id:
    legajo = retencion.legajo
    legajo_id = legajo.id if legajo else None

  if request.method == 'POST':
    form = RetencionForm(request.POST, request.FILES, instance=retencion)
    if form.is_valid():
      retencion = form.save(commit=False)
      retencion.save()
      return redirect('legajos:info_general', legajo_id=legajo_id)
  else:
    form = RetencionForm(instance=retencion)

  context = {
    'form': form,
    'retencion': retencion,
    'legajo_preseleccionado': legajo_id,
  }
  return render(request, 'retencion_edit.html', context)

# Agregar Compensaciones
class CompensacionesCrearView(CreateView):
  model = Compensaciones
  form_class = CompensacionesForm
  template_name = 'compensaciones_crear.html'

  def get_initial(self):
    # Preseleccionar el legajo con el ID proporcionado en la URL
    legajo_id = self.kwargs.get('legajo_id')
    initial = super().get_initial()
    if legajo_id:
      initial['legajo'] = legajo_id
    return initial

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    legajo_id = self.kwargs.get('legajo_id')
    if legajo_id:
      context['legajo_preseleccionado'] = Legajo.objects.get(id=legajo_id)
    return context

  def get_success_url(self):
    # Redirigir a la página de detalles del legajo luego de guardar
    legajo_id = self.kwargs.get('legajo_id')
    return reverse('legajos:info_general', kwargs={'legajo_id': legajo_id})

  def form_valid(self, form):
    # Asociar la bonificación al legajo automáticamente
    legajo_id = self.kwargs.get('legajo_id')
    if legajo_id:
      form.instance.legajo = Legajo.objects.get(id=legajo_id)

    # Manejo de la acción del botón
    action = self.request.POST.get('action')
    self.object = form.save()
    if action == 'save_and_add_more':
      return redirect('legajos:compensaciones_crear', legajo_id=legajo_id)
    elif action == 'save_and_exit':
      return super().form_valid(form)

    return super().form_valid(form)

#Editar Compensaciones
def compensaciones_editar(request, compensaciones_id, legajo_id=None):
  compensaciones = get_object_or_404(Compensaciones, id=compensaciones_id)

  # Obtener el legajo relacionado, si no está en la URL
  if not legajo_id:
    legajo = compensaciones.legajo
    legajo_id = legajo.id if legajo else None

  if request.method == 'POST':
    form = CompensacionesForm(request.POST, request.FILES, instance=compensaciones)
    if form.is_valid():
      compensaciones = form.save(commit=False)
      compensaciones.save()
      return redirect('legajos:info_general', legajo_id=legajo_id)
  else:
    form = CompensacionesForm(instance=compensaciones)
    # Configurar inicialización de datos si es necesario
    if compensaciones.fecha:
      form.fields['fecha'].initial = compensaciones.fecha

  context = {
    'form': form,
    'compensaciones': compensaciones,
    'legajo_preseleccionado': legajo_id,
  }
  return render(request, 'compensaciones_edit.html', context)

# Vista para crear Evaluación de Desempeño
class EvaluacionCrearView(CreateView):
  model = Evaluacion
  form_class = EvaluacionForm
  template_name = 'evaluacion_crear.html'
  
  def get_initial(self):
    legajo_id = self.kwargs.get('legajo_id')
    initial = super().get_initial()
    if legajo_id:
      initial['legajo'] = Legajo.objects.get(id=legajo_id)  # Obtener la instancia completa
    return initial

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    legajo_id = self.kwargs.get('legajo_id')
    if legajo_id:
      context['legajo_preseleccionado'] = Legajo.objects.get(id=legajo_id)
    return context

  def get_success_url(self):
    legajo_id = self.kwargs.get('legajo_id')
    return reverse('legajos:info_general', kwargs={'legajo_id': legajo_id})

  def form_valid(self, form):
    # Asociar la evaluación al legajo automáticamente
    legajo_id = self.kwargs.get('legajo_id')
    if legajo_id:
      form.instance.legajo = Legajo.objects.get(id=legajo_id)

    # Manejo de la acción del botón
    action = self.request.POST.get('action')
    self.object = form.save()
    if action == 'save_and_add_more':
      return redirect('legajos:evaluacion_crear', legajo_id=legajo_id)
    elif action == 'save_and_exit':
      return super().form_valid(form)

    return super().form_valid(form)


def evaluacion_editar(request, evaluacion_id, legajo_id=None):
  evaluacion = get_object_or_404(Evaluacion, id=evaluacion_id)

  if not legajo_id:
    legajo = evaluacion.legajo
    legajo_id = legajo.id if legajo else None

  if request.method == 'POST':
    form = EvaluacionForm(request.POST, request.FILES, instance=evaluacion)
    if form.is_valid():
      evaluacion = form.save(commit=False)
      evaluacion.save()
      return redirect('legajos:info_general', legajo_id=legajo_id)
  else:
    form = EvaluacionForm(instance=evaluacion)

  context = {
    'form': form,
    'evaluacion': evaluacion,
    'legajo_preseleccionado': legajo_id,
  }
  return render(request, 'evaluacion_edit.html', context)

# Vista para crear Progresión
class ProgresionCrearView(CreateView):
  model = Progresion
  form_class = ProgresionForm
  template_name = 'progresion_crear.html'

  def get_initial(self):
    legajo_id = self.kwargs.get('legajo_id')
    initial = super().get_initial()
    if legajo_id:
      initial['legajo'] = [legajo_id]
    return initial

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    legajo_id = self.kwargs.get('legajo_id')
    if legajo_id:
      context['legajo_preseleccionado'] = Legajo.objects.get(id=legajo_id)
    return context

  def get_success_url(self):
    legajo_id = self.kwargs.get('legajo_id')
    return reverse('legajos:info_general', kwargs={'legajo_id': legajo_id})

  def form_valid(self, form):
    # Guarda el formulario
    self.object = form.save()

    # Maneja la acción según el botón presionado
    action = self.request.POST.get('action')
    if action == 'save_and_add_more':
      # Redirige a la misma página para seguir agregando
      legajo_id = self.kwargs.get('legajo_id')
      return redirect('legajos:progresion_crear', legajo_id=legajo_id)
    elif action == 'save_and_exit':
      # Redirige a info_general
      return super().form_valid(form)

    return super().form_valid(form)

def progresion_editar(request, progresion_id, legajo_id=None):
  progresion = get_object_or_404(Progresion, id=progresion_id)

  if not legajo_id:
    legajo = progresion.legajo
    legajo_id = legajo.id if legajo else None

  if request.method == 'POST':
    form = ProgresionForm(request.POST, request.FILES, instance=progresion)
    if form.is_valid():
      progresion = form.save(commit=False)
      progresion.save()
      form.save_m2m()
      return redirect('legajos:info_general', legajo_id=legajo_id)
  else:
    form = ProgresionForm(instance=progresion)
    
  context = {
    'form': form,
    'progresion': progresion,
    'legajo_preseleccionado': legajo_id,
  }
  return render(request, 'progresion_edit.html', context)

# Vista para crear Desplazamiento
class DesplazamientoCrearView(CreateView):
  model = Desplazamiento
  form_class = DesplazamientoForm
  template_name = 'desplazamiento_crear.html'

  def get_initial(self):
    legajo_id = self.kwargs.get('legajo_id')
    initial = super().get_initial()
    if legajo_id:
      initial['legajo'] = [legajo_id]
    return initial

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    legajo_id = self.kwargs.get('legajo_id')
    if legajo_id:
      context['legajo_preseleccionado'] = Legajo.objects.get(id=legajo_id)
    return context

  def get_success_url(self):
    legajo_id = self.kwargs.get('legajo_id')
    return reverse('legajos:info_general', kwargs={'legajo_id': legajo_id})

  def form_valid(self, form):
    # Guarda el formulario
    self.object = form.save()

    # Maneja la acción según el botón presionado
    action = self.request.POST.get('action')
    if action == 'save_and_add_more':
      # Redirige a la misma página para seguir agregando
      legajo_id = self.kwargs.get('legajo_id')
      return redirect('legajos:desplazamiento_crear', legajo_id=legajo_id)
    elif action == 'save_and_exit':
      # Redirige a info_general
      return super().form_valid(form)

    return super().form_valid(form)

def desplazamiento_editar(request, desplazamiento_id, legajo_id=None):
  desplazamiento = get_object_or_404(Desplazamiento, id=desplazamiento_id)

  if not legajo_id:
    legajo = desplazamiento.legajo
    legajo_id = legajo.id if legajo else None

  if request.method == 'POST':
    form = DesplazamientoForm(request.POST, request.FILES, instance=desplazamiento)
    if form.is_valid():
      desplazamiento = form.save(commit=False)
      desplazamiento.save()
      form.save_m2m()
      return redirect('legajos:info_general', legajo_id=legajo_id)
  else:
    form = DesplazamientoForm(instance=desplazamiento)
    
  context = {
    'form': form,
    'desplazamiento': desplazamiento,
    'legajo_preseleccionado': legajo_id,
  }
  return render(request, 'desplazamiento_edit.html', context)

# Vista para crear Reconocimientos y Sanciones
class ReconocimientoCrearView(CreateView):
  model = Reconocimiento
  form_class = ReconocimientoForm
  template_name = 'reconocimiento_crear.html'

  def get_initial(self):
    legajo_id = self.kwargs.get('legajo_id')
    initial = super().get_initial()
    if legajo_id:
      initial['legajo'] = [legajo_id]
    return initial

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    legajo_id = self.kwargs.get('legajo_id')
    if legajo_id:
      context['legajo_preseleccionado'] = Legajo.objects.get(id=legajo_id)
    return context

  def get_success_url(self):
    legajo_id = self.kwargs.get('legajo_id')
    return reverse('legajos:info_general', kwargs={'legajo_id': legajo_id})

  def form_valid(self, form):
    # Guarda el formulario
    self.object = form.save()

    # Maneja la acción según el botón presionado
    action = self.request.POST.get('action')
    if action == 'save_and_add_more':
      # Redirige a la misma página para seguir agregando
      legajo_id = self.kwargs.get('legajo_id')
      return redirect('legajos:reconocimiento_crear', legajo_id=legajo_id)
    elif action == 'save_and_exit':
      # Redirige a info_general
      return super().form_valid(form)

    return super().form_valid(form)

def reconocimiento_editar(request, reconocimiento_id, legajo_id=None):
  reconocimiento = get_object_or_404(Reconocimiento, id=reconocimiento_id)

  if not legajo_id:
    legajo = reconocimiento.legajo
    legajo_id = legajo.id if legajo else None

  if request.method == 'POST':
    form = ReconocimientoForm(request.POST, request.FILES, instance=reconocimiento)
    if form.is_valid():
      reconocimiento = form.save(commit=False)
      reconocimiento.save()
      form.save_m2m()
      return redirect('legajos:info_general', legajo_id=legajo_id)
  else:
    form = ReconocimientoForm(instance=reconocimiento)
    
  context = {
    'form': form,
    'reconocimiento': reconocimiento,
    'legajo_preseleccionado': legajo_id,
  }
  return render(request, 'reconocimiento_edit.html', context)

# Vista para crear Relaciones Laborales
class LaboralCrearView(CreateView):
  model = Laboral
  form_class = LaboralForm
  template_name = 'laboral_crear.html'

  def get_initial(self):
    legajo_id = self.kwargs.get('legajo_id')
    initial = super().get_initial()
    if legajo_id:
      initial['legajo'] = [legajo_id]
    return initial

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    legajo_id = self.kwargs.get('legajo_id')
    if legajo_id:
      context['legajo_preseleccionado'] = Legajo.objects.get(id=legajo_id)
    return context

  def get_success_url(self):
    legajo_id = self.kwargs.get('legajo_id')
    return reverse('legajos:info_general', kwargs={'legajo_id': legajo_id})

  def form_valid(self, form):
    # Guarda el formulario
    self.object = form.save()

    # Maneja la acción según el botón presionado
    action = self.request.POST.get('action')
    if action == 'save_and_add_more':
      # Redirige a la misma página para seguir agregando
      legajo_id = self.kwargs.get('legajo_id')
      return redirect('legajos:laboral_crear', legajo_id=legajo_id)
    elif action == 'save_and_exit':
      # Redirige a info_general
      return super().form_valid(form)

    return super().form_valid(form)

def laboral_editar(request, laboral_id, legajo_id=None):
  laboral = get_object_or_404(Laboral, id=laboral_id)

  if not legajo_id:
    legajo = laboral.legajo
    legajo_id = legajo.id if legajo else None

  if request.method == 'POST':
    form = LaboralForm(request.POST, request.FILES, instance=laboral)
    if form.is_valid():
      laboral = form.save(commit=False)
      laboral.save()
      form.save_m2m()
      return redirect('legajos:info_general', legajo_id=legajo_id)
  else:
    form = LaboralForm(instance=laboral)
    
  context = {
    'form': form,
    'laboral': laboral,
    'legajo_preseleccionado': legajo_id,
  }
  return render(request, 'laboral_edit.html', context)

# Vista para crear SST y Bienestar Social
class SeguridadCrearView(CreateView):
  model = Seguridad
  form_class = SeguridadForm
  template_name = 'seguridad_crear.html'

  def get_initial(self):
    legajo_id = self.kwargs.get('legajo_id')
    initial = super().get_initial()
    if legajo_id:
      initial['legajo'] = [legajo_id]
    return initial

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    legajo_id = self.kwargs.get('legajo_id')
    if legajo_id:
      context['legajo_preseleccionado'] = Legajo.objects.get(id=legajo_id)
    return context

  def get_success_url(self):
    legajo_id = self.kwargs.get('legajo_id')
    return reverse('legajos:info_general', kwargs={'legajo_id': legajo_id})

  def form_valid(self, form):
    # Guarda el formulario
    self.object = form.save()

    # Maneja la acción según el botón presionado
    action = self.request.POST.get('action')
    if action == 'save_and_add_more':
      # Redirige a la misma página para seguir agregando
      legajo_id = self.kwargs.get('legajo_id')
      return redirect('legajos:seguridad_crear', legajo_id=legajo_id)
    elif action == 'save_and_exit':
      # Redirige a info_general
      return super().form_valid(form)

    return super().form_valid(form)

def seguridad_editar(request, seguridad_id, legajo_id=None):
  seguridad = get_object_or_404(Seguridad, id=seguridad_id)

  if not legajo_id:
    legajo = seguridad.legajo
    legajo_id = legajo.id if legajo else None

  if request.method == 'POST':
    form = SeguridadForm(request.POST, request.FILES, instance=seguridad)
    if form.is_valid():
      seguridad = form.save(commit=False)
      seguridad.save()
      form.save_m2m()
      return redirect('legajos:info_general', legajo_id=legajo_id)
  else:
    form = SeguridadForm(instance=seguridad)
    
  context = {
    'form': form,
    'seguridad': seguridad,
    'legajo_preseleccionado': legajo_id,
  }
  return render(request, 'seguridad_edit.html', context)

# Vista para crear Desvinculación
class DesvinculacionCrearView(CreateView):
  model = Desvinculacion
  form_class = DesvinculacionForm
  template_name = 'desvinculacion_crear.html'

  def get_initial(self):
    legajo_id = self.kwargs.get('legajo_id')
    initial = super().get_initial()
    if legajo_id:
      initial['legajo'] = [legajo_id]
    return initial

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    legajo_id = self.kwargs.get('legajo_id')
    if legajo_id:
      context['legajo_preseleccionado'] = Legajo.objects.get(id=legajo_id)
    return context

  def get_success_url(self):
    legajo_id = self.kwargs.get('legajo_id')
    return reverse('legajos:info_general', kwargs={'legajo_id': legajo_id})

  def form_valid(self, form):
    # Guarda el formulario
    self.object = form.save()

    # Maneja la acción según el botón presionado
    action = self.request.POST.get('action')
    if action == 'save_and_add_more':
      # Redirige a la misma página para seguir agregando
      legajo_id = self.kwargs.get('legajo_id')
      return redirect('legajos:desvinculacion_crear', legajo_id=legajo_id)
    elif action == 'save_and_exit':
      # Redirige a info_general
      return super().form_valid(form)

    return super().form_valid(form)

def desvinculacion_editar(request, desvinculacion_id, legajo_id=None):
  desvinculacion = get_object_or_404(Desvinculacion, id=desvinculacion_id)

  if not legajo_id:
    legajo = desvinculacion.legajo
    legajo_id = legajo.id if legajo else None

  if request.method == 'POST':
    form = DesvinculacionForm(request.POST, request.FILES, instance=desvinculacion)
    if form.is_valid():
      desvinculacion = form.save(commit=False)
      desvinculacion.save()
      form.save_m2m()
      return redirect('legajos:info_general', legajo_id=legajo_id)
  else:
    form = DesvinculacionForm(instance=desvinculacion)
    
  context = {
    'form': form,
    'desvinculacion': desvinculacion,
    'legajo_preseleccionado': legajo_id,
  }
  return render(request, 'desvinculacion_edit.html', context)

# Vista para seccion documentos
def documentos(request):
    return render(request, 'documentos.html')

# Vista para dashboard
def dashboard(request):
    return render(request, 'dashboard.html')