from django.contrib import admin
from .models import Producto,Filtro

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'destacado', 'creado']


admin.site.register(Filtro)