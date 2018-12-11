
from django.shortcuts import render,redirect
from ..usuario.models import Usuario
from .head import head,head2


def ventas(func):
	@head
	def menu(self,request,head,tienda):
		usu = Usuario.objects.filter(usuario=request.user)
		if usu.exists():
			usu=usu[0]
			nav=ventas_bar(usu)
			return func(self,request,head,nav,tienda,usu)
		return render(request,"index/index.html")
	return menu


def ventas2(func):
	@head2
	def menu(self,request,id,head,tienda):
		usu = Usuario.objects.filter(usuario=request.user)
		if usu.exists():
			usu=usu[0]
			nav=ventas_bar(usu)
			return func(self,request,id,head,nav,tienda,usu)
		return render(request,"index/index.html")
	return menu

def ventas_bar(usu):
	nav=""
	if usu.inventario:
		nav+='<li><a href="/inventario"><i class="fa fa-barcode fa-fw"></i>Inventario</a></li>'
	if usu.orden_de_compra:
		nav+='<li><a href="/ventas/orden_de_compra"><i class="fa fa-pencil fa-fw"></i>Orden de compra</a></li>'
	if usu.facturacion:
		nav+='<li><a href="/ventas/facturacion"><i class="fa fa-print fa-fw"></i>facturacion</a></li>'
	return nav
