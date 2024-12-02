from django.db import models
from django.utils.html import format_html
from .choices import estados, sexo, departamento, tipo
from django.core.exceptions import ValidationError
from django.utils.formats import date_format

# Modelo principal
class DatosPersonales(models.Model):
    apellido_paterno = models.CharField(max_length=25)
    apellido_materno = models.CharField(max_length=25)
    nombres = models.CharField(max_length=20)
    dni = models.CharField(max_length=8, blank=True, null=True, unique=True)
    carnet_extranjeria = models.CharField(max_length=15, blank=True, null=True, unique=True)
    sexo = models.CharField(max_length=1, choices= sexo, blank=True, null=True)
    estado_civil = models.CharField(max_length=10, choices= estados, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    departamento = models.CharField(max_length=25, choices= departamento, blank=True, null=True)
    provincia = models.CharField(max_length=25, blank=True, null=True)
    distrito = models.CharField(max_length=25, blank=True, null=True)
    domicilio = models.CharField(max_length=100, blank=True, null=True)
    cipss = models.CharField(max_length=12, blank=True, null=True)
    
    def clean(self):     
        # Validar que al menos un documento de identidad esté presente
        if not self.dni and not self.carnet_extranjeria:
            raise ValidationError("Debe proporcionar un DNI o un Carnet de Extranjería.")

    def __str__(self):
        return f"{self.apellido_paterno} {self.apellido_materno}, {self.nombres}"
    
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'


# Modelo relacionado con PDFs
class ServiciosPrestados(models.Model):
    empleado = models.ManyToManyField(DatosPersonales)
    resolucion = models.CharField(max_length=50, unique=True, default='R.D. Nº xxx HHV/2024-OP')
    tipo = models.CharField(max_length=15, choices= tipo, blank=True, null=True)
    fecha= models.DateField()
    fecha_vigencia = models.DateField()
    asunto = models.CharField(max_length=100, blank=True)
    pdf = models.FileField(upload_to='servicios_prestados/', verbose_name='Cargar PDF')

    def ver_pdf(self):
        if self.pdf:
            return format_html('<a href="{}" target="_blank">Ver PDF</a>', self.pdf.url)
        return "No disponible"
    
    ver_pdf.short_description = "Visualizar PDF"
    
    def save(self, *args, **kwargs):
        if not self.asunto and self.fecha_vigencia and self.resolucion and self.tipo:
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
            self.asunto = f"{texto_tipo} {self.resolucion}, a partir del {fecha_formateada}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.resolucion
    
    class Meta:
        verbose_name = 'Servicio Prestado'
        verbose_name_plural = 'Servicios Prestados'

# Programa
class Programa(models.Model):
    trabajador = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
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
    trabajador = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    resolucion = models.CharField(max_length=50, unique=True)
    motivo = models.TextField()
    asunto = models.TextField()
    desde = models.DateField()
    hasta = models.DateField()
    pdfamd = models.FileField(upload_to='ausencias_meritos_demeritos/')

    def __str__(self):
        return self.resolucion

# Bonificación Personal
class BonificacionPersonal(models.Model):
    trabajador = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    resolucion = models.CharField(max_length=50, unique=True)
    fecha = models.DateField()
    motivo = models.TextField()
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)
    años = models.IntegerField()
    meses = models.IntegerField()
    dias = models.IntegerField()
    pdfbp = models.FileField(upload_to='bonificacion_personal/')

    def __str__(self):
        return self.resolucion

# Tiempo de Servicios
class TiempodeServicios(models.Model):
    trabajador = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    resolucion = models.CharField(max_length=50, unique=True)
    desde = models.DateField()
    hasta = models.DateField()
    años = models.IntegerField()
    meses = models.IntegerField()
    dias = models.IntegerField()
    pdfts = models.FileField(upload_to='tiempo_de_servicios/')

    def __str__(self):
        return self.resolucion

# Pensionista Sobreviviente
class PensionistaSobreviviente(models.Model):
    empleado = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    resolucion = models.CharField(max_length=15, unique=True)
    fecha = models.DateField()
    apellido_paterno = models.CharField(max_length=25)
    apellido_materno = models.CharField(max_length=25)
    nombres = models.CharField(max_length=50)
    dni = models.CharField(max_length=8)
    pdfps = models.FileField(upload_to='pensionista_sobreviviente/', verbose_name='Cargar PDF')
    
    def ver_pdf(self):
        if self.pdfps:
            return format_html('<a href="{}" target="_blank">Ver PDF</a>', self.pdfps.url)
        return "No disponible"
    
    ver_pdf.short_description = "Visualizar PDF"

    def __str__(self):
        return self.resolucion
    
    class Meta:
        verbose_name = 'Pensionista sobreviviente'
        verbose_name_plural = 'Pensionista Sobreviviente'
    
# Estudios Realizados
class EstudiosRealizados(models.Model):
    trabajador = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    inicio = models.DateField()
    fin = models.DateField()
    grado_instruccion = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    sub_especialidad = models.CharField(max_length=100, blank=True, null=True)
    cod_especialidad = models.CharField(max_length=50, blank=True, null=True)
    fecha_expedicion = models.DateField()
    pdfer = models.FileField(upload_to='estudios_realizados/')

    def __str__(self):
        return self.grado_instruccion
