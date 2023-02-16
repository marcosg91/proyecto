from django.shortcuts import render 
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from django.urls import reverse

from .forms import ProductoForm
from .models import Producto

"""
def adm_listado_productos(request):
    template_name = 'productos/listado.html'

    contexto = {
        'productos': Producto.objects.all()
    }
    return render(request, template_name, contexto)
"""


class AdminListadoProductos (ListView):
    template_name = "productos/listado.html"
    model = Producto
    context_object_name = "productos"
    paginate_by = 3

    def get_queryset(self):
        productos = Producto.objects.all()
        nombre_producto = self.request.GET.get("buscador")
        if nombre_producto:
            productos = productos.filter(nombre__contains=nombre_producto)
        return productos.order_by("nombre")


class NuevoProducto(CreateView):
    model= Producto
    template_name = "productos/nuevo_producto.html"
    form_class = ProductoForm

    def get_success_url(self):
        return reverse("productos:adm_listado_productos")

class EditarProducto(UpdateView):
    model= Producto
    template_name = "productos/editar.html"
    form_class = ProductoForm

    def get_success_url(self):
        return reverse("productos:adm_listado_productos")