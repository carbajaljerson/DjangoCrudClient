from django.db import models
from django.utils import timezone

# Create your models here.
class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    razon_social = models.CharField(max_length=20)
    direccion =  models.CharField(max_length=255)
    telefono =  models.CharField(max_length=20)
    celular  =  models.CharField(max_length=20)
    ruc =  models.CharField(max_length=11)
    contacto =  models.CharField(max_length=255)
    fecha_registro = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.razon_social