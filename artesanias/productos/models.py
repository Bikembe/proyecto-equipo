from django.db import models

class Filtro(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='productos/')
    destacado = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)
    filtro = models.ForeignKey(Filtro, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.nombre
