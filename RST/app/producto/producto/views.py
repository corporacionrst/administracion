from django.shortcuts import render,redirect


from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
import json


from ...logica.bodega import bodega
from django.views.generic import TemplateView
from django.contrib import messages
from .forms import MarcaForm,ProductoForm

from .models import Marca,Producto,Lista,Combinacion,Inventario
from ...usuario.models import Usuario

class stock(TemplateView):
	def get(self,request,*args,**kwargs):
		usu = Usuario.objects.filter(usuario=request.user)
		if usu.exists():
			usu=usu[0]
			pag=int(request.GET['pag'])*10
			query=request.GET['codigo']
			p = Inventario.objects.filter(producto__producto__codigo__icontains=query).filter(tienda=usu.tienda)[pag:pag+10]
			if p.exists():
				p=p.values("producto__id","producto__producto__codigo","producto__producto__descripcion","producto__producto__marca__nombre","id","cantidad","costo",
					"distribuidor","mayorista","efectivo","tarjeta")
				p=json.dumps(list(p),cls=DjangoJSONEncoder)
				return HttpResponse(p,content_type="application/json")

class combinacion(TemplateView):
	def get(self,request,*args,**kwargs):
		usu = Usuario.objects.filter(usuario=request.user)
		if usu.exists():
			usu=usu[0]
			if usu.combinar_productos:
				query = request.GET['codigo']
				p     = Lista.objects.get(id=query)
				p     = p.combinacion
				p     = p.values("producto__codigo","producto__descripcion","producto__marca__nombre","cantidad","id")
				p     = json.dumps(list(p),cls=DjangoJSONEncoder)
				return HttpResponse(p,content_type="application/json")
	def post(self,request,*args,**kwargs):
		usu = Usuario.objects.filter(usuario=request.user)
		if usu.exists():
			usu=usu[0]
			if usu.combinar_productos:
				principal 			 = request.POST['principal']
				cantidad  			 = request.POST['cantidad']
				query    			 = request.POST['codigo']
				p         			 = Lista.objects.get(id=principal).combinacion
				combinacion 		 = Combinacion()
				pr 					 = Producto.objects.get(id=query)
				combinacion.producto = pr
				combinacion.cantidad = cantidad
				combinado 			 = Combinacion.objects.filter(producto=pr).filter(cantidad=cantidad)
				if not combinado.exists():
					combinacion.save()
				else:
					combinacion=combinado[0]
				p.add(combinacion)
				return HttpResponse("1",content_type="text")
		return HttpResponse("Error re permisos, favor revisar",content_type="text")





class consulta(TemplateView):
	def get(self,request,*args,**kwargs):
		usu = Usuario.objects.filter(usuario=request.user)
		if usu.exists():
			pag=int(request.GET['pag'])*10
			query=request.GET['codigo']
			p = Lista.objects.filter(producto__codigo__icontains=query)[pag:pag+10]
			if p.exists():
				p=p.values("producto__codigo","producto__descripcion","producto__marca__nombre","id")
				p=json.dumps(list(p),cls=DjangoJSONEncoder)
				return HttpResponse(p,content_type="application/json")
			


class buscar(TemplateView):
	def get(self,request,*args,**kwargs):
		usu = Usuario.objects.filter(usuario=request.user)
		if usu.exists():
			pag=int(request.GET['pag'])*10
			usu=usu[0]
			c = Compras.objects.filter(owner=usu.owner).filter(tienda=usu.tienda).filter(ingresa=request.user).filter(abierto=True)
			if c.exists():
				c=c[0]
				t='total:'+str(c.total)
				c=c.lista_productos.all()[pag:pag+10]
				c=c.annotate(total=F("cantidad")*F("unitario"))
				c=c.values("cantidad","producto__producto__codigo","producto__producto__descripcion","unitario","producto__producto__marca__nombre","id","total")
				c=list(c)
				c.append(t)
				c=json.dumps(c,cls=DjangoJSONEncoder)
				return HttpResponse(c,content_type="application/json")
		return HttpResponse("{}",content_type="application/json")


