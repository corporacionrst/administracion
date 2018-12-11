from django.shortcuts import render,redirect

from ..logica.ventas import ventas,ventas2
from .forms import Profile,byNit
from ..usuario.models import Usuario
from ..persona.models import Proveedor,Persona
from .models import Historial,Orden,Venta
from ..producto.producto.models import Codigo,Lista,Producto,Inventario


from django.views.generic import TemplateView
from django.contrib import messages
from django.http import HttpResponse
from decimal import Decimal
from datetime import datetime




class documento(TemplateView):
	plantilla="consulta/documento.html"
	form = Profile
	formulario=byNit
	initial={'key':'value'}
	@ventas2
	def get(self,request,id,head,nav,tienda,usu):
		if usu.facturacion:
			if int(id)>0 and int(id)<5:
				context={
					"pagina":id,
					"head":head,
					"nav":nav,
					"tienda":tienda,
					"titulo":"facturacion",
					"form":self.form(initial=self.initial),
					"formulario":self.formulario(initial=self.initial),
					"ingreso":"agregar cliente",
					"agregar":"/admin/persona/buscar_cliente/",
					"ver_costos":usu.ver_costos,
					"ver_distribuidor":usu.ver_distribuidor,
					"ver_mayorista":usu.ver_mayorista,
					"ver_efectivo":usu.ver_efectivo,
					"ver_tarjeta":usu.ver_tarjeta,
				}
				return render(request,self.plantilla,context)	
		return redirect("/blocked")
	def post(self,request,*args,**kwargs):
		usu=Usuario.objects.filter(usuario=request.user)
		if usu.exists():
			usu=usu[0]
			


class facturacion(TemplateView):
	plantilla="ventas/menu.html"
	form = Profile
	formulario=byNit
	initial={'key':'value'}
	@ventas
	def get(self,request,head,nav,tienda,usu):
		if usu.facturacion:
			context={
				"head":head,
				"nav":nav,
				"tienda":tienda,
				"titulo":"facturacion",
				"form":self.form(initial=self.initial),
				"formulario":self.formulario(initial=self.initial),
			}
			return render(request,self.plantilla,context)
		else:
			return redirect("/blocked")

class remover(TemplateView):
	def post(self,request,*args,**kwargs):
		usu = Usuario.objects.filter(usuario=request.user)
		if usu.exists():
			usu=usu[0]
			prod 		= request.POST["codigo"]
			pagina		= int(request.POST["pagina"])
			documento 	= Venta.objects.filter(
				documento__tienda=usu.tienda).filter(
				documento__usuario=usu).filter(
				autorizacion=False).filter(
				documento__hoja=pagina).last().documento
			valor		= documento.listado.get(id=prod)
			documento.total=documento.total-(valor.cantidad*valor.precio)
			documento.save()
			documento.listado.remove(prod)
			return HttpResponse("Elemento borrado",content_type="text")
		return HttpResponse("Algo sucedio, favor revisar",content_type="text")
		


class quitar(TemplateView):
	def post(self,request,*args,**kwargs):
		usu = Usuario.objects.filter(usuario=request.user)
		if usu.exists():
			usu=usu[0]
			prod 		= request.POST["codigo"]
			documento 	= Orden.objects.filter(
				documento__tienda=usu.tienda).filter(
				documento__usuario=usu).filter(
				enviado=False
				).filter(documento__hoja=0).last().documento
			valor		= documento.listado.get(id=prod)
			documento.total=documento.total-(valor.cantidad*valor.precio)
			documento.save()
			documento.listado.remove(prod)
			return HttpResponse("Elemento borrado",content_type="text")
		return HttpResponse("Algo sucedio, favor revisar",content_type="text")
		

