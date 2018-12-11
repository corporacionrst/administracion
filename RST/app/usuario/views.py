from django.shortcuts import render,redirect

from ..logica.admin import admin
# Create your views here.
from django.views.generic import TemplateView
from .models import Usuario
from .forms import UsuarioForm
from django.contrib import messages

class agregar(TemplateView):
	plantilla="main/form.html"
	form = UsuarioForm
	initial = {'key': 'value'}
	@admin
	def get(self,request,head,nav,tienda,usu):
		if usu.crear_usuario:
			context={
				"head":head,
				"nav":nav,
				"form":self.form(initial=self.initial),
				"titulo":"Crear usuario en "+tienda,
				"ruta":"/admin/usuario/agregar/",
				"accion":"Crear usuario"
			}
			return render(request,self.plantilla,context)
		else:
			return redirect("/blocked")
	def post(self,request,*args,**kwargs):
		formU = self.form(request.POST)
		perfil=Usuario.objects.get(usuario=request.user)
		if perfil.crear_usuario and formU.is_valid():
			usu=Usuario()
			instance = formU.save(commit=False)
			instance.save()	
			nombre					= formU.cleaned_data['nombre']
			usu.usuario				= instance
			usu.nombre	   			= formU.cleaned_data['nombre']
			usu.nombre     			= nombre
			usu.apellido   			= formU.cleaned_data['apellido']
			usu.telefono 			= formU.cleaned_data['telefono']
			usu.tienda  	    	= perfil.tienda
			usu.email    			= formU.cleaned_data['email']
			usu.birthday			= formU.cleaned_data['fecha_de_nacimiento']
			usu.fecha_ingreso   	= formU.cleaned_data['fecha_ingreso']
			usu.cui     	  		= formU.cleaned_data['cui']
			# ------------inicia lista de caracteristicas------------
			# Ver precios
			usu.ver_costos			= formU.cleaned_data["ver_costos"]
			usu.ver_distribuidor	= formU.cleaned_data["ver_distribuidor"]
			usu.ver_mayorista		= formU.cleaned_data["ver_mayorista"]
			usu.ver_efectivo		= formU.cleaned_data["ver_efectivo"]
			usu.ver_tarjeta			= formU.cleaned_data["ver_tarjeta"]


			# Administrador
			usu.crear_usuario		= formU.cleaned_data['crear_usuario']
			usu.crear_clientes		= formU.cleaned_data['crear_clientes']
			usu.modificar_clientes	= formU.cleaned_data['modificar_clientes']
			usu.historial_clientes	= formU.cleaned_data['historial_clientes']
			usu.crear_proveedor		= formU.cleaned_data['crear_proveedor']
			usu.autorizar_orden		= formU.cleaned_data['autorizar_orden']
			# Bodega
			usu.crear_marca			= formU.cleaned_data['crear_marca']
			usu.crear_producto		= formU.cleaned_data['crear_producto']
			usu.combinar_productos  = formU.cleaned_data['crear_producto']
			usu.cargar_compra		= formU.cleaned_data['cargar_compra']
			usu.solicitar_traslados	= formU.cleaned_data['solicitar_traslados']
			usu.autorizar_traslados = formU.cleaned_data['autorizar_traslados']
			usu.listar_traslados	= formU.cleaned_data['listar_traslados']
			# Ventas

			usu.orden_de_compra		= formU.cleaned_data['orden_de_compra']
			usu.inventario 			= formU.cleaned_data['inventario']
			usu.facturacion			= formU.cleaned_data['facturacion']
			usu.save()
			# --------------------fin de la lista--------------------
			messages.success(request,nombre+" fue creado satifactoriamente")
			
		else:
			messages.error(request,"algo salio mal, favor verifique")
		return redirect("/admin/usuario/agregar/")

		

class index(TemplateView):
	plantilla="administrador/usuario/index.html"
	@admin
	def get(self,request,head,nav,tienda,usu):
		usuarios = Usuario.objects.filter(tienda=usu.tienda)
		print (usuarios)
		context={
			"head":head,
			"nav":nav,
			"tienda":tienda,
			"usuarios":usuarios
		}
		return render(request,self.plantilla,context)