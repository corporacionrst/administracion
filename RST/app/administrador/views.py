from django.shortcuts import render,redirect

from ..logica.admin import admin
from django.views.generic import TemplateView
from ..usuario.forms import TiendaForm
from django.contrib import messages

class tiendas(TemplateView):
	plantilla="main/form.html"
	form = TiendaForm
	initial={'key':'value'}
	@admin
	def get(self,request,head,nav,tienda,usu):
		if request.user.is_staff:
			context={
				"head":head,
				"nav":nav,
				"form":self.form(initial=self.initial),
				"titulo":"Tiendas",
				"ruta":"/admin/tiendas/",
				"accion":"crear tiendas"
			}
			return render(request,self.plantilla,context)
		else:
			return redirect("/blocked")
	def post(self,request,*args,**kwargs):
		formU = self.form(request.POST)
		if request.user.is_staff:
			if formU.is_valid():
				formU.save()
				name=formU.cleaned_data['nombre']
				messages.success(request,name+" fue creado satifactoriamente")
			else:
				messages.error(request,formU.errors)
			return redirect("/admin/tiendas/")



class index(TemplateView):
	plantilla="main/inicio.html"
	@admin
	def get(self,request,head,nav,tienda,usu):
		context={
			"head":head,
			"nav":nav,
			"tienda":tienda,
			"titulo":"Crear usuario en "+tienda,
			"ruta":"/admin/usuario/agregar/",
			"accion":"Crear usuario"
		}
		return render(request,self.plantilla,context)