from django.shortcuts import render, redirect
from .models import DatosPersonales
from .forms import DatosPersonalesForm

def datospersonales_lista_creada(request):
  
  if request.method == 'POST':
    form = DatosPersonalesForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('legajos:datos_personales')
  else:
    form = DatosPersonalesForm()
    
  datos_personales = DatosPersonales.objects.all()
  
  return render(request, 'datos_personales.html', {
    'form':form,
    'datos_personales':datos_personales
  })


