from django.db import models

from categorias.models import Categoria

class Producto(models.Model):
    nombre=models.CharField(max_length=255)
    precio=models.DecimalField(max_digits=6, decimal_places=2)
    descripcion=models.TextField()

    activo=models.BooleanField(default=True)

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, related_name="categorias", blank=True)

    categoria2 = models.ManyToManyField(Categoria)

    #ficha = models.OneToOneField(Ficha)  para los casos de 1 a 1 (a un producto le corresponde una ficha); se deberia crear el modelo Ficha

    imagen = models.ImageField(upload_to="productos", null=True, blank=True)
    #tambien existe archivo = models.FileField

    def __str__(self):
        return self.nombre


"""
c = Categoria.objects.get(id=1)
c.categorias.all()

#crear tabla intermedia de forma manual: 
class ProductoCategoria(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True)
    # fecha
"""

