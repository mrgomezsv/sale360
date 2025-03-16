from django.urls import path
from . import views

urlpatterns = [
    path('pedidos/', views.pedidos_view, name='pedidos'),
]
