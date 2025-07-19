from django.urls import path
from .views import lista_productos, detalle_producto, ver_carrito
from . import views

urlpatterns = [
    path('', lista_productos, name='lista_productos'),
    path('<int:pk>/', detalle_producto, name='detalle_producto'),
    path('carrito/', ver_carrito, name="ver_carrito"),
    path('carrito/agregar/<int:producto_id>/', views.agregar_carrito, name="agregar_carrito"),
    path('carrito/eliminar/<int:item_id>/', views.eliminar_carrito, name="eliminar_carrito"),
    path('carrito/limpiar/', views.limpiar_carrito, name="limpiar_carrito"),
    path('carrito/completar/', views.completar_compra, name='completar_compra'),
]
