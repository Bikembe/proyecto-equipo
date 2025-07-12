from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.admin.views.decorators import staff_member_required
from productos.models import Producto
from .forms import ProductoForm
from .models import EnlaceSocial

def home(request):
    destacados = Producto.objects.filter(destacado=True)
    redes = EnlaceSocial.objects.all()
    return render(request, 'core/home.html', {'productos': destacados, 'redes': redes})

def login_view(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'core/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@staff_member_required
def dashboard(request):
    return render(request, 'core/dashboard.html')

@staff_member_required
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProductoForm()
    return render(request, 'core/agregar_producto.html', {'form': form})

def contacto(request):
    enlaces = EnlaceSocial.objects.all()
    return render(request, 'core/contacto.html', {'enlaces': enlaces})

def nosotros(request):
    enlaces = EnlaceSocial.objects.all()
    return render(request, 'core/nosotros.html', {'enlaces': enlaces})