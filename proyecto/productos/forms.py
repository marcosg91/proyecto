from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    nombre=  forms.CharField(label="Nombre", widget=forms.TextInput(attrs={"class":"form-control"}))
    descripcion = forms.CharField(label="Descripcion", widget=forms.TextInput(attrs={"class":"form-control"}))
  
    
    class Meta:
        model=Producto
        fields=["nombre", "descripcion", "precio", "activo", "categoria", "categoria2", "imagen"]
    
    def clean_precio(self):
        precio = self.cleaned_data["precio"]
        if precio <= 0:
            raise forms.ValidationError("el precio debe ser un numero positivo")
        return precio