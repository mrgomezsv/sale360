from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # Ruta del dashboard
    path('', views.pedidos, name='pedidos'),
]
