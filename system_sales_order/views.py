from django.shortcuts import render
from .models import Presupuesto

def lista_presupuestos(request):
    presupuestos = Presupuesto.objects.all()  # Obtener todos los presupuestos
    return render(request, 'presupuestos/lista_presupuestos.html', {'presupuestos': presupuestos})
