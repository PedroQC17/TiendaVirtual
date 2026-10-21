from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    class Rol(models.TextChoices):
        DUENA = "duena", "Dueña"
        VENDEDOR = "vendedor", "Vendedor"

    email = models.EmailField(unique=True)
    rol = models.CharField(max_length=10, choices=Rol.choices, default=Rol.DUENA)