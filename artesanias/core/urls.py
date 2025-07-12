from django.urls import path
from .views import home, login_view, logout_view, dashboard, agregar_producto
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('agregar-producto/', agregar_producto, name='agregar_producto'),
    path('contacto/', views.contacto, name='contacto'),
    path('nosotros/', views.nosotros, name='nosotros'),
]
