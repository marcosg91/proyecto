from django import forms
from django.contrib.auth.forms import UserCreationForm


from .models import Usuario

class UsuarioForm(UserCreationForm):
    first_name=forms.CharField(label="Nombre", widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name=forms.CharField(label="Apellido", widget=forms.TextInput(attrs={"class":"form-control"}))
    email=forms.CharField(label="e-mail", widget=forms.TextInput(attrs={"class":"form-control"}))
    username=forms.CharField(label="Nombre de Usuario", widget=forms.TextInput(attrs={"class":"form-control"}))
    password1=forms.CharField(label="Contraseña", widget=forms.TextInput(attrs={"class":"form-control"}))
    password2=forms.CharField(label="Confirmar", widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model= Usuario
        fields=["first_name", "last_name", "email", "username", "password1", "password2"]