from django.contrib.auth.models import User
from django.db import models

class EnlaceSocial(models.Model):
    nombre = models.CharField(max_length=100)
    url = models.URLField()
    imagen = models.ImageField(upload_to='enlaces/', blank=True, null=True)  # Nueva línea

    def __str__(self):
        return self.nombre

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='perfiles/', null=True, blank=True)

    def __str__(self):
        return self.user.username

