from __future__ import absolute_import, unicode_literals
from celery import shared_task
from ..producto.producto.models import Inventario
from ..ventas.models import Historial

@shared_task
def cargar_al_inventario(documento):
	his = Historial.objects.get(id=documento)
	for l in his.listado.all():
		inv = Inventario.objects.filter(
			tienda=his.tienda).filter(
			producto=l.producto)
		if inv.exists():
			inv=inv[0]
			inv.cantidad=inv.cantidad+l.cantidad
			if inv.costo<l.precio:
				inv.costo 		 = l.precio
				if l.precio*1.2 > inv.distribuidor:
					inv.distribuidor =l.precio*1.2

				if l.precio*1.5 > inv.mayorista:
					inv.mayorista 	 = l.precio*1.5
					
				if l.precio*1.8 > inv.efectivo:
					inv.efectivo 	 = l.precio*1.8

				if l.precio*2 > inv.tarjeta:
					inv.tarjeta 	 = l.precio*2
		else:
			inv= Inventario()
			inv.tienda 		 = his.tienda
			inv.producto 	 = l.producto
			inv.cantidad	 = l.cantidad
			inv.costo		 = l.precio
			inv.distribuidor = float(l.precio)*1.2
			inv.mayorista	 = float(l.precio)*1.5
			inv.efectivo	 = float(l.precio)*1.8
			inv.tarjeta		 = float(l.precio)*2
		inv.save()
