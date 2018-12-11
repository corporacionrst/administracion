from django.urls import path
from .views import solicitar,tienda,stock,agregar,quitar,autorizar,pdf,listar

urlpatterns = [

    path('solicitar/',solicitar.as_view(),name="solicitar"),
    path('tienda/',tienda.as_view(),name="tienda"),
    path('stock/',stock.as_view(),name="stock"),
    path('agregar/',agregar.as_view(),name="agregar"),
    path('quitar/',quitar.as_view(),name="quitar"),
    path('pdf/<int:id>',pdf.as_view(),name="pdf"),
    path('listar/',listar.as_view(),name="listar"),

    path('autorizar/',autorizar.as_view(),name="autorizar")
]
