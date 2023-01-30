from django.shortcuts import render 
from productos.models import Producto

def inicio(request):
    template_name = 'index.html'

    """"
    p=Producto.objects.create(
        nombre="pantalon",
        precio=1500,
        descripcion="pantalaon azul"
    )
    """

    
    
    contexto = {
        'productos': Producto.objects.filter(activo=True)
    }
    return render(request, template_name, contexto)

"""
def login(request):
    print("entre al login")
    print(request.GET["password"])

    return render(request, "login.html",{})
"""