from django.shortcuts import render
from vistaprevia.models import Producto
from django.db.models import Q

def index(request):
    params = {}
    params['nombre_sitio'] = 'Libros Online'
    productos = Producto.objects.filter(Q(estado="Publicado"))
    params['productos'] = productos
    return render(request, 'vistaprevia/index.html', params)
    




