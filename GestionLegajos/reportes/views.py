from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from docxtpl import DocxTemplate
from legajos.models import DatosPersonales, ServiciosPrestados
from io import BytesIO

def formulario_reportes(request):
    # Obtener la lista de trabajadores
    trabajadores = DatosPersonales.objects.all()
    return render(request, 'formulario_reportes.html', {'trabajadores': trabajadores})

def generar_constancia(request, id_trabajador):
    trabajador_id = request.GET.get('trabajador')  # ID del trabajador desde el formulario
    trabajador = get_object_or_404(DatosPersonales, id=trabajador_id)  # Buscar el trabajador

    # Filtrar servicios relacionados con el trabajador
    servicios = ServiciosPrestados.objects.filter(empleado__id=trabajador_id)

    # Contexto para el template
    context = {
        'trabajador': trabajador,
        'servicios': servicios,
    }

    return render(request, 'constancia_trabajo.html', context)

def descargar_constancia(request, trabajador_id):
    trabajador = get_object_or_404(DatosPersonales, id=trabajador_id)

    # Filtrar servicios prestados seleccionados manualmente
    servicios_ids = request.GET.getlist('servicios')
    servicios = ServiciosPrestados.objects.filter(id__in=servicios_ids, empleado=trabajador)

    # Plantilla para constancia
    template_path = 'reportes/plantillas/constancia_template.docx'
    doc = DocxTemplate(template_path)

    context = {
        'nombre': f'{trabajador.nombres} {trabajador.apellido_paterno} {trabajador.apellido_materno}',
        'dni': trabajador.dni,
        'servicios': [
            {
                'cargo': ', '.join(cargo.denominacion for cargo in servicio.cargo.all()),
                'dependencia': servicio.dependencia,
                'fecha_inicio': servicio.fecha_vigencia,
                'fecha_fin': servicio.fecha_fin or 'actualidad',
            }
            for servicio in servicios
        ],
    }

    doc.render(context)
    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)

    response = HttpResponse(buffer, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = f'attachment; filename="Constancia_{trabajador.nombres}_{trabajador.apellido_paterno}_{trabajador.apellido_materno}.docx"'
    return response

def generar_informe(request, id_trabajador):
    trabajador_id = request.GET.get('trabajador')  # ID del trabajador desde el formulario
    trabajador = get_object_or_404(DatosPersonales, id=trabajador_id)  # Buscar el trabajador

    # Filtrar servicios relacionados con el trabajador
    servicios = ServiciosPrestados.objects.filter(empleado__id=trabajador_id)

    # Contexto para el template
    context = {
        'trabajador': trabajador,
        'servicios': servicios,
    }

    return render(request, 'informe_trabajo.html', context)
  
def descargar_informe(request, trabajador_id):
    trabajador = get_object_or_404(DatosPersonales, id=trabajador_id)

    # Obtener servicios seleccionados
    servicios_ids = request.GET.getlist('servicios')
    servicios = ServiciosPrestados.objects.filter(id__in=servicios_ids, empleado=trabajador)

    # Cargar plantilla del informe
    template_path = 'reportes/plantillas/informe_template.docx'
    doc = DocxTemplate(template_path)

    # Contexto para reemplazar en la plantilla
    context = {
        'nombre': f'{trabajador.nombres} {trabajador.apellido_paterno} {trabajador.apellido_materno}',
        'dni': trabajador.dni,
        'servicios': [
            {
                'cargo': ', '.join(cargo.denominacion for cargo in servicio.cargo.all()),
                'dependencia': servicio.dependencia,
                'fecha_inicio': servicio.fecha_vigencia,
                'fecha_fin': servicio.fecha_fin or 'actualidad',
            }
            for servicio in servicios
        ],
    }

    doc.render(context)

    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)

    response = HttpResponse(buffer, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = f'attachment; filename="Informe_{trabajador.nombres}_{trabajador.apellido_paterno}_{trabajador.apellido_materno}.docx"'
    return response

