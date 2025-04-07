from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')  # Ruta directa a la plantilla

@login_required
def pedidos_view(request):
    return render(request, 'pedidos.html')
