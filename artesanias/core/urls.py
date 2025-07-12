from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),

    path('login/', views.login_view, name='login'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('contacto/', views.contacto, name='contacto'),
    path('nosotros/', views.nosotros, name='nosotros'),

    path('register/', views.register, name='register'),

    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('logout/', views.logout_view, name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)