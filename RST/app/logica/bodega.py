
from django.shortcuts import render,redirect
from ..usuario.models import Usuario
from .head import head


def bodega(func):
	@head
	def menu(self,request,head,tienda):
		usu = Usuario.objects.filter(usuario=request.user)
		if usu.exists():
			nav=""
			usu=usu[0]
			if usu.crear_marca or usu.crear_producto or usu.combinar_productos:
				nav+='<li><a href="#"><i class="fa fa-plus fa-fw"></i>Producto<span class="fa arrow"></span></a><ul class="nav nav-second-level">'
				if usu.crear_producto:
					nav+='<li><a href="/bodega/producto/#"><i class="fa fa-cog fa-fw"></i>Producto</a></li>'
				if usu.crear_marca:
					nav+='<li><a href="/bodega/producto/marca/"><i class="fa fa-copyright fa-fw"></i> Marca</a></li>'
				if usu.combinar_productos:
					nav+='<li><a href="/bodega/producto/combinar"><i class="fa fa-cogs fa-fw"></i>Combinar</a></li>'	
				nav+='</ul></li>'
			
			if usu.cargar_compra:
				nav+='<li><a href="/bodega/producto/cargar_compra"><i class="fa fa-download fa-fw"></i>compra</a></li>'
			if usu.autorizar_traslados or usu.solicitar_traslados:
				nav+='<li><a href="#"><i class="fa fa-truck fa-fw"></i>Traslados<span class="fa arrow"></span></a><ul class="nav nav-second-level">'
				if usu.solicitar_traslados:
					nav+='<li><a href="/bodega/traslados/solicitar"><i class="fa fa-gift fa-fw"></i>Solicitar</a></li>'
				if usu.autorizar_traslados:
					nav+='<li><a href="/bodega/traslados/autorizar"><i class="fa fa-heart fa-fw"></i>Autorizar</a></li>'
				if usu.listar_traslados:
					nav+='<li><a href="/bodega/traslados/listar"><i class="fa fa-list fa-fw"></i>Listar</a></li>'
				
			return func(self,request,head,nav,tienda,usu)
		return render(request,"index/index.html")
	return menu

