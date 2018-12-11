
from django.urls import path
from django.conf.urls import url
from .views import (
	index,
	orden_de_compra,
	agregar,
	quitar,
	facturacion,
	documento,
	cargar,
	remover)

urlpatterns = [
	path('',index.as_view(),name="index"),
	path('orden_de_compra/',orden_de_compra.as_view(),name="orden_de_compra"),
	path('agregar/',agregar.as_view(),name="agregar"),
	path('quitar/',quitar.as_view(),name="quitar"),
	path('facturacion/',facturacion.as_view(),name="facturacion"),
	url(r'^facturacion/(?P<id>\d+)/$', documento.as_view(), name='documento'),

	path('cargar/',cargar.as_view(),name="cargar"),
	path('remover/',remover.as_view(),name="remover"),
	
]
