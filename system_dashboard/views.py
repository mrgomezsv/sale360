from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def pedidos(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return render(request, 'pedidos_partial.html')
    return render(request, 'pedidos.html')
