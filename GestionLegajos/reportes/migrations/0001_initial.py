# Generated by Django 5.1.3 on 2025-03-27 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlantillaReporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('constancia', 'Constancia de Trabajo'), ('escalafonario', 'Informe Escalafonario')], default='constancia', max_length=50)),
                ('archivo', models.FileField(upload_to='plantillas_reportes/')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
    ]
