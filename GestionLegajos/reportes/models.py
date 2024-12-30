from django.db import models

class PlantillaReporte(models.Model):
    TIPO_CHOICES = [
        ('constancia', 'Constancia de Trabajo'),
        ('escalafonario', 'Informe Escalafonario'),
    ]
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES, default='constancia')
    archivo = models.FileField(upload_to='plantillas_reportes/')
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre