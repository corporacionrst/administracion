from django.shortcuts import render


from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
import json

from django.views.generic import TemplateView
from ...logica.admin import admin
from ..producto.models import Producto
from ...usuario.models import Usuario
from ...ventas.models import Compra, Historial ,Orden,Venta
from ...logica.ventas import ventas

from django.db.models import F ,DecimalField
from decimal import Decimal


class venta(TemplateView):
	def get(self,request,*args,**kwargs):
		usu = Usuario.objects.filter(usuario=request.user)
		if usu.exists():
			usu 	= usu[0]
			pag 	= int(request.GET['pag'])*10
			pagina 	= int(request.GET['pagina'])
			venta 	= Venta.objects.filter(
				autoriza=usu,
				autorizacion=False,
				documento__hoja=pagina)
			if venta.exists():
				venta = venta[0].documento
				total = venta.total
				venta = venta.listado.all()[pag:pag+10]
				venta = venta.annotate(total=F("cantidad")*F("precio"))
				venta = venta.values(
					"id",
					"producto__producto__codigo",
					"producto__producto__descripcion",
					"producto__producto__marca__nombre",
					"cantidad",
					"precio",
					"total"
				)	
				venta=list(venta)
				venta.append(total)
				venta=json.dumps(venta,cls=DjangoJSONEncoder)
				return HttpResponse(venta,content_type="application/json")
		return HttpResponse("{}",content_type="application/json")
		


class compra(TemplateView):
	def get(self,request,*args,**kwargs):
		usu = Usuario.objects.filter(usuario=request.user)
		if usu.exists():
			usu 	= usu[0]
			pag 	= int(request.GET['pag'])*10
			orden 	= Orden.objects.filter(
				enviado =False,
				documento__usuario=usu)
			if orden.exists():
				orden = orden[0]
				orden = orden.documento
				total = orden.total
				orden = orden.listado.all()[pag:pag+10]
				orden = orden.annotate(total=F("cantidad")*F("precio"))
				orden = orden.values(
					"id",
					"producto__producto__codigo",
					"producto__producto__descripcion",
					"producto__producto__marca__nombre",
					"cantidad",
					"precio",
					"total"
				)	
				orden=list(orden)
				orden.append(total)
				orden=json.dumps(orden,cls=DjangoJSONEncoder)
				return HttpResponse(orden,content_type="application/json")
		return HttpResponse("{}",content_type="application/json")
		


# class buscar(TemplateView):
# 	def get(self,request,*args,**kwargs):
# 		usu = Usuario.objects.all()
# 		if usu.exists():
# 			pag=int(request.GET['pag'])*10
# 			consulta=request.GET['codigo'].upper()
# 			usu=usu[0]
# 			producto=Lista.objects.filter(producto__producto__icontains="codigo")
# 			if producto.exists():
# 				# c=c[0]
# 				# t='total:'+str(c.total)
# 				# c=c.lista_productos.all()[pag:pag+10]
# 				# c=c.annotate(total=F("cantidad")*F("unitario"))
# 				# c=c.values("cantidad","producto__producto__codigo","producto__producto__descripcion","unitario","producto__producto__marca__nombre","id","total")
# 				# c=list(c)
# 				# c.append(t)
# 				# c=json.dumps(c,cls=DjangoJSONEncoder)
# 				return HttpResponse("{}",content_type="application/json")
# 		return HttpResponse("{}",content_type="application/json")


class index(TemplateView):
	plantilla="inventario/consulta.html"
	@ventas
	def get(self,request,head,nav,tienda,usu):
		if usu.inventario:
			context={
				"head":head,
				"nav":nav,
				"tienda":tienda,
				"titulo":"inventario",
				"ver_costos":usu.ver_costos,  
				"ver_distribuidor":usu.ver_distribuidor,
				"ver_mayorista":usu.ver_mayorista, 
    			"ver_efectivo":usu.ver_efectivo,
    			"ver_tarjeta":usu.ver_tarjeta,
			}
			return render(request,self.plantilla,context)
		else:
			return redirect("/blocked")