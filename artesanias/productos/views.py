from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Filtro, Carrito, ItemCarrito
from django.contrib.auth.decorators import login_required

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

@login_required(login_url='/login/') 
def agregar_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    item, creado = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
    if not creado:
        item.cantidad += 1
        item.save()
    return redirect('ver_carrito')

@login_required(login_url='/login/')
def ver_carrito(request):
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    items = carrito.items.select_related('producto')
    total = carrito.total()
    return render(request, "productos/carrito.html", {"items": items, "total": total})

@login_required(login_url='/login/')
def eliminar_carrito(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id, carrito__usuario=request.user)
    item.delete()
    return redirect('ver_carrito')

@login_required(login_url='/login/')
def limpiar_carrito(request):
    carrito = get_object_or_404(Carrito, usuario=request.user)
    carrito.items.all().delete()
    return redirect('ver_carrito')

@login_required(login_url='/login/')
def completar_compra(request):
    if request.method == "POST":
        carrito = get_object_or_404(Carrito, usuario=request.user)
        carrito.items.all().delete()
        return render(request, "productos/carrito.html", {"items": [], "total": 0, "mensaje": "Gracias por su compra"})
    return redirect('ver_carrito')