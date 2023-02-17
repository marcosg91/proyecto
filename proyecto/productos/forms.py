from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    nombre=  forms.CharField(label="Nombre", widget=forms.TextInput(attrs={"class":"form-control"}))
    descripcion = forms.CharField(label="Descripcion", widget=forms.TextInput(attrs={"class":"form-control"}))
  
    
    class Meta:
        model=Producto
        fields=["nombre", "descripcion", "precio", "activo", "categoria", "categoria2", "imagen"]