class combinar(TemplateView):
	plantilla="bodega/producto/combinar.html"
	form = ProductoForm
	initial= {'key':'value'}
	@bodega
	def get(self,request,head,nav,tienda,usu):
		if usu.combinar_productos: 
			context={
				"head":head,
				"nav":nav,
				"tienda":tienda,
				"form":self.form(initial=self.initial),
				"titulo":"Combinar",
			}
			return render(request,self.plantilla,context)
		else:
			return redirect("/blocked")
	def post(self,request,*args,**kwargs):
		usu = Usuario.objects.filter(usuario=request.user)
		if usu.exists():
			usu=usu[0]
			if usu.combinar_productos:
				principal 			 = request.POST['principal']
				query    			 = request.POST['codigo']
				p         			 = Lista.objects.get(id=principal).combinacion
				p.remove(query)
				return HttpResponse("1",content_type="text")
		return HttpResponse("Error re permisos, favor revisar",content_type="text")






class producto(TemplateView):
	plantilla="main/form.html"
	form = ProductoForm
	initial= {'key':'value'}
	@bodega
	def get(self,request,head,nav,tienda,usu):
		if usu.crear_marca: 
			context={
				"head":head,
				"nav":nav,
				"tienda":tienda,
				"form":self.form(initial=self.initial),
				"titulo":"Productos",
				"ruta":"/bodega/producto/crear/",
				"accion":"Crear nuevo producto"
			}
			return render(request,self.plantilla,context)
		else:
			return redirect("/blocked")
	def post(self,request,*args,**kwargs):
		formU = self.form(request.POST)
		if formU.is_valid():
			codigo=formU.cleaned_data['codigo'].upper()
			producto = Producto.objects.filter(codigo=codigo,marca=formU.cleaned_data['marca'])
			if producto.exists():
				messages.error(request,"el codigo "+codigo+" ya existe")
			else:
				producto 				= Producto()
				producto.codigo 		= codigo
				producto.descripcion	= formU.cleaned_data['descripcion'].upper()
				producto.marca 			= formU.cleaned_data['marca'] 
				producto.save()
				lista 					= Lista()
				lista.producto          = producto
				lista.save()
				messages.success(request,codigo+" fue creado satifactoriamente")
		else:
			messages.error(request,formU.errors)
		return redirect("/bodega/producto/crear/")


class marca(TemplateView):
	plantilla="main/form.html"
	form = MarcaForm
	initial= {'key':'value'}
	@bodega
	def get(self,request,head,nav,tienda,usu):
		if usu.crear_marca: 
			context={
				"head":head,
				"nav":nav,
				"tienda":tienda,
				"form":self.form(initial=self.initial),
				"titulo":"Crear marcas",
				"ruta":"/bodega/producto/marca/",
				"accion":"Crear nueva marca"
			}
			return render(request,self.plantilla,context)
		else:
			return redirect("/blocked")
	def post(self,request,*args,**kwargs):
		formU = self.form(request.POST)
		if formU.is_valid():
			name=formU.cleaned_data['nombre'].upper()
			brand = Marca.objects.filter(nombre=name)
			if brand.exists():
				messages.error(request,name+" ya existe")
			else:
				brand=Marca()
				brand.nombre=name
				brand.save()
				messages.success(request,name+" fue creado satifactoriamente")
		else:
			messages.error(request,formU.errors)
		return redirect("/bodega/producto/marca/")

class index(TemplateView):
	plantilla="bodega/producto/inicio.html"
	@bodega
	def get(self,request,head,nav,tienda,usu):
		if usu.crear_marca: 
			context={
				"head":head,
				"nav":nav,
				"tienda":tienda,
				"marca":usu.crear_marca,
				"productos":usu.crear_producto,
				"combinacion":True,
				"inv":True,
			}
			return render(request,self.plantilla,context)
		else:
			return redirect("/blocked")