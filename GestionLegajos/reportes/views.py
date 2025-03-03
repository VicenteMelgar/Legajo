from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from docxtpl import DocxTemplate
from legajos.models import Legajo, Vinculo
from io import BytesIO

def formulario_reportes(request):
    # Obtener la lista de trabajadores
    trabajadores = Legajo.objects.all()
    return render(request, 'formulario_reportes.html', {'trabajadores': trabajadores})

def generar_constancia(request, id_trabajador):
    trabajador_id = request.GET.get('trabajador')  # ID del trabajador desde el formulario
    trabajador = get_object_or_404(Legajo, id=trabajador_id)  # Buscar el trabajador

    # Filtrar servicios relacionados con el trabajador
    vinculos = Vinculo.objects.filter(legajo__in=[trabajador])  # Corregido

    # Verificar si se están obteniendo los vínculos
    print("Trabajador seleccionado:", trabajador)
    print("Vínculos encontrados:", vinculos)

    # Contexto para el template
    context = {
        'trabajador': trabajador,
        'vinculos': vinculos,  # Corregido (antes estaba en singular)
    }

    return render(request, 'constancia_trabajo.html', context)

def descargar_constancia(request, trabajador_id):
    trabajador = get_object_or_404(Legajo, id=trabajador_id)

    # Filtrar servicios prestados seleccionados manualmente
    vinculo_ids = request.GET.getlist('vinculos')  # Corregido el nombre de la clave
    vinculos = Vinculo.objects.filter(id__in=vinculo_ids, legajo__in=[trabajador])  # Corregido el filtro

    # Verificar si se están obteniendo vínculos
    print("Vínculos seleccionados:", vinculos)  # Esto imprimirá los vínculos en la consola

    # Plantilla para constancia
    template_path = 'reportes/plantillas/constancia_template.docx'
    doc = DocxTemplate(template_path)

    context = {
        'nombre': f'{trabajador.empleado.nombres} {trabajador.empleado.apellido_paterno} {trabajador.empleado.apellido_materno}',
        'dni': trabajador.empleado.dni,
        'vinculos': vinculos,
    }

    doc.render(context)
    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)

    response = HttpResponse(buffer, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = f'attachment; filename="Constancia_{trabajador.empleado.nombres}_{trabajador.empleado.apellido_paterno}_{trabajador.empleado.apellido_materno}.docx"'
    return response

def generar_informe(request, id_trabajador):
    trabajador_id = request.GET.get('trabajador')  # ID del trabajador desde el formulario
    trabajador = get_object_or_404(Legajo, id=trabajador_id)  # Buscar el trabajador

    # Filtrar servicios relacionados con el trabajador
    vinculo = Vinculo.objects.filter(legajo_id=trabajador_id)

    # Contexto para el template
    context = {
        'trabajador': trabajador,
        'vinculo': vinculo,
    }

    return render(request, 'informe_trabajo.html', context)
  
def descargar_informe(request, trabajador_id):
    trabajador = get_object_or_404(Legajo, id=trabajador_id)

    # Filtrar servicios prestados seleccionados manualmente
    vinculo_ids = request.GET.getlist('vinculo')
    vinculos = Vinculo.objects.filter(id__in=vinculo_ids, legajo=trabajador)

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

