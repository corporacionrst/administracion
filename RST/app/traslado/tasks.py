from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import Traslados
from ..producto.producto.models import Inventario

@shared_task
def autorizar_traslado(traslado):
	traslado=Traslados.objects.get(id=traslado)
	solicita = traslado.tienda_solicita
	recibe = traslado.tienda_recibe
	for producto in traslado.lista.all():
		inventario_recibe_peticion = Inventario.objects.filter(
			tienda=recibe).filter(
			producto=producto.producto)[0]
		inventario_solicita= Inventario.objects.filter(
			tienda=solicita).filter(
			producto=producto.producto
			)
		if not inventario_solicita.exists():
			inventario_solicita					= Inventario()
			inventario_solicita.tienda 			= solicita
			inventario_solicita.producto 	 	= inventario_recibe_peticion.producto
			inventario_solicita.cantidad	 	= producto.cantidad
		else:
			inventario_solicita=inventario_solicita[0]
			inventario_solicita.cantidad		=inventario_solicita.cantidad+producto.cantidad
		if inventario_solicita.distribuidor < producto.precio:
			inventario_solicita.costo		 	= inventario_recibe_peticion.costo
			inventario_solicita.distribuidor 	= inventario_recibe_peticion.distribuidor
			inventario_solicita.mayorista	 	= inventario_recibe_peticion.mayorista
			inventario_solicita.efectivo	 	= inventario_recibe_peticion.efectivo
			inventario_solicita.tarjeta			= inventario_recibe_peticion.tarjeta
		inventario_solicita.save()
		inventario_recibe_peticion.cantidad=inventario_recibe_peticion.cantidad - producto.cantidad
		inventario_recibe_peticion.save()
