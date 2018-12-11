from django.urls import path,include
from .views import index,ventas,cliente,proveedor,buscar_proveedor,buscar_cliente

urlpatterns = [
    path('',index.as_view(),name="index"),
    path('ventas/',ventas.as_view(),name="ventas"),
    path('clientes/',cliente.as_view(),name="cliente"),
    path('proveedor/',proveedor.as_view(),name="proveedor"),
    path('buscar_proveedor/',buscar_proveedor.as_view(),name="buscar_proveedor"),
    path('buscar_cliente/',buscar_cliente.as_view(),name="buscar_cliente"),
    

]
