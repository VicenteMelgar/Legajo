from django.db import models
from django.utils.html import format_html
from .choices import estados, sexo, departamento, tipo_vinculo, tipo_historial, documento, documento_identidad, condicion_laboral, documentos_informacion, documentos_seleccion, documentos_induccion, documentos_prueba, documentos_cursos, documentos_experiencia, documentos_retencion, periodo_evaluacion, documentos_reconocimientos, documentos_laboral, documentos_sst, documentos_desvinculacion, tipo_movimientos, documentos_grado, documentos_especialidad, departamento_oficina, documentos_regimen, grupo_ocupacional, cargos, niveles
from django.core.exceptions import ValidationError
from django.utils.formats import date_format
from django.db.models import Q
            
# Modelo de Resolución
class Resolucion(models.Model):
  documento = models.CharField(max_length=100, choices= documento, blank=True, null=True)
  numero = models.CharField(max_length=50, unique=True, verbose_name='Número de Resolución')
  tipo = models.CharField(max_length=100, choices=tipo_vinculo)
  otro = models.CharField(max_length=1000, null=True, blank=True, verbose_name='Otro Documento, Especificar:')
  fecha = models.DateField(verbose_name="Fecha del Documento")
  pdf = models.FileField(upload_to='resoluciones/', verbose_name='Cargar PDF')

  def ver_pdf(self):
      if self.pdf:
          return format_html('<a href="{}" target="_blank">Ver PDF</a>', self.pdf.url)
      return "No disponible"
  
  ver_pdf.short_description = "Visualizar PDF"

  def __str__(self):
      return f'{self.documento} Nº {self.numero}'
  
  class Meta:
    ordering = ['-fecha']
    verbose_name = 'Resolución'
    verbose_name_plural = 'Resoluciones'
    
