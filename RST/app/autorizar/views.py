from django.shortcuts import render,redirect

from django.views.generic import TemplateView
from datetime import date, timedelta

from ..usuario.models import Usuario

from ..logica.admin import admin
from ..ventas.models import Orden
from django.http import HttpResponse
from .tasks import cargar_al_inventario

class orden(TemplateView):
	plantilla="administrador/autorizar/orden.html"
	@admin
	def get(self,request,head,nav,tienda,usu):
		if usu.autorizar_orden:
			limite = date.today() - timedelta(5)
			orden    = Orden.objects.filter(
				autoriza=None).filter(
				enviado=True).filter(
				documento__fecha__gte=limite)
			context={
				"head":head,
				"nav":nav,
				"tienda":tienda,
				"orden":orden,

			}
			return render(request,self.plantilla,context)
		else:
			return redirect("/blocked")
	def post(self,request,*args,**kwargs):
		usu = Usuario.objects.filter(usuario=request.user)
		if usu.exists():
			usu=usu[0]
			doc 	= request.POST["doc"]
			motivo 	= request.POST["motivo"]
			si 		= request.POST["si"]
			orden 	= Orden.objects.get(id=doc)
			orden.autoriza 	 	= usu
			orden.descripcion	= motivo
			if si=="si":
				orden.autorizacion 	= True
				cargar_al_inventario.delay(orden.documento.id)
			orden.save()
			return HttpResponse(usu.nombre,content_type="text")
		else:
			return HttpResponse("Algo sucedio, favor revisar",content_type="text")
		
class index(TemplateView):
	plantilla="administrador/autorizar/index.html"
	@admin
	def get(self,request,head,nav,tienda,usu):
		context={
			"head":head,
			"nav":nav,
			"tienda":tienda,
			"orden":usu.autorizar_orden
		}
		return render(request,self.plantilla,context)