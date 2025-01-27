from django.db import models
from django.utils.html import format_html
from .choices import estados, sexo, departamento, tipo, documento, modalidad, documentos_informacion, documentos_seleccion, documentos_induccion, documentos_prueba, documentos_colegiatura, documentos_cursos, documentos_experiencia, documentos_retencion, documentos_evaluacion, tipo_desplazamiento, documentos_reconocimientos, documentos_laboral, documentos_sst, documentos_desvinculacion
from django.core.exceptions import ValidationError
from django.utils.formats import date_format
            
# Modelos de tablas complementarias

class Cargo(models.Model):
    denominacion = models.CharField(max_length=100)

    def __str__(self):
        return self.denominacion

class Nivel(models.Model):
    denominacion = models.CharField(max_length=4)

    def __str__(self):
        return self.denominacion

class Plaza(models.Model):
    denominacion = models.CharField(max_length=30)

    def __str__(self):
        return self.denominacion
    
# Modelo principal
class DatosPersonales(models.Model):
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    nombres = models.CharField(max_length=50)
    dni = models.CharField(max_length=8, blank=True, null=True, unique=True)
    carnet_extranjeria = models.CharField(max_length=15, blank=True, null=True, unique=True)
    sexo = models.CharField(max_length=1, choices= sexo, blank=True, null=True)
    estado_civil = models.CharField(max_length=10, choices= estados, blank=True, null=True)
    telefono = models.CharField(max_length=12, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    modalidad = models.CharField(max_length=25, choices= modalidad, blank=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    departamento = models.CharField(max_length=50, choices= departamento, blank=True, null=True)
    provincia = models.CharField(max_length=50, blank=True, null=True)
    distrito = models.CharField(max_length=50, blank=True, null=True)
    domicilio = models.CharField(max_length=100, blank=True, null=True)
    cipss = models.CharField(max_length=12, blank=True, null=True)
     
    def clean(self):     
        # Validar que al menos un documento de identidad esté presente
        if not self.dni and not self.carnet_extranjeria:
            raise ValidationError("Debe proporcionar un DNI o un Carnet de Extranjería.")

    def __str__(self):
        return f"{self.apellido_paterno} {self.apellido_materno}, {self.nombres}"
    
    class Meta:
        ordering = ['apellido_paterno']
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

# Modelo Información Personal
class InfoPersonal(models.Model):
    empleado = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    tipo_documento = models.PositiveSmallIntegerField(choices=documentos_informacion, verbose_name='Tipo de Documento')
    pdf = models.FileField(upload_to='documentos_personales/', verbose_name='Cargar PDF')
    fecha_carga = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Carga')
        
    def ver_pdf(self):
        if self.pdf:
            return format_html('<a href="{}" target="_blank">Ver PDF</a>', self.pdf.url)
        return "No disponible"
    
    ver_pdf.short_description = "Visualizar PDF"
  
    class Meta:
        ordering = ['tipo_documento']  # Ordenar según el tipo
        unique_together = ('empleado', 'tipo_documento')
        verbose_name = 'Información Personal'
        verbose_name_plural = 'Información Personal'
    
    def __str__(self):
        return f"{self.get_tipo_documento_display()} - {self.empleado}"
      
# Modelo Proceso de Selección
class Seleccion(models.Model):
    empleado = models.ManyToManyField(DatosPersonales)
    tipo_documento = models.PositiveSmallIntegerField(choices=documentos_seleccion, verbose_name='Tipo de Documento')
    descripcion = models.CharField(max_length=250, blank=True, verbose_name='Descripción')
    pdf = models.FileField(upload_to='documentos_seleccion/', verbose_name='Cargar PDF')
    fecha_carga = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Carga')
        
    def ver_pdf(self):
        if self.pdf:
            return format_html('<a href="{}" target="_blank">Ver PDF</a>', self.pdf.url)
        return "No disponible"
    
    ver_pdf.short_description = "Visualizar PDF"
  
    class Meta:
        ordering = ['tipo_documento']  # Ordenar según el tipo
        verbose_name = 'Proceso de Selección'
        verbose_name_plural = 'Proceso de Selección'
    
    def __str__(self):
        return f"{self.get_tipo_documento_display()} - {self.empleado}"
      
# Modelo de Vinculo laboral
class Vinculo(models.Model):
  empleado = models.ManyToManyField(DatosPersonales)
  documento = models.PositiveSmallIntegerField(choices=documento, verbose_name='Tipo de Documento')
  numero = models.CharField(max_length=50, unique=True, verbose_name='Número')
  tipo = models.CharField(max_length=15, choices= tipo, blank=True, null=True)
  asunto = models.CharField(max_length=100, blank=True)
  fecha = models.DateField()
  fecha_vigencia = models.DateField()
  fecha_fin = models.DateField(blank=True, null=True)
  cargo = models.ManyToManyField(Cargo, blank=True)
  nivel = models.ManyToManyField(Nivel, blank=True)
  plaza = models.ManyToManyField(Plaza, blank=True)
  pdf = models.FileField(upload_to='documentos_vinculo/', verbose_name='Cargar PDF')

  def ver_pdf(self):
      if self.pdf:
          return format_html('<a href="{}" target="_blank">Ver PDF</a>', self.pdf.url)
      return "No disponible"
  
  ver_pdf.short_description = "Visualizar PDF"
  
  def save(self, *args, **kwargs):
      if not self.asunto and self.fecha_vigencia and self.numero and self.tipo:
          # Formatear la fecha
          fecha_formateada = date_format(self.fecha_vigencia, "j \d\e F \d\e Y", use_l10n=True)
          
          # Texto personalizado según el tipo
          if self.tipo == 'Nombramiento':
              texto_tipo = "Nombrar con resolución"
          elif self.tipo == 'Reasignacion':
              texto_tipo = "Reasignar con resolución"
          elif self.tipo == 'Ascenso':
              texto_tipo = "Ascender con resolución"
          elif self.tipo == 'Cese':
              texto_tipo = "Cesar con resolución"
          else:
              texto_tipo = "Sin tipo definido"  # Caso por defecto

          # Concatenar asunto
          self.asunto = f"{texto_tipo} {self.numero}, a partir del {fecha_formateada}"
      super().save(*args, **kwargs)

  def __str__(self):
      return self.asunto
  
  class Meta:
    ordering = ['-fecha']
    verbose_name = 'Formalización de Vínculo'
    verbose_name_plural = 'Formalización de Vínculo'

# Modelo Inducción del Personal
class Induccion(models.Model):
  empleado = models.ManyToManyField(DatosPersonales)
  tipo_documento = models.PositiveSmallIntegerField(choices=documentos_induccion, verbose_name='Tipo de Documento')
  pdf = models.FileField(upload_to='documentos_induccion/', verbose_name='Cargar PDF')
  fecha_carga = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Carga')
      
  def ver_pdf(self):
    if self.pdf:
      return format_html('<a href="{}" target="_blank">Ver PDF</a>', self.pdf.url)
    return "No disponible"

  ver_pdf.short_description = "Visualizar PDF"

  class Meta:
    ordering = ['tipo_documento']  # Ordenar según el tipo
    verbose_name = 'Inducción del Personal'
    verbose_name_plural = 'Inducción del Personal'

  def __str__(self):
    return f"{self.get_tipo_documento_display()} - {self.empleado}"

# Modelo Período de Prueba
class Prueba(models.Model):
    empleado = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    tipo_documento = models.PositiveSmallIntegerField(choices=documentos_prueba, verbose_name='Tipo de Documento')
    pdf = models.FileField(upload_to='documentos_prueba/', verbose_name='Cargar PDF')
    fecha_carga = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Carga')
        
    def ver_pdf(self):
        if self.pdf:
            return format_html('<a href="{}" target="_blank">Ver PDF</a>', self.pdf.url)
        return "No disponible"
    
    ver_pdf.short_description = "Visualizar PDF"
  
    class Meta:
        ordering = ['tipo_documento']  # Ordenar según el tipo
        unique_together = ('empleado', 'tipo_documento')
        verbose_name = 'Período de Prueba'
        verbose_name_plural = 'Período de Prueba'
    
    def __str__(self):
        return f"{self.get_tipo_documento_display()} - {self.empleado}"

# Modelo Colegiatura y Habilitación Profesional
class Colegiatura(models.Model):
  empleado = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
  tipo_documento = models.PositiveSmallIntegerField(choices=documentos_colegiatura, verbose_name='Tipo de Documento')
  fecha_emision = models.DateField()
  pdf = models.FileField(upload_to='documentos_colegiatura/', verbose_name='Cargar PDF')
  fecha_carga = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Carga')
      
  def ver_pdf(self):
    if self.pdf:
      return format_html('<a href="{}" target="_blank">Ver PDF</a>', self.pdf.url)
    return "No disponible"
  
  ver_pdf.short_description = "Visualizar PDF"

  class Meta:
    ordering = ['tipo_documento', '-fecha_emision']  # Ordenar según el tipo
    verbose_name = 'Colegiatura'
    verbose_name_plural = 'Colegiatura'
  
  def __str__(self):
    return f"{self.get_tipo_documento_display()} - {self.empleado}"
                  
# Estudios Realizados
class EstudiosRealizados(models.Model):
  empleado = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
  inicio = models.DateField()
  fin = models.DateField()
  grado_instruccion = models.CharField(max_length=50)
  especialidad = models.CharField(max_length=50)
  sub_especialidad = models.CharField(max_length=50, blank=True, null=True)
  cod_especialidad = models.CharField(max_length=50, blank=True, null=True, verbose_name='Nº de RNE')
  fecha_expedicion = models.DateField(blank=True, null=True)
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
        
# Especializaciones, Diplomados, cursos, talleres
class Curso(models.Model):
  empleado = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
  tipo_documento = models.PositiveSmallIntegerField(choices=documentos_cursos, verbose_name='Tipo de Documento')
  descripcion = models.CharField(max_length=250)
  inicio = models.DateField()
  fin = models.DateField()
  duracion_horas = models.IntegerField(blank=True, null=True)
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
  empleado = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
  tipo_documento = models.PositiveSmallIntegerField(blank=True, null=True, choices=documentos_experiencia, verbose_name='Tipo de Documento')
  descripcion = models.CharField(max_length=250)
  inicio = models.DateField()
  fin = models.DateField()
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
    ordering = ['-inicio']
    verbose_name = 'Experiencia Laboral'
    verbose_name_plural = 'Experiencia Laboral'

# Movimientos del Personal
class Movimientos(models.Model):
  empleado = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
  resolucion = models.CharField(max_length=50, unique=True)
  motivo = models.CharField(max_length=50)
  asunto = models.CharField(max_length=50)
  desde = models.DateField()
  hasta = models.DateField()
  pdf = models.FileField(upload_to='movimientos_personal/', verbose_name='Cargar PDF')

  def ver_pdf(self):
    if self.pdf:
      return format_html('<a href="{}" target="_blank">Ver PDF</a>', self.pdf.url)
    return "No disponible"
  
  ver_pdf.short_description = "Visualizar PDF"
  
  def __str__(self):
    return self.resolucion

  class Meta:
    verbose_name = 'Movimientos del Personal'
    verbose_name_plural = 'Movimientos del Personal'
        
# Modelo de Exoneración de Retención 
class Retencion(models.Model):
  empleado = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
  tipo_documento = models.PositiveSmallIntegerField(choices=documentos_retencion, verbose_name='Tipo de Documento')
  pdf = models.FileField(upload_to='documentos_retencion/', verbose_name='Cargar PDF')
  fecha_carga = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Carga')
      
  def ver_pdf(self):
    if self.pdf:
      return format_html('<a href="{}" target="_blank">Ver PDF</a>', self.pdf.url)
    return "No disponible"
  
  ver_pdf.short_description = "Visualizar PDF"

  class Meta:
    ordering = ['tipo_documento']  # Ordenar según el tipo
    unique_together = ('empleado', 'tipo_documento')
    verbose_name = 'Exoneración de Retención'
    verbose_name_plural = 'Exoneración de Retención'
  
  def __str__(self):
    return f"{self.get_tipo_documento_display()} - {self.empleado}"
      
# Compensaciones
class Compensaciones(models.Model):
  empleado = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
  resolucion = models.CharField(max_length=50, unique=True)
  fecha = models.DateField()
  motivo = models.CharField(max_length=100)
  porcentaje = models.DecimalField(max_digits=5, decimal_places=2)
  anios = models.IntegerField(verbose_name='años')
  meses = models.IntegerField()
  dias = models.IntegerField()
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
  empleado = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
  tipo_documento = models.PositiveSmallIntegerField(choices=documentos_evaluacion, verbose_name='Tipo de Documento')
  pdf = models.FileField(upload_to='documentos_evaluacion/', verbose_name='Cargar PDF')
  fecha_carga = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Carga')
      
  def ver_pdf(self):
    if self.pdf:
      return format_html('<a href="{}" target="_blank">Ver PDF</a>', self.pdf.url)
    return "No disponible"
  
  ver_pdf.short_description = "Visualizar PDF"

  class Meta:
    ordering = ['tipo_documento']  # Ordenar según el tipo
    verbose_name = 'Evaluación de Desempeño'
    verbose_name_plural = 'Evaluación de Desempeño'
  
  def __str__(self):
    return f"{self.get_tipo_documento_display()} - {self.empleado}"
  
  # Modelo de Progresión en la Carrera
class Progresion(models.Model):
  empleado = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
  tipo_documento = models.PositiveSmallIntegerField(choices=documento, verbose_name='Tipo de Documento')
  fecha = models.DateField(blank=True, null=True)
  nivel = models.ManyToManyField(Nivel, blank=True)
  pdf = models.FileField(upload_to='documentos_progresion/', verbose_name='Cargar PDF')
  fecha_carga = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Carga')
      
  def ver_pdf(self):
    if self.pdf:
      return format_html('<a href="{}" target="_blank">Ver PDF</a>', self.pdf.url)
    return "No disponible"

  ver_pdf.short_description = "Visualizar PDF"

  class Meta:
    ordering = ['tipo_documento']  # Ordenar según el tipo
    verbose_name = 'Progresión en la Carrera'
    verbose_name_plural = 'Progresión en la Carrera'

  def __str__(self):
    return f"{self.get_tipo_documento_display()} - {self.empleado}"
  
  # Modelo de Desplazamiento
class Desplazamiento(models.Model):
  empleado = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
  documento = models.PositiveSmallIntegerField(choices=documento, verbose_name='Tipo de Documento')
  numero = models.CharField(max_length=50, unique=True, verbose_name='Número')
  tipo = models.PositiveSmallIntegerField(choices= tipo_desplazamiento, blank=True, null=True)
  asunto = models.CharField(max_length=100, blank=True)
  fecha = models.DateField()
  fecha_vigencia = models.DateField()
  cargo = models.ManyToManyField(Cargo, blank=True)
  nivel = models.ManyToManyField(Nivel, blank=True)
  plaza = models.ManyToManyField(Plaza, blank=True)
  pdf = models.FileField(upload_to='documentos_desplazamiento/', verbose_name='Cargar PDF')

  def ver_pdf(self):
      if self.pdf:
          return format_html('<a href="{}" target="_blank">Ver PDF</a>', self.pdf.url)
      return "No disponible"
  
  ver_pdf.short_description = "Visualizar PDF"
  
  def save(self, *args, **kwargs):
      if not self.asunto and self.fecha_vigencia and self.numero and self.tipo:
          # Formatear la fecha
          fecha_formateada = date_format(self.fecha_vigencia, "j \d\e F \d\e Y", use_l10n=True)
          
          # Texto personalizado según el tipo
          if self.tipo == 5:
              texto_tipo = "Nombrar con resolución Nº"
          elif self.tipo == 10:
              texto_tipo = "Rotar con resolución Nº"
          elif self.tipo == 15:
              texto_tipo = "Destacar con resolución Nº"
          elif self.tipo == 20:
              texto_tipo = "Encargar con resolución Nº"
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
    verbose_name_plural = 'Desplazamiento'
    
# Modelo de Reconocimientos y Sanciones
class Reconocimiento(models.Model):
  empleado = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
  tipo_documento = models.PositiveSmallIntegerField(choices=documentos_reconocimientos, verbose_name='Reconocimientos y Sanciones')
  documento = models.PositiveSmallIntegerField(choices=documento, verbose_name='Tipo de Documento')
  descripcion = models.CharField(max_length=250, blank=True, null=True)
  fecha = models.DateField(blank=True, null=True)
  pdf = models.FileField(upload_to='documentos_reconocimiento/', verbose_name='Cargar PDF')
  fecha_carga = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Carga')
      
  def ver_pdf(self):
    if self.pdf:
      return format_html('<a href="{}" target="_blank">Ver PDF</a>', self.pdf.url)
    return "No disponible"
  
  ver_pdf.short_description = "Visualizar PDF"

  class Meta:
    ordering = ['tipo_documento']  # Ordenar según el tipo
    verbose_name = 'Reconocimientos y Sanciones'
    verbose_name_plural = 'Reconocimientos y Sanciones'
  
  def __str__(self):
    return f"{self.get_tipo_documento_display()} - {self.empleado}"

# Modelo de Relaciones individuales y colectivas
class Laboral(models.Model):
  empleado = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
  tipo_documento = models.PositiveSmallIntegerField(choices=documentos_laboral, verbose_name='Relaciones Laborales')
  documento = models.PositiveSmallIntegerField(choices=documento, verbose_name='Tipo de Documento')
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
    ordering = ['tipo_documento']  # Ordenar según el tipo
    verbose_name = 'Relaciones Laborales'
    verbose_name_plural = 'Relaciones Laborales'
  
  def __str__(self):
    return f"{self.get_tipo_documento_display()} - {self.empleado}"

# Modelo de Relaciones individuales y colectivas
class Seguridad(models.Model):
  empleado = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
  tipo_documento = models.PositiveSmallIntegerField(choices=documentos_sst, verbose_name='SST y Bienestar social')
  descripcion = models.CharField(max_length=250, blank=True, null=True)
  fecha = models.DateField(blank=True, null=True)
  pdf = models.FileField(upload_to='documentos_sst/', verbose_name='Cargar PDF')
  fecha_carga = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Carga')
      
  def ver_pdf(self):
    if self.pdf:
      return format_html('<a href="{}" target="_blank">Ver PDF</a>', self.pdf.url)
    return "No disponible"
  
  ver_pdf.short_description = "Visualizar PDF"

  class Meta:
    ordering = ['tipo_documento']  # Ordenar según el tipo
    verbose_name = 'SST y Bienestar social'
    verbose_name_plural = 'SST y Bienestar social'
  
  def __str__(self):
    return f"{self.get_tipo_documento_display()} - {self.empleado}"
  
  # Modelo de Desvinculación
class Desvinculacion(models.Model):
  empleado = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
  tipo_documento = models.PositiveSmallIntegerField(choices=documentos_desvinculacion, verbose_name='Desvinculación')
  descripcion = models.CharField(max_length=250, blank=True, null=True)
  fecha = models.DateField(blank=True, null=True)
  pdf = models.FileField(upload_to='documentos_desvinculacion/', verbose_name='Cargar PDF')
  fecha_carga = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Carga')
      
  def ver_pdf(self):
    if self.pdf:
      return format_html('<a href="{}" target="_blank">Ver PDF</a>', self.pdf.url)
    return "No disponible"
  
  ver_pdf.short_description = "Visualizar PDF"

  class Meta:
    ordering = ['tipo_documento']  # Ordenar según el tipo
    verbose_name = 'Desvinculación'
    verbose_name_plural = 'Desvinculación'
  
  def __str__(self):
    return f"{self.get_tipo_documento_display()} - {self.empleado}"