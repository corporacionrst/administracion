from django.shortcuts import render,redirect,HttpResponse, get_object_or_404,Http404


# Create your views here.

from django.views import View
from django.views.generic import TemplateView

from ..logica.bodega import bodega
from ..usuario.models import Tienda,Usuario
from ..producto.producto.models import Codigo,Lista
from .models import Traslados
from ..producto.producto.models import Inventario,Producto
from django.contrib import messages

from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
import json
from datetime import datetime
from ..usuario.models import Usuario
from .require import renderPDF

from .tasks import autorizar_traslado

class listar(TemplateView):
	plantilla="bodega/traslados/listar.html"
	@bodega
	def get(self,request,head,nav,tienda,usu):
		tiendas = Tienda.objects.all().exclude(id=usu.tienda.id)
		context={
			"titulo":"Solicitar traslado",
			"head":head,
			"nav":nav,
			"tienda":tienda,
			"tiendas":tiendas
		}
		return render(request,self.plantilla,context)


class pdf(View):
	def get(self,request,id):
		usu=Usuario.objects.filter(usuario=request.user)
		if usu.exists():
			usu=usu[0]
			try:
				query=get_object_or_404(Traslados,id=id)
				lista=query.lista.all()
				if query.despacha==None:
					query.despacha=usu
					query.save()
			except:
				query=None
				Http404('pdf no generado')
			context={
				"tipo":"Traslado",
				"numero":id,
				"documento":query,
				"lista":lista,
				"size":range(10-lista.count())
			}
			article_pdf=renderPDF('pdf/pdf.html',context)
		else:
			article_pdf=""
		return HttpResponse(article_pdf,content_type='application/pdf')



class autorizar(TemplateView):
	plantilla="bodega/traslados/autorizar.html"
	@bodega
	def get(self,request,head,nav,tienda,usu):
		tiendas = Tienda.objects.all().exclude(id=usu.tienda.id)
		if usu.solicitar_traslados:
			tr = Traslados.objects.filter(
				tienda_recibe=usu.tienda).filter(
				enviada=True).filter(
				despacha=None)
			context={
				"traslados":tr,
				"titulo":"Solicitar traslado",
				"head":head,
				"nav":nav,
				"tienda":tienda,
				"tiendas":tiendas
			}
			return render(request,self.plantilla,context)
		return redirect("/blocked")
	def post(self,request,*args,**kwargs):
		usu = Usuario.objects.filter(usuario=request.user)
		if usu.exists():
			usu=usu[0]
			if usu.autorizar_traslados:
				id_traslado = int(request.POST["traslado"])
				traslado = Traslados.objects.get(id=id_traslado)
				if traslado.despacha==None:
					traslado.despacha=usu
					traslado.save()
					autorizar_traslado.delay(id_traslado)
				return HttpResponse("impreso",content_type="text")


	

class quitar(TemplateView):
	def post(self,request,*args,**kwargs):
		usu = Usuario.objects.filter(usuario=request.user)
		if usu.exists():
			usu=usu[0]
			store    = Tienda.objects.get(id=int(request.POST['tienda']))
			producto = int(request.POST['producto'])
			t = Traslados.objects.filter(
				tienda_solicita=usu.tienda).filter(
				tienda_recibe=store).filter(
				solicita=usu).filter(
				enviada=False).last()
			codigo=Codigo.objects.get(id=producto)
			t.lista.remove(codigo)
			return HttpResponse("1",content_type="text")



class stock(TemplateView):
	@bodega
	def get(self,request,head,nav,tienda,usu):
		pag=int(request.GET['pag'])*10
		tienda=int(request.GET['tienda'])
		tienda=Tienda.objects.get(id=tienda)
		query=request.GET['codigo']
		inventario = Inventario.objects.filter(
			producto__producto__codigo__icontains=query).filter(
			tienda=tienda)[pag:pag+10]
		if inventario.exists():
			inventario=inventario.values("producto__id","producto__producto__codigo","producto__producto__descripcion","producto__producto__marca__nombre","id","cantidad","costo",
				"distribuidor","mayorista","efectivo","tarjeta")
			inventario=json.dumps(list(inventario),cls=DjangoJSONEncoder)
			return HttpResponse(inventario,content_type="application/json")

class agregar(TemplateView):
	def post(self,request,*args,**kwargs):
		usu = Usuario.objects.filter(usuario=request.user)
		if usu.exists():
			usu=usu[0]
			store    = Tienda.objects.get(id=int(request.POST['tienda']))
			producto = int(request.POST['producto'])
			cantidad = int(request.POST['cantidad'])
			precio 	 = request.POST['precio']
			t = Traslados.objects.filter(
				tienda_solicita=usu.tienda).filter(
				tienda_recibe=store).filter(
				solicita=usu).filter(
				enviada=False)
			if t.exists():
				t = t.last()
			else:
				t = Traslados()
				t.tienda_solicita=usu.tienda
				t.fecha=datetime.now()
				t.tienda_recibe=store
				t.solicita=usu
				t.save()
			
			lista 		 	= Lista.objects.get(id=producto)
			codigo 			= Codigo()
			codigo.producto = lista
			codigo.cantidad = cantidad
			codigo.precio  	= precio
			codigo.save()
			t.lista.add(codigo)
			return HttpResponse("1",content_type="text")



class tienda(TemplateView):
	@bodega
	def get(self,request,head,nav,tienda,usu):
		if usu.solicitar_traslados:
			tienda 	= request.GET['tienda']
			pag		= int(request.GET["pag"])*10
			tienda  = Tienda.objects.get(id=tienda)
			t = Traslados.objects.filter(
				tienda_solicita=usu.tienda).filter(
				tienda_recibe=tienda).filter(
				solicita=usu).filter(
				enviada=False)
			if t.exists():
				t.last()
				t=t.values(
					"lista__producto__producto__codigo",
					"lista__producto__producto__descripcion",
					"lista__producto__producto__marca__nombre",
					"lista__cantidad",
					"lista__precio",
					"lista__id"
					)
				t=json.dumps(list(t),cls=DjangoJSONEncoder)
				
				return HttpResponse(t,content_type="application/json")
		return HttpResponse("{}",content_type="application/json")


class solicitar(TemplateView):
	plantilla="bodega/traslados/solicitar.html"
	@bodega
	def get(self,request,head,nav,tienda,usu):
		tiendas = Tienda.objects.all().exclude(id=usu.tienda.id)
		if usu.solicitar_traslados:
			context={
				"titulo":"Solicitar traslado",
				"head":head,
				"nav":nav,
				"tienda":tienda,
				"tiendas":tiendas
			}
			return render(request,self.plantilla,context)
		return redirect("/blocked")
	def post(self,request,*args,**kwargs):
		usu = Usuario.objects.filter(usuario=request.user)
		if usu.exists():
			usu=usu[0]
			if usu.solicitar_traslados:
				store    = Tienda.objects.get(id=int(request.POST['tienda']))
				t = Traslados.objects.filter(
					tienda_solicita=usu.tienda).filter(
					tienda_recibe=store).filter(
					solicita=usu).filter(
					enviada=False)
				if t.exists():
					t = t.last()
					if t.lista.count()>0:
						t.enviada=True
						t.save()
						messages.success(request,"La solicitud fue realizada satisfactoriamente.")
						return HttpResponse("1",content_type="text")
					else:
						return HttpResponse("La lista parece estar vacia",content_type="text")
				else:
					return HttpResponse("El documento no ha sido creado")
			return HttpResponse("no tienes habilitada esta opcion",content_type="text")
