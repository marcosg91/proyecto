from django.shortcuts import render 
from productos.models import Producto

def inicio(request):
    template_name = "index.html"
    """"
    p=Producto.objects.create(
        nombre="pantalon",
        precio=1500,
        descripcion="pantalaon azul"
    )
    """
    productos=Producto.objects.all()
    
    contexto = {
        'productos': productos
    }
    return render(request, template_name, contexto)