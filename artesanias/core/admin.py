from django.contrib import admin
from .models import EnlaceSocial
from django.utils.html import format_html

@admin.register(EnlaceSocial)
class EnlaceSocialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'url', 'imagen_preview')

    def imagen_preview(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" style="width: 50px; height: auto;" />', obj.imagen.url)
        return "-"
    imagen_preview.short_description = 'Imagen'
