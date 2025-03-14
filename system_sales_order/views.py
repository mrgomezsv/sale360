# system_sales_order/views.py
from django.shortcuts import render

def lista_presupuestos(request):
    # Lógica para obtener los datos de los presupuestos
    presupuestos = [
        {'numero': 1, 'cliente': 'Cliente A', 'total': 1000},
        {'numero': 2, 'cliente': 'Cliente B', 'total': 2000},
    ]
    context = {
        'presupuestos': presupuestos,
    }
    return render(request, 'lista_presupuestos.html', context)
