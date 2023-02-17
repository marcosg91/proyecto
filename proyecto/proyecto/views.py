from django.shortcuts import render 

from django.contrib.auth.decorators import login_required

from utilidades.mixins import is_admin_required

from productos.models import Producto

@is_admin_required()
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