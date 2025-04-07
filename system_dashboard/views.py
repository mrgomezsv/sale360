from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db import transaction
from django.contrib import messages
from .models import SaleOrder, Product
from .forms import SaleOrderForm, SaleOrderLineFormSet

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def pedidos(request):
    pedidos = SaleOrder.objects.all().order_by('-date_order')
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return render(request, 'pedidos.html', {'pedidos': pedidos})
    return render(request, 'pedidos.html', {'pedidos': pedidos})

@login_required
def pedido_nuevo(request):
    if request.method == 'POST':
        form = SaleOrderForm(request.POST)
        formset = SaleOrderLineFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            try:
                with transaction.atomic():
                    pedido = form.save(commit=False)
                    pedido.user_id = request.user
                    pedido.save()
                    
                    formset.instance = pedido
                    formset.save()
                    
                    # Calcular totales
                    for line in pedido.order_line.all():
                        line.calculate_amounts()
                    pedido.calculate_amounts()
                    
                    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                        return JsonResponse({'success': True})
                    return redirect('pedidos')
            except Exception as e:
                error_msg = f'Error al crear el pedido: {str(e)}'
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({'success': False, 'error': error_msg})
                messages.error(request, error_msg)
    else:
        form = SaleOrderForm()
        formset = SaleOrderLineFormSet()
    
    context = {
        'form': form,
        'formset': formset
    }
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return render(request, 'pedido_form.html', context)
    return render(request, 'pedido_form.html', context)

@login_required
def pedido_editar(request, pk):
    pedido = get_object_or_404(SaleOrder, pk=pk)
    if request.method == 'POST':
        form = SaleOrderForm(request.POST, instance=pedido)
        formset = SaleOrderLineFormSet(request.POST, instance=pedido)
        if form.is_valid() and formset.is_valid():
            try:
                with transaction.atomic():
                    pedido = form.save()
                    formset.save()
                    
                    # Calcular totales
                    for line in pedido.order_line.all():
                        line.calculate_amounts()
                    pedido.calculate_amounts()
                    
                    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                        return JsonResponse({'success': True})
                    return redirect('pedidos')
            except Exception as e:
                error_msg = f'Error al actualizar el pedido: {str(e)}'
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({'success': False, 'error': error_msg})
                messages.error(request, error_msg)
    else:
        form = SaleOrderForm(instance=pedido)
        formset = SaleOrderLineFormSet(instance=pedido)
    
    context = {
        'form': form,
        'formset': formset
    }
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return render(request, 'pedido_form.html', context)
    return render(request, 'pedido_form.html', context)

@login_required
def pedido_eliminar(request, pk):
    pedido = get_object_or_404(SaleOrder, pk=pk)
    try:
        pedido.delete()
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': True})
        messages.success(request, 'Pedido eliminado exitosamente.')
    except Exception as e:
        error_msg = f'Error al eliminar el pedido: {str(e)}'
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'error': error_msg})
        messages.error(request, error_msg)
    return redirect('pedidos')

@login_required
def get_product_info(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return JsonResponse({
        'name': product.name,
        'list_price': str(product.list_price),
        'description': product.description
    })

@login_required
def a_facturar(request):
    pedidos = SaleOrder.objects.filter(state='sale').order_by('-date_order')
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return render(request, 'a_facturar.html', {'pedidos': pedidos})
    return render(request, 'a_facturar.html', {'pedidos': pedidos})
