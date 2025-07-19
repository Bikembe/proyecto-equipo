from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.admin.views.decorators import staff_member_required
from productos.models import Producto
from .models import EnlaceSocial, Profile
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import logout
from django.contrib import messages


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

def contacto(request):
    enlaces = EnlaceSocial.objects.all()
    return render(request, 'core/contacto.html', {'enlaces': enlaces})

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

def perfil_usuario(request):
    return render(request, 'core/perfil.html', {'usuario': request.user})

def editar_perfil(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        imagen = request.FILES.get('imagen')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        user = request.user
        user.username = username
        user.email = email
        user.save()

        # Imagen de perfil
        profile, _ = Profile.objects.get_or_create(user=user)
        if imagen:
            profile.imagen = imagen
            profile.save()

        # Cambio de contraseña
        if password1 and password2:
            if password1 == password2:
                user.set_password(password1)
                user.save()
                messages.success(request, 'Perfil actualizado. Debes volver a iniciar sesión con tu nueva contraseña.')
                return redirect('login')
            else:
                messages.error(request, 'Las contraseñas no coinciden.')
                return redirect('editar_perfil')

        messages.success(request, 'Perfil actualizado correctamente.')
        return redirect('perfil_usuario')

    return render(request, 'usuarios/editar_perfil.html', {'usuario': request.user})
