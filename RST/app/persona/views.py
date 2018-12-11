from django.shortcuts import render,redirect

from django.views.generic import TemplateView
from ..logica.admin import admin
from .forms import PersonaForm

from .models import Persona, Cliente, Proveedor

from ..usuario.models import Usuario
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
import json
from django.contrib import messages

from ..ventas.forms import byNit

class buscar_cliente(TemplateView):
	form = byNit
	def get(self,request,*args,**kwargs):
		usu = Usuario.objects.filter(usuario=request.user)
		if usu.exists():
			usu=usu[0]
			nit=(request.GET['nit']).upper()
			ppl=Persona.objects.filter(nit=nit)
			if ppl.exists():
				ppl=ppl[0]
				pr = Cliente.objects.filter(
					tienda=usu.tienda).filter(
					persona=nit)
				if pr.exists():
					pr=pr.values("persona__nombre","persona__direccion")
					pr=json.dumps(list(pr),cls=DjangoJSONEncoder)
					return HttpResponse(pr,content_type="application/json")
			return HttpResponse("{}",content_type="application/json")
	def post(self,request,*args,**kwargs):
		usu = Usuario.objects.filter(usuario=request.user)
		if usu.exists():
			usu=usu[0]
			if usu.crear_clientes:
				f = self.form(request.POST)
				if f.is_valid():
					nit=(f.cleaned_data['nit_a_registrar']).upper()
					ppl=Persona.objects.filter(nit=nit)
					if ppl.exists():
						ppl=ppl[0]
					else:
						ppl=Persona()
						ppl.nit 		=nit
						ppl.nombre 		=(f.cleaned_data['nombre_a_registrar']).upper()
						ppl.direccion 	=(f.cleaned_data['direccion_a_registrar']).upper()
						ppl.save()
					nombre=ppl.nombre
					pr=Cliente.objects.filter(tienda=usu.tienda).filter(persona=nit)
					if pr.exists():
						messages.error(request,nombre+" Ya existe <button class='btn-primary btn' onclick='usar("+'"'+ppl.nit+'","'+ppl.nombre+'","'+ppl.direccion+'"'+")'>usar</button>")
					else:
						pr=Cliente()
						pr.tienda=usu.tienda
						pr.persona=ppl
						pr.save()
						messages.success(request,nombre+" fue creado exitosamente: <button class='btn-primary btn' onclick='usar("+'"'+ppl.nit+'","'+ppl.nombre+'","'+ppl.direccion+'"'+")'>usar</button>")
				else:
					messages.error(request,"algo salio mal, favor revisar")

			else:
				messages.error(request,"no tienes permitido agregar proveedores nuevos")
		return redirect("/ventas/orden_de_compra/")
	




class buscar_proveedor(TemplateView):
	form = byNit
	def get(self,request,*args,**kwargs):
		usu = Usuario.objects.filter(usuario=request.user)
		if usu.exists():
			usu=usu[0]
			nit=(request.GET['nit']).upper()
			ppl=Persona.objects.filter(nit=nit)
			if ppl.exists():
				ppl=ppl[0]
				pr = Proveedor.objects.filter(
					tienda=usu.tienda).filter(
					persona=nit)
				if pr.exists():
					pr=pr.values("persona__nombre","persona__direccion")
					pr=json.dumps(list(pr),cls=DjangoJSONEncoder)
					return HttpResponse(pr,content_type="application/json")
			return HttpResponse("{}",content_type="application/json")
	def post(self,request,*args,**kwargs):
		usu = Usuario.objects.filter(usuario=request.user)
		if usu.exists():
			usu=usu[0]
			if usu.crear_proveedor:
				f = self.form(request.POST)
				if f.is_valid():
					nit=(f.cleaned_data['nit_a_registrar']).upper()
					ppl=Persona.objects.filter(nit=nit)
					if ppl.exists():
						ppl=ppl[0]
					else:
						ppl=Persona()
						ppl.nit 		=nit
						ppl.nombre 		=(f.cleaned_data['nombre_a_registrar']).upper()
						ppl.direccion 	=(f.cleaned_data['direccion_a_registrar']).upper()
						ppl.save()
					nombre=ppl.nombre
					pr=Proveedor.objects.filter(tienda=usu.tienda).filter(persona=nit)
					if pr.exists():
						messages.error(request,nombre+" Ya existe <button class='btn-primary btn' onclick='usar("+'"'+ppl.nit+'","'+ppl.nombre+'","'+ppl.direccion+'"'+")'>usar</button>")
					else:
						pr=Proveedor()
						pr.tienda=usu.tienda
						pr.persona=ppl
						pr.save()
						messages.success(request,nombre+" fue creado exitosamente: <button class='btn-primary btn' onclick='usar("+'"'+ppl.nit+'","'+ppl.nombre+'","'+ppl.direccion+'"'+")'>usar</button>")
				else:
					messages.error(request,"algo salio mal, favor revisar")

			else:
				messages.error(request,"no tienes permitido agregar proveedores nuevos")
		return redirect("/ventas/orden_de_compra/")
	
		

