from django.urls import path
from . import views

urlpatterns = [
    path('presupuestos/', views.lista_presupuestos, name='lista_presupuestos'),
]
