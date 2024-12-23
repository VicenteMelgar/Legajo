from django.db import models
from django.utils.html import format_html
from .choices import estados, sexo, departamento, tipo, dependencia, documento, modalidad
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

# Modelo relacionado con PDFs
class ServiciosPrestados(models.Model):
    empleado = models.ManyToManyField(DatosPersonales)
    documento = models.CharField(max_length=25, choices= documento, blank=True, null=True)
    numero = models.CharField(max_length=50, unique=True, verbose_name='Número')
    tipo = models.CharField(max_length=15, choices= tipo, blank=True, null=True)
    asunto = models.CharField(max_length=100, blank=True)
    fecha= models.DateField()
    fecha_vigencia = models.DateField()
    dependencia = models.CharField(max_length=30, choices= dependencia, blank=True, null=True)
    cargo = models.ManyToManyField(Cargo, blank=True)
    nivel = models.ManyToManyField(Nivel, blank=True)
    plaza = models.ManyToManyField(Plaza, blank=True)
    pdf = models.FileField(upload_to='servicios_prestados/', verbose_name='Cargar PDF')

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
        verbose_name = 'Servicio Prestado'
        verbose_name_plural = 'Servicios Prestados'

# Programa
class Programa(models.Model):
    empleado = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    denominacion = models.CharField(max_length=100)
    codfun = models.CharField(max_length=4)
    codpro = models.CharField(max_length=4)
    codsub = models.CharField(max_length=4)
    codact = models.CharField(max_length=4)
    codcom = models.CharField(max_length=4)
    codmet = models.CharField(max_length=4)

    def __str__(self):
        return self.denominacion

# Ausencias, Méritos y Deméritos
class AusenciasMeritosDemeritos(models.Model):
    empleado = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    resolucion = models.CharField(max_length=50, unique=True)
    motivo = models.CharField(max_length=50)
    asunto = models.CharField(max_length=50)
    desde = models.DateField()
    hasta = models.DateField()
    pdf = models.FileField(upload_to='ausencias_meritos_demeritos/', verbose_name='Cargar PDF')

    def ver_pdf(self):
        if self.pdf:
            return format_html('<a href="{}" target="_blank">Ver PDF</a>', self.pdf.url)
        return "No disponible"
    
    ver_pdf.short_description = "Visualizar PDF"
    
    def __str__(self):
        return self.resolucion

    class Meta:
        verbose_name = 'Ausencias, Méritos y Deméritos'
        verbose_name_plural = 'Ausencias, Méritos y Deméritos'
        
# Bonificación Personal
class BonificacionPersonal(models.Model):
    empleado = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    resolucion = models.CharField(max_length=50, unique=True)
    fecha = models.DateField()
    motivo = models.CharField(max_length=100)
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)
    anios = models.IntegerField(verbose_name='años')
    meses = models.IntegerField()
    dias = models.IntegerField()
    pdf = models.FileField(upload_to='bonificacion_personal/', verbose_name='Cargar PDF')

    def ver_pdf(self):
        if self.pdf:
            return format_html('<a href="{}" target="_blank">Ver PDF</a>', self.pdf.url)
        return "No disponible"
    
    ver_pdf.short_description = "Visualizar PDF"
    
    def __str__(self):
        return self.resolucion
    
    class Meta:
        verbose_name = 'Bonificación Personal'
        verbose_name_plural = 'Bonificación Personal'

# Tiempo de Servicios
class TiempodeServicios(models.Model):
    empleado = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    resolucion = models.CharField(max_length=50, unique=True)
    desde = models.DateField()
    hasta = models.DateField()
    anios = models.IntegerField(verbose_name='años')
    meses = models.IntegerField()
    dias = models.IntegerField()
    pdf = models.FileField(upload_to='tiempo_de_servicios/', verbose_name='Cargar PDF')
    
    def ver_pdf(self):
        if self.pdf:
            return format_html('<a href="{}" target="_blank">Ver PDF</a>', self.pdf.url)
        return "No disponible"
    
    ver_pdf.short_description = "Visualizar PDF"

    def __str__(self):
        return self.resolucion
    
    class Meta:
        verbose_name = 'Tiempo de Servicio'
        verbose_name_plural = 'Tiempo de Servicio'

# Pensionista Sobreviviente
class PensionistaSobreviviente(models.Model):
    empleado = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    resolucion = models.CharField(max_length=25, unique=True)
    fecha = models.DateField()
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    nombres = models.CharField(max_length=50)
    dni = models.CharField(max_length=8)
    pdf = models.FileField(upload_to='pensionista_sobreviviente/', verbose_name='Cargar PDF')
    
    def ver_pdf(self):
        if self.pdf:
            return format_html('<a href="{}" target="_blank">Ver PDF</a>', self.pdf.url)
        return "No disponible"
    
    ver_pdf.short_description = "Visualizar PDF"

    def __str__(self):
        return self.resolucion
    
    class Meta:
        verbose_name = 'Pensionista sobreviviente'
        verbose_name_plural = 'Pensionista Sobreviviente'
    
# Estudios Realizados
class EstudiosRealizados(models.Model):
    empleado = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    inicio = models.DateField()
    fin = models.DateField()
    grado_instruccion = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50)
    sub_especialidad = models.CharField(max_length=50, blank=True, null=True)
    cod_especialidad = models.CharField(max_length=50, blank=True, null=True)
    fecha_expedicion = models.DateField()
    pdf = models.FileField(upload_to='estudios_realizados/', verbose_name='Cargar PDF')

    def ver_pdf(self):
        if self.pdf:
            return format_html('<a href="{}" target="_blank">Ver PDF</a>', self.pdf.url)
        return "No disponible"
    
    ver_pdf.short_description = "Visualizar PDF"
    
    def __str__(self):
        return self.grado_instruccion
    
    class Meta:
        verbose_name = 'Estudio Realizado'
        verbose_name_plural = 'Estudios Realizados'