# system_sales_order/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('pedidos/', views.lista_presupuestos, name='lista_presupuestos'),
]