class cargar(TemplateView):
	def post(self,request,*args,**kwargs):
		usu = Usuario.objects.filter(usuario=request.user)
		if usu.exists():
			usu=usu[0]
			pagina 		= int(request.POST["pagina"])
			lista_venta = Venta.objects.filter(
				documento__tienda=usu.tienda).filter(
				documento__usuario=usu).filter(
				autorizacion=False).filter(
				documento__hoja=pagina)
			if lista_venta.exists():
				lista_venta=lista_venta.last()
				his=lista_venta.documento
			else:
				his 			= Historial()
				his.tienda 		= usu.tienda
				his.usuario 	= usu
				his.fecha		= datetime.now()
				his.hoja		= pagina
				his.save()
				lista_venta 			= Venta()
				lista_venta.documento 	= his
				lista_venta.fecha		= datetime.now()
				lista_venta.autoriza 	= usu
				lista_venta.save()
			lista 		= lista_venta.documento.listado
			total 		= lista_venta.documento.total
			prod 		= request.POST["codigo"]
			cantidad 	= request.POST["cantidad"]
			precio 		= request.POST["precio"]
			prod 		= Inventario.objects.get(id=prod).producto
			total=total+Decimal(cantidad)*Decimal(precio)
			his.total=total
			his.save()
			codigo 			= Codigo()
			codigo.producto = prod
			codigo.cantidad = cantidad
			codigo.precio 	= precio
			codigo.save()
			lista.add(codigo)
			return HttpResponse("1",content_type="text")

		


class agregar(TemplateView):
	def post(self,request,*args,**kwargs):
		usu = Usuario.objects.filter(usuario=request.user)
		if usu.exists():
			usu=usu[0]
			orden = Orden.objects.filter(
				documento__tienda=usu.tienda).filter(
				documento__usuario=usu).filter(
				enviado=False).filter(
				documento__hoja=0)
			if orden.exists():
				orden=orden.last()
				his=orden.documento
			else:
				his 			= Historial()
				his.tienda 		= usu.tienda
				his.usuario 	= usu
				his.fecha		= datetime.now()
				his.save()
				orden 			= Orden()
				orden.documento = his
				orden.save()
			lista 		= orden.documento.listado
			total 		= orden.documento.total
			prod 		= request.POST["codigo"]
			cantidad 	= request.POST["cantidad"]
			precio 		= request.POST["precio"]
			prod 		= Lista.objects.get(id=prod)
			total=total+Decimal(cantidad)*Decimal(precio)
			his.total=total
			his.save()
			codigo 			= Codigo()
			codigo.producto = prod
			codigo.cantidad = cantidad
			codigo.precio 	= precio
			codigo.save()
			lista.add(codigo)
			return HttpResponse("1",content_type="text")
		



class orden_de_compra(TemplateView):
	plantilla="consulta/base.html"
	form = Profile
	formulario=byNit
	initial={'key':'value'}
	@ventas
	def get(self,request,head,nav,tienda,usu):
		if usu.orden_de_compra:
			context={
				"head":head,
				"nav":nav,
				"tienda":tienda,
				"titulo":"orden de compra ",
				"form":self.form(initial=self.initial),
				"formulario":self.formulario(initial=self.initial),
				"ingreso":"agregar proveedor",
				"pagina":0,
				"agregar":"/admin/persona/buscar_proveedor/",
			}
			return render(request,self.plantilla,context)
		else:
			return redirect("/blocked")
	def post(self,request,*args,**kwargs):
		usu=Usuario.objects.filter(usuario=request.user)
		if usu.exists():
			usu=usu[0]
			if usu.orden_de_compra:
				oc 	= Orden.objects.filter(
				documento__tienda=usu.tienda).filter(
				documento__usuario=usu).filter(
				enviado=False).filter(
				documento__hoja=0)
				if oc.exists():
					nit=request.POST['nit'].upper()
					persona=Persona.objects.filter(nit=nit)
					if persona.exists():
						persona=persona[0]
						pr=Proveedor.objects.filter(
							persona=persona).filter(
							tienda=usu.tienda)
						if pr.exists():
							oc=oc.last()
							if oc.documento.listado.exists():
								pr=pr[0]
								oc.proveedor=pr
								oc.enviado=True
								oc.save()
								return HttpResponse("1",content_type="text")
							else:
								return HttpResponse("La lista parece estar vacia, favor verificar",content_type="text")
						else:
							return HttpResponse("El proveedor al parecer no existe",content_type="text")
					else:
						return HttpResponse("El nit al parecer no existe",content_type="text")
				else:

					return HttpResponse("la orden parece no existir",content_type="text")
		return HttpResponse("No tienes permiso para ejecutar esta accion",content_type="text")


class index(TemplateView):
	plantilla="main/inicio.html"
	@ventas
	def get(self,request,head,nav,tienda,usu):
		context={
			"head":head,
			"nav":nav,
			"tienda":tienda,

		}
		return render(request,self.plantilla,context)
		