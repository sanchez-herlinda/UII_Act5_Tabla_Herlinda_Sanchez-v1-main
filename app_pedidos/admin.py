from django.contrib import admin

# Register your models here.
from .models import Pedidos

# Registrar el modelo Pedidos en el admin
admin.site.register(Pedidos)