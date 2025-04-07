from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # Ruta del dashboard
    path('pedidos/', views.pedidos, name='pedidos'),
    path('a-facturar/', views.a_facturar, name='a_facturar'),
]
