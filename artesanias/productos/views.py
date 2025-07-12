from django.shortcuts import render, get_object_or_404
from .models import Producto, Filtro

from django.contrib.auth.decorators import login_required
@login_required(login_url='/login/') 
def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    filtros = Filtro.objects.all()
    filtro_slug = request.GET.get('filtro')

    mas_productos = Producto.objects.exclude(pk=pk)[:4]

    return render(request, 'productos/detalle.html', {
        'producto': producto,
        'filtros': filtros,
        'filtro_seleccionado': filtro_slug,
        'mas_productos': mas_productos,
    })
@login_required(login_url='/login/') 
def lista_productos(request):
    filtro_slug = request.GET.get('filtro')
    filtros = Filtro.objects.all()
    productos = Producto.objects.all()

    if filtro_slug:
        try:
            filtro_obj = Filtro.objects.get(slug=filtro_slug)
            productos = productos.filter(filtro=filtro_obj)
        except Filtro.DoesNotExist:
            productos = Producto.objects.none()

    return render(request, 'productos/lista.html', {
        'productos': productos,
        'filtros': filtros,
        'filtro_seleccionado': filtro_slug
    })

