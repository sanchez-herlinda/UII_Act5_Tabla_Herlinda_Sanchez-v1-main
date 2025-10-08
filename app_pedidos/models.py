from django.db import models

# Create your models here.
class Pedidos(models.Model):
    nombre=models.CharField(max_length=100)
    total=models.DecimalField(max_digits=10, decimal_places=2)
    estado=models.CharField(max_length=50, default='Pendiente')
# Es para administrador
    def __str__(self):
        return f"{self.total} {self.estado}"