class proveedor(TemplateView):
	plantilla="main/form.html"
	form = PersonaForm
	initial = {'key': 'value'}
	@admin
	def get(self,request,head,nav,tienda,usu):
		if usu.crear_proveedor:
			context={
				"head":head,
				"nav":nav,
				"form":self.form(initial=self.initial),
				"titulo":"Crear proveedor",
				"ruta":"/admin/persona/proveedor/",
				"accion":"Crear proveedor"
			}
			return render(request,self.plantilla,context)
		else:
			return redirect("/blocked")
	def post(self,request,*args,**kwargs):
		usu = Usuario.objects.filter(usuario=request.user)
		f = self.form(request.POST)
		if usu.exists():
			usu=usu[0]
			if f.is_valid():
				if usu.crear_proveedor:
					nit			= (f.cleaned_data['nit']).upper()
					nombre		= (f.cleaned_data['nombre']).upper()
					direccion 	= (f.cleaned_data['direccion']).upper()
					dias		= (f.cleaned_data['dias'])
					credito 	= (f.cleaned_data['credito'])
					ppl 		= Persona.objects.filter(nit=nit)
					if ppl.exists():
						ppl			  = ppl[0]
					else:
						ppl			  = Persona()
						ppl.nit		  = nit
						ppl.nombre	  = nombre
						ppl.direccion = direccion
						ppl.save()
					pr = Proveedor.objects.filter(persona=ppl).filter(tienda=usu.tienda)
					if pr.exists():
						messages.error(request,nombre+" ya existe")
					else:
						pr 			  = Proveedor()
						pr.persona 	  = ppl
						pr.tienda 	  = usu.tienda
						pr.credito 	  = credito
						pr.dias   	  = dias
						pr.save()
						messages.success(request,nombre+" Agregado exitosamente")
			else:
				messages.error(request,"algo salio mal, favor revisar sus datos")
			return redirect("/admin/persona/clientes/")

		return redirect("/blocked/")



class cliente(TemplateView):
	plantilla="main/form.html"
	form = PersonaForm
	initial = {'key': 'value'}
	@admin
	def get(self,request,head,nav,tienda,usu):
		if usu.crear_usuario:
			context={
				"head":head,
				"nav":nav,
				"form":self.form(initial=self.initial),
				"titulo":"Crear cliente en "+tienda,
				"ruta":"/admin/persona/clientes/",
				"accion":"Crear cliente"
			}
			return render(request,self.plantilla,context)
		else:
			return redirect("/blocked")
	def post(self,request,*args,**kwargs):
		usu = Usuario.objects.filter(usuario=request.user)
		f = self.form(request.POST)
		if usu.exists():
			usu=usu[0]
			if f.is_valid():
				if usu.crear_usuario:
					nit			= (f.cleaned_data['nit']).upper()
					nombre		= (f.cleaned_data['nombre']).upper()
					direccion 	= (f.cleaned_data['direccion']).upper()
					dias		= (f.cleaned_data['dias'])
					credito 	= (f.cleaned_data['credito'])
					ppl 		= Persona.objects.filter(nit=nit)
					if ppl.exists():
						ppl			  = ppl[0]
					else:
						ppl			  = Persona()
						ppl.nit		  = nit
						ppl.nombre	  = nombre
						ppl.direccion = direccion
						ppl.save()
					cl = Cliente.objects.filter(persona=ppl).filter(tienda=usu.tienda)
					if cl.exists():
						messages.error(request,nombre+" ya existe")
					else:
						cl 			  = Cliente()
						cl.persona 	  = ppl
						cl.tienda 	  = usu.tienda
						cl.atiende	  = usu
						cl.credito 	  = credito
						cl.dias   	  = dias
						cl.save()
						messages.success(request,nombre+" Agregado exitosamente")
			else:
				messages.error(request,"algo salio mal, favor revisar sus datos")
			return redirect("/admin/persona/clientes/")

		return redirect("/blocked/")

	

class index(TemplateView):
	plantilla="persona/index.html"
	@admin
	def get(self,request,head,nav,tienda,usu):
		if usu.crear_usuario:
			context={
				"head":head,
				"nav":nav,
				"tienda":tienda,
				
			}
			return render(request,self.plantilla,context)
		else:
			return redirect("/blocked")

class ventas(TemplateView):
	plantilla="persona/historial.html"
	@admin
	def get(self,request,head,nav,tienda,usu):
		if usu.crear_usuario:
			context={
				"head":head,
				"nav":nav,
				"tienda":"en "+tienda,
				"titulo":"Ventas",
				
			}
			return render(request,self.plantilla,context)
		else:
			return redirect("/blocked")