# Modelo para agregar empleado
class Empleado(models.Model):
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    nombres = models.CharField(max_length=50)
    documento_identidad = models.CharField(max_length=100, choices=documento_identidad)
    numero_documento = models.CharField(max_length=15, unique=True)
    sexo = models.CharField(max_length=1, choices= sexo, blank=True, null=True)
    estado_civil = models.CharField(max_length=10, choices= estados, blank=True, null=True)
    telefono = models.CharField(max_length=12, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    departamento = models.CharField(max_length=50, choices= departamento, blank=True, null=True)
    provincia = models.CharField(max_length=50, blank=True, null=True)
    distrito = models.CharField(max_length=50, blank=True, null=True)
    domicilio = models.CharField(max_length=100, blank=True, null=True)
    
    def oficina_actual(self):
        return self.oficinahistorial_set.filter(fecha_fin__isnull=True).order_by('-fecha_inicio').first()

    def condicion_actual(self):
        return self.condicionhistorial_set.filter(fecha_fin__isnull=True).order_by('-fecha_inicio').first()

    def grupo_actual(self):
        return self.grupohistorial_set.filter(fecha_fin__isnull=True).order_by('-fecha_inicio').first()

    def cargo_actual(self):
        return self.cargohistorial_set.filter(fecha_fin__isnull=True).order_by('-fecha_inicio').first()

    def nivel_actual(self):
        return self.nivelhistorial_set.filter(fecha_fin__isnull=True).order_by('-fecha_inicio').first()

    def plaza_actual(self):
        return self.plazahistorial_set.filter(fecha_fin__isnull=True).order_by('-fecha_inicio').first()

    def __str__(self):
        return f"{self.apellido_paterno} {self.apellido_materno}, {self.nombres}"
    
    class Meta:
        ordering = ['apellido_paterno']
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

# Modelo de oficina
class OficinaHistorial(models.Model):
  empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
  resolucion = models.ForeignKey(Resolucion, on_delete=models.CASCADE, verbose_name='Resolución')
  denominacion = models.CharField(max_length=100, choices=departamento_oficina, verbose_name='Departamento u Oficina')
  fecha_inicio = models.DateField(null=True, blank=True, verbose_name="Fecha de Inicio")
  fecha_fin = models.DateField(blank=True, null=True, verbose_name='Fecha de Finalización')

  def __str__(self):
      return self.denominacion
  
  class Meta:
    ordering = ['-fecha_inicio']
    verbose_name = 'Departamento u Oficina'
    verbose_name_plural = 'Departamentos u Oficinas'
    
# Modelo de Condición Laboral 
class CondicionHistorial(models.Model):
  empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
  resolucion = models.ForeignKey(Resolucion, on_delete=models.CASCADE, verbose_name='Resolución')
  denominacion = models.CharField(max_length=100, choices= condicion_laboral, verbose_name='Denominación')
  fecha_inicio = models.DateField(null=True, blank=True, verbose_name="Fecha de Inicio")
  fecha_fin = models.DateField(blank=True, null=True, verbose_name='Fecha de Finalización')

  def __str__(self):
      return self.denominacion
  
  class Meta:
    ordering = ['-fecha_inicio']
    verbose_name = 'Condición Laboral'
    verbose_name_plural = 'Condiciónes Laborales'

# Modelo de Grupo Ocupacional
class GrupoHistorial(models.Model):
  empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
  resolucion = models.ForeignKey(Resolucion, on_delete=models.CASCADE, verbose_name='Resolución')
  denominacion = models.CharField(max_length=100, choices= grupo_ocupacional, verbose_name='Denominación')
  fecha_inicio = models.DateField(null=True, blank=True, verbose_name="Fecha de Inicio")
  fecha_fin = models.DateField(blank=True, null=True, verbose_name='Fecha de Finalización')

  def __str__(self):
      return self.denominacion
  
  class Meta:
    ordering = ['-fecha_inicio']
    verbose_name = 'Grupo Ocupacional'
    verbose_name_plural = 'Grupos Ocupacionales'
    
# Modelo de Cargo
class CargoHistorial(models.Model):
  empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
  resolucion = models.ForeignKey(Resolucion, on_delete=models.CASCADE, verbose_name='Resolución')
  denominacion = models.CharField(max_length=100, choices= cargos, verbose_name='Cargo')
  fecha_inicio = models.DateField(null=True, blank=True, verbose_name="Fecha de Inicio")
  fecha_fin = models.DateField(blank=True, null=True, verbose_name='Fecha de Finalización')

  def __str__(self):
      return self.denominacion
  
  class Meta:
    ordering = ['-fecha_inicio']
    verbose_name = 'Cargo'
    verbose_name_plural = 'Cargos'
    
# Modelo de Nivel
class NivelHistorial(models.Model):
  empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
  resolucion = models.ForeignKey(Resolucion, on_delete=models.CASCADE, verbose_name='Resolución')
  denominacion = models.CharField(max_length=100, choices= niveles, verbose_name='Denominación')
  fecha_inicio = models.DateField(null=True, blank=True, verbose_name="Fecha de Inicio")
  fecha_fin = models.DateField(blank=True, null=True, verbose_name='Fecha de Finalización')

  def __str__(self):
      return self.denominacion
  
  class Meta:
    ordering = ['-fecha_inicio']
    verbose_name = 'Nivel'
    verbose_name_plural = 'Niveles'

# Modelo de Plaza
class PlazaHistorial(models.Model):
  empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
  resolucion = models.ForeignKey(Resolucion, on_delete=models.CASCADE, verbose_name='Resolución')
  denominacion = models.CharField(max_length=100, verbose_name='Número de Plaza (airhsp)')
  fecha_inicio = models.DateField(null=True, blank=True, verbose_name="Fecha de Inicio")
  fecha_fin = models.DateField(blank=True, null=True, verbose_name='Fecha de Finalización')

  def __str__(self):
      return self.denominacion
  
  class Meta:
    ordering = ['-fecha_inicio']
    verbose_name = 'Plaza (airhsp)'
    verbose_name_plural = 'Plaza (airhsp)'
     
# Modelo para Aperturar Legajos
class Legajo(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='legajos')
    regimen_laboral = models.CharField(max_length=100, choices=documentos_regimen, verbose_name='Régimen Laboral')
    fecha_creacion = models.DateField(auto_now_add=True)
    activo = models.BooleanField(default=True)  # Para marcar el legajo actual

    def __str__(self):
        return f"{self.empleado.apellido_paterno} {self.empleado.apellido_materno}, {self.empleado.nombres} - {self.regimen_laboral}"

    def clean(self):
        super().clean()
        if self.id is None: # Si es un legajo nuevo
            if Legajo.objects.filter(empleado=self.empleado, regimen_laboral=self.regimen_laboral).exists():
                raise ValidationError(f"El empleado ya tiene un legajo de tipo {self.regimen_laboral}.")
        else: # Si es un legajo existente que se está modificando
             if Legajo.objects.filter(empleado=self.empleado, regimen_laboral=self.regimen_laboral).exclude(id=self.id).exists():
                raise ValidationError(f"El empleado ya tiene un legajo de tipo {self.regimen_laboral}.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Legajo, self).save(*args, **kwargs)

        if self.activo:
            # Desactiva los otros legajos del mismo empleado
            Legajo.objects.filter(empleado=self.empleado).exclude(id=self.id).update(activo=False)
            
# Modelo de Vinculo laboral
class Vinculo(models.Model):
  legajo = models.ForeignKey(Legajo, on_delete=models.CASCADE)
  tipo = models.CharField(max_length=100, choices=tipo_historial)
  resolucion = models.ForeignKey(Resolucion, on_delete=models.CASCADE, verbose_name='Resolución')
  descripcion = models.CharField(max_length=1000, blank=True, verbose_name='Descripción')
  
  def __str__(self):
      return self.descripcion
  
  class Meta:
    ordering = ['descripcion']
    verbose_name = 'Historial Laboral'
    verbose_name_plural = 'Historial Laboral'

# Modelo Información Personal
class InfoPersonal(models.Model):
    legajo = models.ForeignKey(Legajo, on_delete=models.CASCADE)
    documento = models.CharField(max_length=100, choices=documentos_informacion, verbose_name='Tipo de Documento')
    documento_otro = models.CharField(max_length=100, blank=True, verbose_name='Especificar otro documento')
    fecha = models.DateField(null=True, blank=True)
    pdf = models.FileField(upload_to='documentos_personales/', verbose_name='Cargar PDF')
        
    def ver_pdf(self):
        if self.pdf:
            return format_html('<a href="{}" target="_blank">Ver PDF</a>', self.pdf.url)
        return "No disponible"
    
    ver_pdf.short_description = "Visualizar PDF"
  
    class Meta:
        ordering = ['documento', '-fecha']  # Ordenar según el tipo
        verbose_name = 'Información Personal'
        verbose_name_plural = 'Información Personal'
    
    def __str__(self):
        if self.documento_otro:
            return f"{self.documento_otro} - {self.legajo}"
        return f"{self.get_documento_display()} - {self.legajo}"
      
# Modelo Proceso de Selección
class Seleccion(models.Model):
    legajo = models.ManyToManyField(Legajo)
    documento = models.CharField(max_length=100, choices=documentos_seleccion, verbose_name='Tipo de Documento')
    documento_otro = models.CharField(max_length=100, blank=True, verbose_name='Especificar otro documento')
    fecha = models.DateField(null=True, blank=True)
    descripcion = models.CharField(max_length=250, blank=True, verbose_name='Descripción')
    pdf = models.FileField(upload_to='documentos_seleccion/', verbose_name='Cargar PDF')
        
    def save(self, *args, **kwargs):
        # Si no se selecciona "Otros", limpia el campo "documento_otro"
        if self.documento != 'Otro Documento':
            self.documento_otro = ''
        super().save(*args, **kwargs)
        
    def ver_pdf(self):
        if self.pdf:
            return format_html('<a href="{}" target="_blank">Ver PDF</a>', self.pdf.url)
        return "No disponible"
    
    ver_pdf.short_description = "Visualizar PDF"
  
    class Meta:
        ordering = ['documento']  # Ordenar según el tipo
        verbose_name = 'Proceso de Selección'
        verbose_name_plural = 'Proceso de Selección'
    
    def __str__(self):
        return f"{self.get_documento_display()} - {self.legajo}"
        
# Modelo Inducción del Personal
class Induccion(models.Model):
  legajo = models.ManyToManyField(Legajo)
  documento = models.PositiveSmallIntegerField(choices=documentos_induccion, verbose_name='Tipo de Documento')
  fecha = models.DateField(null=True, blank=True)
  pdf = models.FileField(upload_to='documentos_induccion/', verbose_name='Cargar PDF')
      
  def ver_pdf(self):
    if self.pdf:
      return format_html('<a href="{}" target="_blank">Ver PDF</a>', self.pdf.url)
    return "No disponible"

  ver_pdf.short_description = "Visualizar PDF"

  class Meta:
    ordering = ['documento']  # Ordenar según el tipo
    verbose_name = 'Inducción del Personal'
    verbose_name_plural = 'Inducción del Personal'

  def __str__(self):
    return f"{self.get_documento_display()} - {self.legajo}"

# Modelo Período de Prueba
class Prueba(models.Model):
    legajo = models.ForeignKey(Legajo, on_delete=models.CASCADE)
    documento = models.PositiveSmallIntegerField(choices=documentos_prueba, verbose_name='Tipo de Documento')
    fecha = models.DateField(null=True, blank=True)
    pdf = models.FileField(upload_to='documentos_prueba/', verbose_name='Cargar PDF')
        
    def ver_pdf(self):
        if self.pdf:
            return format_html('<a href="{}" target="_blank">Ver PDF</a>', self.pdf.url)
        return "No disponible"
    
    ver_pdf.short_description = "Visualizar PDF"
  
    class Meta:
        ordering = ['documento']  # Ordenar según el tipo
        verbose_name = 'Período de Prueba'
        verbose_name_plural = 'Período de Prueba'
    
    def __str__(self):
        return f"{self.get_documento_display()} - {self.legajo}"
                  
# Estudios Realizados
class EstudiosRealizados(models.Model):
  legajo = models.ForeignKey(Legajo, on_delete=models.CASCADE)
  centro = models.CharField(max_length=250, blank=True, null=True, verbose_name='Centro de Estudios')
  inicio = models.DateField()
  fin = models.DateField()
  grado_instruccion = models.PositiveSmallIntegerField(choices=documentos_grado, verbose_name='Grado de Instrucción')
  especialidad = models.CharField(max_length=50, blank=True, null=True)
  fecha_expedicion = models.DateField(blank=True, null=True)
  colegiatura = models.CharField(max_length=25, blank=True, null=True)
  pdf = models.FileField(upload_to='formacion_academica/', verbose_name='Cargar PDF')

  def ver_pdf(self):
      if self.pdf:
          return format_html('<a href="{}" target="_blank">Ver PDF</a>', self.pdf.url)
      return "No disponible"
  
  ver_pdf.short_description = "Visualizar PDF"
  
  def __str__(self):
      return self.grado_instruccion
  
  class Meta:
    ordering = ['-fecha_expedicion']
    verbose_name = 'Estudio Realizado'
    verbose_name_plural = 'Estudios Realizados'

# Modelo Habilitación Profesional
class Serum(models.Model):
  legajo = models.ForeignKey(Legajo, on_delete=models.CASCADE)
  registro = models.CharField(blank=True, null=True, max_length=25, verbose_name='Número de Registro')
  fecha_emision = models.DateField(verbose_name='Fecha de Emisión')
  pdf = models.FileField(upload_to='documentos_serum/', verbose_name='Cargar PDF')
      
  def ver_pdf(self):
    if self.pdf:
      return format_html('<a href="{}" target="_blank">Ver PDF</a>', self.pdf.url)
    return "No disponible"
  
  ver_pdf.short_description = "Visualizar PDF"

  class Meta:
    ordering = ['registro', '-fecha_emision']  # Ordenar según el tipo
    verbose_name = 'SERUM'
    verbose_name_plural = 'SERUM'
  
  def __str__(self):
    return f"{self.registro()} - {self.legajo}"
  
# Especialidad-Subespecialidad
class Subespecialidad(models.Model):
  legajo = models.ForeignKey(Legajo, on_delete=models.CASCADE)
  centro = models.CharField(max_length=250, blank=True, null=True, verbose_name='Centro de Estudios')
  inicio = models.DateField()
  fin = models.DateField()
  documento = models.PositiveSmallIntegerField(choices=documentos_especialidad, verbose_name='Especialidad o Subespecialidad')
  mencion = models.CharField(max_length=50, verbose_name='Mención')
  cod_especialidad = models.CharField(max_length=50, blank=True, null=True, verbose_name='Nº de RNE')
  fecha_expedicion = models.DateField(blank=True, null=True)
  pdf = models.FileField(upload_to='formacion_especialidad/', verbose_name='Cargar PDF')

  def ver_pdf(self):
      if self.pdf:
          return format_html('<a href="{}" target="_blank">Ver PDF</a>', self.pdf.url)
      return "No disponible"
  
  ver_pdf.short_description = "Visualizar PDF"
  
  def __str__(self):
      return self.sub_especialidad
  
  class Meta:
    ordering = ['-fecha_expedicion']
    verbose_name = 'Subespecialidad'
    verbose_name_plural = 'Subespecialidad'

# Modelo Habilitación Profesional
class Habilitacion(models.Model):
  legajo = models.ForeignKey(Legajo, on_delete=models.CASCADE)
  registro = models.CharField(blank=True, null=True, max_length=25, verbose_name='Número de Registro')
  fecha_emision = models.DateField(verbose_name='Fecha de Emisión')
  fecha_vigencia = models.DateField(blank=True, null=True, verbose_name='Válido Hasta')
  pdf = models.FileField(upload_to='documentos_habilitacion/', verbose_name='Cargar PDF')
      
  def ver_pdf(self):
    if self.pdf:
      return format_html('<a href="{}" target="_blank">Ver PDF</a>', self.pdf.url)
    return "No disponible"
  
  ver_pdf.short_description = "Visualizar PDF"

  class Meta:
    ordering = ['registro', '-fecha_emision']  # Ordenar según el tipo
    verbose_name = 'Habilitación Profesional'
    verbose_name_plural = 'Habilitación Profesional'
  
  def __str__(self):
    return f"{self.registro()} - {self.legajo}"
        
# Especializaciones, Diplomados, cursos, talleres
class Curso(models.Model):
  legajo = models.ForeignKey(Legajo, on_delete=models.CASCADE)
  centro = models.CharField(max_length=250, blank=True, null=True, verbose_name='Centro de Estudios')
  documento = models.PositiveSmallIntegerField(choices=documentos_cursos, verbose_name='Tipo de Documento')
  descripcion = models.CharField(max_length=250)
  inicio = models.DateField(blank=True, null=True)
  fin = models.DateField(blank=True, null=True)
  horas = models.PositiveSmallIntegerField(blank=True, null=True)
  creditos = models.PositiveSmallIntegerField(blank=True, null=True)
  fecha_expedicion = models.DateField(blank=True, null=True)
  pdf = models.FileField(upload_to='cursos/', verbose_name='Cargar PDF')

  def ver_pdf(self):
    if self.pdf:
      return format_html('<a href="{}" target="_blank">Ver PDF</a>', self.pdf.url)
    return "No disponible"
  
  ver_pdf.short_description = "Visualizar PDF"
  
  def __str__(self):
    return self.descripcion
  
  class Meta:
    ordering = ['-fecha_expedicion']
    verbose_name = 'Especializaciones, Diplomados, Cursos, Talleres'
    verbose_name_plural = 'Especializaciones, Diplomados, Cursos, Talleres'

# Experiencia Laboral
class Experiencia(models.Model):
  legajo = models.ForeignKey(Legajo, on_delete=models.CASCADE)
  institucion = models.CharField(max_length=250, null=True, blank=True, verbose_name='Institución o Empresa')
  documento = models.PositiveSmallIntegerField(blank=True, null=True, choices=documentos_experiencia, verbose_name='Tipo de Documento')
  numero = models.CharField(blank=True, null=True, max_length=50, unique=True, verbose_name='Número')
  cargo = models.CharField(max_length=250,)
  fecha_inicio = models.DateField()
  fecha_fin = models.DateField()
  cargo2 = models.CharField(max_length=250, blank=True, null=True, verbose_name='Cargo 2')
  fecha_inicio2 = models.DateField(blank=True, null=True, verbose_name='Fecha Inicio 2')
  fecha_fin2 = models.DateField(blank=True, null=True, verbose_name='Fecha Fin 2')
  cargo3 = models.CharField(max_length=250, blank=True, null=True, verbose_name='Cargo 3')
  fecha_inicio3 = models.DateField(blank=True, null=True, verbose_name='Fecha Inicio 3')
  fecha_fin3 = models.DateField(blank=True, null=True, verbose_name='Fecha Fin 3')
  cargo4 = models.CharField(max_length=250, blank=True, null=True, verbose_name='Cargo 4')
  fecha_inicio4 = models.DateField(blank=True, null=True, verbose_name='Fecha Inicio 4')
  fecha_fin4 = models.DateField(blank=True, null=True, verbose_name='Fecha Fin 4')
  cargo5 = models.CharField(max_length=250, blank=True, null=True, verbose_name='Cargo 5')
  fecha_inicio5 = models.DateField(blank=True, null=True, verbose_name='Fecha Inicio 5')
  fecha_fin5 = models.DateField(blank=True, null=True, verbose_name='Fecha Fin 5')
  fecha_expedicion = models.DateField(blank=True, null=True)
  pdf = models.FileField(upload_to='experiencia_laboral/', verbose_name='Cargar PDF')

  def ver_pdf(self):
    if self.pdf:
      return format_html('<a href="{}" target="_blank">Ver PDF</a>', self.pdf.url)
    return "No disponible"
  
  ver_pdf.short_description = "Visualizar PDF"
  
  def __str__(self):
    return self.descripcion
  
  class Meta:
    ordering = ['-fecha_inicio']
    verbose_name = 'Experiencia Laboral'
    verbose_name_plural = 'Experiencia Laboral'

# Movimientos del Personal
class Movimientos(models.Model):
  legajo = models.ForeignKey(Legajo, on_delete=models.CASCADE)
  documento = models.CharField(max_length=50)
  tipo = models.PositiveSmallIntegerField(choices=tipo_movimientos, blank=True, null=True, verbose_name='Tipo de Licencia')
  motivo = models.CharField(max_length=50)
  asunto = models.CharField(max_length=50)
  desde = models.DateField(blank=True, null=True)
  hasta = models.DateField(blank=True, null=True)
  total_dias = models.PositiveIntegerField(blank=True, null=True, verbose_name='Total de Días')
  pdf = models.FileField(upload_to='movimientos_personal/', verbose_name='Cargar PDF')

  def save(self, *args, **kwargs):
      if self.desde and self.hasta:
          diferencia = self.hasta - self.desde
          self.total_dias = diferencia.days + 1  # Sumamos 1 para incluir el día de inicio
      elif self.desde and not self.hasta:
          self.total_dias = 1
      else:
          self.total_dias = 0
      super(Movimientos, self).save(*args, **kwargs)
  
  def ver_pdf(self):
    if self.pdf:
      return format_html('<a href="{}" target="_blank">Ver PDF</a>', self.pdf.url)
    return "No disponible"
  
  ver_pdf.short_description = "Visualizar PDF"
  
  def __str__(self):
    return self.resolucion

  class Meta:
    ordering = ['-desde']
    verbose_name = 'Movimientos del Personal'
    verbose_name_plural = 'Movimientos del Personal'
        
# Modelo de Exoneración de Retención 
class Retencion(models.Model):
  legajo = models.ForeignKey(Legajo, on_delete=models.CASCADE)
  documento = models.PositiveSmallIntegerField(choices=documentos_retencion, verbose_name='Tipo de Documento')
  fecha = models.DateTimeField(null=True, blank=True)
  pdf = models.FileField(upload_to='documentos_retencion/', verbose_name='Cargar PDF')
      
  def ver_pdf(self):
    if self.pdf:
      return format_html('<a href="{}" target="_blank">Ver PDF</a>', self.pdf.url)
    return "No disponible"
  
  ver_pdf.short_description = "Visualizar PDF"

  class Meta:
    ordering = ['documento']  # Ordenar según el tipo
    unique_together = ('legajo', 'documento')
    verbose_name = 'Exoneración de Retención'
    verbose_name_plural = 'Exoneración de Retención'
  
  def __str__(self):
    return f"{self.get_documento_display()} - {self.legajo}"
      
# Compensaciones
class Compensaciones(models.Model):
  legajo = models.ForeignKey(Legajo, on_delete=models.CASCADE)
  documento = models.PositiveSmallIntegerField(choices=documento, verbose_name='Tipo de Documento')
  numero = models.CharField(max_length=50, unique=True, verbose_name='Número')
  motivo = models.CharField(max_length=50)
  descripcion = models.CharField(max_length=250, blank=True)
  fecha = models.DateField()
  pdf = models.FileField(upload_to='compensaciones/', verbose_name='Cargar PDF')

  def ver_pdf(self):
    if self.pdf:
      return format_html('<a href="{}" target="_blank">Ver PDF</a>', self.pdf.url)
    return "No disponible"
  
  ver_pdf.short_description = "Visualizar PDF"
  
  def __str__(self):
    return self.resolucion
  
  class Meta:
    verbose_name = 'Compensación'
    verbose_name_plural = 'Compensaciones'

# Modelo de Exoneración de Retención 
class Evaluacion(models.Model):
  legajo = models.ForeignKey(Legajo, on_delete=models.CASCADE)
  periodo = models.CharField(choices=periodo_evaluacion, max_length=50)
  anio = models.CharField(max_length=4, blank=True, null=True)
  puntaje = models.PositiveSmallIntegerField(blank=True, null=True)
  pdf = models.FileField(upload_to='documentos_evaluacion/', verbose_name='Cargar PDF')
      
  def ver_pdf(self):
    if self.pdf:
      return format_html('<a href="{}" target="_blank">Ver PDF</a>', self.pdf.url)
    return "No disponible"
  
  ver_pdf.short_description = "Visualizar PDF"

  class Meta:
    ordering = ['periodo', 'anio']  # Ordenar según el tipo
    verbose_name = 'Evaluación de Desempeño'
    verbose_name_plural = 'Evaluación de Desempeño'
  
  def __str__(self):
    return f"{self.get_documento_display()} - {self.legajo}"
  
""" # Modelo de Progresión en la Carrera
class Progresion(models.Model):
  legajo = models.ForeignKey(Legajo, on_delete=models.CASCADE)
  documento = models.PositiveSmallIntegerField(choices=documento, verbose_name='Tipo de Documento')
  numero = models.CharField(max_length=100, null=True, blank=True, verbose_name='Número')
  motivo = models.CharField(max_length=300, blank=True, null=True, verbose_name='Motivo')
  descripcion = models.CharField(max_length=100, blank=True, null=True, verbose_name='Descripción')
  fecha = models.DateField(verbose_name="Fecha del Documento")
  fecha_inicio = models.DateField(null=True, blank=True, verbose_name="Fecha de Inicio")
  cargo = models.CharField(blank=True, null=True, max_length=100, choices= cargos)
  nivel = models.CharField(blank=True, null=True, max_length=100, choices= niveles)
  plaza = models.CharField(blank=True, null=True, max_length=10, verbose_name='Plaza (airhsp)')
  pdf = models.FileField(upload_to='documentos_progresion/', verbose_name='Cargar PDF')
      
  def ver_pdf(self):
    if self.pdf:
      return format_html('<a href="{}" target="_blank">Ver PDF</a>', self.pdf.url)
    return "No disponible"

  ver_pdf.short_description = "Visualizar PDF"

  class Meta:
    ordering = ['documento']  # Ordenar según el tipo
    verbose_name = 'Progresión en la Carrera'
    verbose_name_plural = 'Progresión en la Carrera'

  def __str__(self):
    return f"{self.get_documento_display()} - {self.legajo}"
  
  # Modelo de Desplazamiento
class Desplazamiento(models.Model):
  legajo = models.ForeignKey(Legajo, on_delete=models.CASCADE)
  documento = models.PositiveSmallIntegerField(choices=documento, verbose_name='Tipo de Documento')
  numero = models.CharField(max_length=50, unique=True, verbose_name='Número')
  tipo = models.PositiveSmallIntegerField(choices= tipo_desplazamiento, blank=True, null=True)
  asunto = models.CharField(max_length=100, blank=True)
  fecha = models.DateField(verbose_name="Fecha del Documento")
  fecha_inicio = models.DateField(null=True, blank=True, verbose_name="Fecha de Inicio")
  fecha_fin = models.DateField(blank=True, null=True, verbose_name='Fecha de Finalización')
  condicion_laboral = models.CharField(max_length=100, choices= condicion_laboral)
  grupo_ocupacional = models.CharField(max_length=100, choices= grupo_ocupacional)
  cargo = models.CharField(blank=True, null=True, max_length=100, choices= cargos)
  nivel = models.CharField(blank=True, null=True, max_length=100, choices= niveles)
  plaza = models.CharField(blank=True, null=True, max_length=10, verbose_name='Plaza (airhsp)')
  pdf = models.FileField(upload_to='documentos_desplazamiento/', verbose_name='Cargar PDF')

  def ver_pdf(self):
      if self.pdf:
          return format_html('<a href="{}" target="_blank">Ver PDF</a>', self.pdf.url)
      return "No disponible"
  
  ver_pdf.short_description = "Visualizar PDF"
  
  def save(self, *args, **kwargs):
      if not self.asunto and self.fecha_inicio and self.numero and self.tipo:
          # Formatear la fecha
          fecha_formateada = date_format(self.fecha_inicio, "j \d\e F \d\e Y", use_l10n=True)
          
          # Texto personalizado según el tipo
          if self.tipo == 5:
              texto_tipo = "Nombrar con resolución"
          elif self.tipo == 10:
              texto_tipo = "Rotar con resolución"
          elif self.tipo == 15:
              texto_tipo = "Destacar con resolución"
          elif self.tipo == 20:
              texto_tipo = "Encargar con resolución"
          else:
              texto_tipo = "Sin tipo definido"  # Caso por defecto

          # Concatenar asunto
          self.asunto = f"{texto_tipo} {self.numero}, a partir del {fecha_formateada}"
      super().save(*args, **kwargs)

  def __str__(self):
      return self.asunto
  
  class Meta:
    ordering = ['-fecha']
    verbose_name = 'Desplazamiento'
    verbose_name_plural = 'Desplazamiento' """
    
# Modelo de Reconocimientos y Sanciones
class Reconocimiento(models.Model):
  legajo = models.ForeignKey(Legajo, on_delete=models.CASCADE)
  documento_reconocimiento = models.PositiveSmallIntegerField(choices=documentos_reconocimientos, verbose_name='Reconocimientos y Sanciones')
  documento = models.PositiveSmallIntegerField(choices=documento, verbose_name='Tipo de Documento')
  numero = models.CharField(blank=True, null=True, max_length=50, verbose_name='Número')
  descripcion = models.CharField(max_length=250, blank=True, null=True)
  fecha = models.DateField(blank=True, null=True, verbose_name='Fecha del Documento')
  desde = models.DateField(blank=True, null=True, verbose_name='Fecha de Inicio')
  hasta = models.DateField(blank=True, null=True, verbose_name='Fecha de Finalización')
  total_dias = models.PositiveIntegerField(blank=True, null=True, verbose_name='Total de Días')
  pdf = models.FileField(upload_to='documentos_reconocimiento/', verbose_name='Cargar PDF')
      
  def ver_pdf(self):
    if self.pdf:
      return format_html('<a href="{}" target="_blank">Ver PDF</a>', self.pdf.url)
    return "No disponible"
  
  ver_pdf.short_description = "Visualizar PDF"

  class Meta:
    ordering = ['documento']  # Ordenar según el tipo
    verbose_name = 'Reconocimientos y Sanciones'
    verbose_name_plural = 'Reconocimientos y Sanciones'
  
  def __str__(self):
    return f"{self.get_documento_display()} - {self.legajo}"

# Modelo de Relaciones individuales y colectivas
class Laboral(models.Model):
  legajo = models.ForeignKey(Legajo, on_delete=models.CASCADE)
  documento = models.CharField(max_length=250, blank=True, null=True, verbose_name='Tipo de Documento')
  documento_laboral = models.PositiveSmallIntegerField(choices=documentos_laboral, verbose_name='Relaciones Laborales')
  descripcion = models.CharField(max_length=250, blank=True, null=True)
  fecha = models.DateField(blank=True, null=True)
  pdf = models.FileField(upload_to='documentos_laboral/', verbose_name='Cargar PDF')
  fecha_carga = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Carga')
      
  def ver_pdf(self):
    if self.pdf:
      return format_html('<a href="{}" target="_blank">Ver PDF</a>', self.pdf.url)
    return "No disponible"
  
  ver_pdf.short_description = "Visualizar PDF"

  class Meta:
    ordering = ['documento']  # Ordenar según el tipo
    verbose_name = 'Relaciones Laborales'
    verbose_name_plural = 'Relaciones Laborales'
  
  def __str__(self):
    return f"{self.get_documento_display()} - {self.legajo}"

# Modelo de Relaciones individuales y colectivas
class Seguridad(models.Model):
  legajo = models.ForeignKey(Legajo, on_delete=models.CASCADE)
  documento = models.PositiveSmallIntegerField(choices=documentos_sst, verbose_name='Tipo de Documento')
  descripcion = models.CharField(max_length=250, blank=True, null=True)
  fecha = models.DateField(blank=True, null=True, verbose_name='Fecha del Documento')
  fecha_inicio = models.DateField(blank=True, null=True, verbose_name='Fecha de Inicio')
  fecha_fin = models.DateField(blank=True, null=True, verbose_name='Fecha de Finalización')
  total_dias = models.PositiveIntegerField(blank=True, null=True, verbose_name='Total de Días')
  pdf = models.FileField(upload_to='documentos_sst/', verbose_name='Cargar PDF')
      
  def ver_pdf(self):
    if self.pdf:
      return format_html('<a href="{}" target="_blank">Ver PDF</a>', self.pdf.url)
    return "No disponible"
  
  ver_pdf.short_description = "Visualizar PDF"

  class Meta:
    ordering = ['documento']  # Ordenar según el tipo
    verbose_name = 'SST y Bienestar social'
    verbose_name_plural = 'SST y Bienestar social'
  
  def __str__(self):
    return f"{self.get_documento_display()} - {self.legajo}"
  
  # Modelo de Desvinculación
class Desvinculacion(models.Model):
  legajo = models.ForeignKey(Legajo, on_delete=models.CASCADE)
  documento = models.PositiveSmallIntegerField(choices=documentos_desvinculacion, verbose_name='Desvinculación')
  descripcion = models.CharField(max_length=250, blank=True, null=True)
  fecha = models.DateField(blank=True, null=True)
  pdf = models.FileField(upload_to='documentos_desvinculacion/', verbose_name='Cargar PDF')
      
  def ver_pdf(self):
    if self.pdf:
      return format_html('<a href="{}" target="_blank">Ver PDF</a>', self.pdf.url)
    return "No disponible"
  
  ver_pdf.short_description = "Visualizar PDF"

  class Meta:
    ordering = ['documento']  # Ordenar según el tipo
    verbose_name = 'Desvinculación'
    verbose_name_plural = 'Desvinculación'
  
  def __str__(self):
    return f"{self.get_documento_display()} - {self.legajo}"
  

"""# Modelo de Finalización de Vinculo laboral
class Final(models.Model):
  legajo = models.ManyToManyField(Legajo)
  documento = models.PositiveSmallIntegerField(choices=documento, verbose_name='Tipo de Documento')
  numero = models.CharField(max_length=50, unique=True, verbose_name='Número')
  descripcion = models.CharField(max_length=100, blank=True)
  fecha = models.DateField(verbose_name='Fecha del Documento')
  fecha_fin = models.DateField(blank=True, null=True, verbose_name='Fecha de Finalización')
  condicion_laboral = models.CharField(max_length=100, choices= condicion_laboral)
  grupo_ocupacional = models.CharField(max_length=100, choices= grupo_ocupacional)
  cargo = models.CharField(blank=True, null=True, max_length=100, choices= cargos)
  nivel = models.CharField(blank=True, null=True, max_length=100, choices= niveles)
  plaza = models.CharField(blank=True, null=True, max_length=10)
  pdf = models.FileField(upload_to='documentos_final/', verbose_name='Cargar PDF')

  def ver_pdf(self):
      if self.pdf:
          return format_html('<a href="{}" target="_blank">Ver PDF</a>', self.pdf.url)
      return "No disponible"
  
  ver_pdf.short_description = "Visualizar PDF"

  def __str__(self):
      return self.descripcion
  
  class Meta:
    ordering = ['-fecha']
    verbose_name = 'Resolución de Finalización de Vínculo'
    verbose_name_plural = 'Resolución de Finalización de Vínculo' """
    
# Modelo de Otros Documentos
class Otro(models.Model):
  legajo = models.ForeignKey(Legajo, on_delete=models.CASCADE)
  documento = models.CharField(max_length=250)
  descripcion = models.CharField(max_length=500, blank=True, null=True)
  fecha = models.DateField(blank=True, null=True)
  pdf = models.FileField(upload_to='documentos_desvinculacion/', verbose_name='Cargar PDF')
      
  def ver_pdf(self):
    if self.pdf:
      return format_html('<a href="{}" target="_blank">Ver PDF</a>', self.pdf.url)
    return "No disponible"
  
  ver_pdf.short_description = "Visualizar PDF"

  class Meta:
    ordering = ['documento']  # Ordenar según el tipo
    verbose_name = 'Otro Documento'
    verbose_name_plural = 'Otros Documentos'
  
  def __str__(self):
    return f"{self.get_documento_display()} - {self.legajo}"