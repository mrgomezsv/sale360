from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('pedidos/', views.pedidos, name='pedidos'),
    path('pedidos/nuevo/', views.pedido_nuevo, name='pedido_nuevo'),
    path('pedidos/<int:pk>/editar/', views.pedido_editar, name='pedido_editar'),
    path('pedidos/<int:pk>/eliminar/', views.pedido_eliminar, name='pedido_eliminar'),
    path('api/products/<int:product_id>/', views.get_product_info, name='get_product_info'),
    path('a-facturar/', views.a_facturar, name='a_facturar'),
]
