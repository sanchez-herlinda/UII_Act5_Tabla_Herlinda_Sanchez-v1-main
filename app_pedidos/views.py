from django.shortcuts import render
from .models import Pedidos
# Create your views here.
def index(request):
    pedidos_s = Pedidos.objects.all()
    return render(request, 'index.html', {'pedidos': pedidos_s})