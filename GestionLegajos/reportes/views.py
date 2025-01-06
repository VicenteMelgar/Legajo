from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from docxtpl import DocxTemplate
from legajos.models import DatosPersonales, Vinculo
from io import BytesIO

def formulario_reportes(request):
    # Obtener la lista de trabajadores
    trabajadores = DatosPersonales.objects.all()
    return render(request, 'formulario_reportes.html', {'trabajadores': trabajadores})

def generar_constancia(request, id_trabajador):
    trabajador_id = request.GET.get('trabajador')  # ID del trabajador desde el formulario
    trabajador = get_object_or_404(DatosPersonales, id=trabajador_id)  # Buscar el trabajador

    # Filtrar servicios relacionados con el trabajador
    vinculo = Vinculo.objects.filter(empleado__id=trabajador_id)

    # Contexto para el template
    context = {
        'trabajador': trabajador,
        'vinculo': vinculo,
    }

    return render(request, 'constancia_trabajo.html', context)

def descargar_constancia(request, trabajador_id):
    trabajador = get_object_or_404(DatosPersonales, id=trabajador_id)

    # Filtrar servicios prestados seleccionados manualmente
    vinculo_ids = request.GET.getlist('vinculo')
    vinculos = Vinculo.objects.filter(id__in=vinculo_ids, empleado=trabajador)

    # Plantilla para constancia
    template_path = 'reportes/plantillas/constancia_template.docx'
    doc = DocxTemplate(template_path)

    context = {
        'nombre': f'{trabajador.nombres} {trabajador.apellido_paterno} {trabajador.apellido_materno}',
        'dni': trabajador.dni,
        'vinculos': [
            {
                'cargo': ', '.join(cargo.denominacion for cargo in vinculo.cargo.all()),
                'fecha_inicio': vinculo.fecha_vigencia,
                'fecha_fin': vinculo.fecha_fin or 'actualidad',
            }
            for vinculo in vinculos
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
    vinculo = Vinculo.objects.filter(empleado__id=trabajador_id)

    # Contexto para el template
    context = {
        'trabajador': trabajador,
        'vinculo': vinculo,
    }

    return render(request, 'informe_trabajo.html', context)
  
def descargar_informe(request, trabajador_id):
    trabajador = get_object_or_404(DatosPersonales, id=trabajador_id)

    # Filtrar servicios prestados seleccionados manualmente
    vinculo_ids = request.GET.getlist('vinculo')
    vinculos = Vinculo.objects.filter(id__in=vinculo_ids, empleado=trabajador)

    # Plantilla para constancia
    template_path = 'reportes/plantillas/constancia_template.docx'
    doc = DocxTemplate(template_path)

    context = {
        'nombre': f'{trabajador.nombres} {trabajador.apellido_paterno} {trabajador.apellido_materno}',
        'dni': trabajador.dni,
        'vinculos': [
            {
                'cargo': ', '.join(cargo.denominacion for cargo in vinculo.cargo.all()),
                'fecha_inicio': vinculo.fecha_vigencia,
                'fecha_fin': vinculo.fecha_fin or 'actualidad',
            }
            for vinculo in vinculos
        ],
    }

    doc.render(context)
    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)

    response = HttpResponse(buffer, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = f'attachment; filename="Informe_{trabajador.nombres}_{trabajador.apellido_paterno}_{trabajador.apellido_materno}.docx"'
    return response

