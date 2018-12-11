
from django.shortcuts import render,redirect
from ..usuario.models import Usuario
from .head import head


def admin(func):
	@head
	def menu(self,request,head,tienda):
		usu = Usuario.objects.filter(usuario=request.user)
		if usu.exists():
			nav=""
			usu=usu[0]
			if usu.crear_usuario:
				nav+='<li><a href="/admin/usuario/"><i class="fa fa-sitemap fa-fw"></i> Usuarios</a></li>'
			if usu.historial_clientes or usu.crear_clientes or usu.modificar_clientes or usu.crear_proveedor:
				nav+='<li><a href="#"><i class="fa fa-bookmark fa-fw"></i>Historial<span class="fa arrow"></span></a><ul class="nav nav-second-level">'
				nav+='<li><a href="/admin/persona/"><i class="fa fa-users fa-fw"></i>ver</a></li>'
				if usu.crear_clientes or usu.modificar_clientes or usu.historial_clientes:
					nav+='<li><a href="/admin/persona/clientes"><i class="fa fa-user fa-fw"></i>cliente</a></li>'
				if usu.crear_proveedor:
					nav+='<li><a href="/admin/persona/proveedor"><i class="fa fa-tasks fa-fw"></i>proveedor</a></li>'

				nav+='</ul></li>'

			if usu.autorizar_orden:
				nav+='<li><a href="#"><i class="fa fa-check fa-fw"></i>Autorizar<span class="fa arrow"></span></a><ul class="nav nav-second-level">'
				if usu.autorizar_orden:
					nav+='<li><a href="/admin/autorizar/orden"><i class="fa fa-pencil fa-fw"></i>orden de compra</a></li>'
				nav+='</ul></li>'

				
			# nav+=' <li><a href="#"><i class="fa fa-star fa-fw"></i> Autorizar<span class="fa arrow"></span></a><ul class="nav nav-second-level">'
			# if usu.autorizar_permisos:
			# 	nav+='<li><a href="/permisos/autorizar"><i class="fa fa-align-left" aria-hidden="true"></i> Permisos</a></li>'
			# if usu.autorizar_cheques:
			# 	nav+='<li><a href="/cheques/autorizar"><i class="fa fa-share fa-fw"></i> Cheques</a></li>'
			# if usu.autoriza_prestamos:
			# 	nav+='<li><a href="/prestamos/autorizar/"><i class="fa fa-align-justify" aria-hidden="true"></i></i> Prestamos</a></li>'
			# if usu.autoriza_ordenes:
			# 	nav+='<li><a href="/ventas/oc_autorizar/"><i class="fa fa-thumbs-up" aria-hidden="true"></i></i> Orden de compra</a></li>'
			# nav+='</ul></li>'
			# if usu.ingresa_gastos:
			# 	nav+='<li><a href="/admin/gastos/"><i class="fa fa-lock" aria-hidden="true"></i> Gastos fijos</a></li>'
			# if usu.rendimiento_tienda:
			# 	nav+='<li><a href="/admin/rendimiento"><i class="fa fa-bar-chart" aria-hidden="true"></i></i> rendimiento de la tienda</a></li>'
			# if usu.agregar_clientes_credito or usu.agregar_clientes_contado or usu.historial_de_clientes:
			# 	nav+='<li><a href="/admin/clientes"><i class="fa fa-users" aria-hidden="true"></i></i> clientes</a></li>'
			
			# if usu.agregar_proveedores_contado or usu.agregar_proveedores_credito or usu.historial_proveedor:
			# 	nav+='<li><a href="/admin/proveedor"><i class="fa fa-cube" aria-hidden="true"></i></i> Proveedor</a></li>'
			
			# if usu.historial_de_clientes:
				
			return func(self,request,head,nav,tienda,usu)
		return render(request,"index/index.html")
	return menu

