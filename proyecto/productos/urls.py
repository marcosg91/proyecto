from django.urls import path
from.import views

app_name="productos"

urlpatterns = [
    path('admin/listado', views.adm_listado_productos, name="adm_listado_productos"),
    path('admin/nuevo', views.NuevoProducto.as_view(), name="adm_nuevo_producto"),
]