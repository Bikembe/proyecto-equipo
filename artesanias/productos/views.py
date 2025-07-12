from django.shortcuts import render, get_object_or_404
from .models import Producto, Filtro

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'productos/detalle.html', {'producto': producto})

def lista_productos(request):
    filtro_slug = request.GET.get('filtro')
    filtros = Filtro.objects.all()
    productos = Producto.objects.all()
    print('Filtro recibido:', filtro_slug)  # Para debug

    if filtro_slug:
        try:
            filtro_obj = Filtro.objects.get(slug=filtro_slug)
            productos = productos.filter(filtro=filtro_obj)
        except Filtro.DoesNotExist:
            productos = Producto.objects.none()  # No hay filtro, no mostrar nada o todos

    return render(request, 'productos/lista.html', {
        'productos': productos,
        'filtros': filtros,
        'filtro_seleccionado': filtro_slug
    })

