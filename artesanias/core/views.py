from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.admin.views.decorators import staff_member_required
from productos.models import Producto
from .models import EnlaceSocial
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileUpdateForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import logout


@login_required(login_url='/login/') 
def home(request):
    destacados = Producto.objects.filter(destacado=True)
    redes = EnlaceSocial.objects.all()
    return render(request, 'core/home.html', {'productos': destacados, 'redes': redes})

@csrf_protect
def login_view(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            # Cambia 'dashboard' a una vista accesible para usuarios normales, no sólo staff
            return redirect('home')  # o la vista que quieras para usuarios normales
        else:
            return render(request, 'core/login.html', {'error': 'Usuario o contraseña incorrectos'})
    return render(request, 'core/login.html')


def logout_view(request):
    logout(request)
    return redirect('home')

@staff_member_required
def dashboard(request):
    return render(request, 'core/dashboard.html')

@login_required(login_url='/login/') 
def contacto(request):
    enlaces = EnlaceSocial.objects.all()
    return render(request, 'core/contacto.html', {'enlaces': enlaces})
@login_required(login_url='/login/') 
def nosotros(request):
    enlaces = EnlaceSocial.objects.all()
    return render(request, 'core/nosotros.html', {'enlaces': enlaces})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'core/register.html', {'form': form})

@login_required(login_url='/login/')
def perfil_usuario(request):
    return render(request, 'core/perfil.html', {'usuario': request.user})

@login_required(login_url='/login/')
def editar_perfil(request):
    profile = getattr(request.user, 'profile', None)
    if not profile:
        return redirect('perfil_usuario')  # O crea el perfil si no existe

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('perfil_usuario')
    else:
        form = ProfileUpdateForm(instance=profile)

    return render(request, 'core/editar_perfil.html', {
        'form': form
    })
