from django.urls import path
from.import views

app_name="productos"

urlpatterns = [
    path('admin/listado', views.AdminListadoProductos.as_view(), name="adm_listado_productos"),
    path('admin/nuevo', views.NuevoProducto.as_view(), name="adm_nuevo_producto"),
    path('admin/editar/<int:pk>', views.EditarProducto.as_view(), name="editar"),
    path('me-gusta/<int:id_producto>', views.dar_mg, name="dar_mg"),
]
