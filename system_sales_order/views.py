from django.shortcuts import render

def pedidos_view(request):
    return render(request, 'pedidos.html')
