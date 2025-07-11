from django.urls import path
from .views import home, login_view, logout_view, dashboard, agregar_producto

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('agregar-producto/', agregar_producto, name='agregar_producto'),
]
