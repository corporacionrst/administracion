from django.shortcuts import redirect
from ..usuario.models import Usuario

def head(func):
	def menu(self,request):
		if request.user.is_authenticated:
			nav=""
			usu = Usuario.objects.filter(usuario=request.user)
			if usu.exists():
				usu=usu[0]
				tienda=usu.tienda.nombre
				nav=navbar(usu)
			return func(self,request,nav,tienda)
		return redirect("/blocked")

	return menu


def head2(func):
	def menu(self,request,id=None):
		if request.user.is_authenticated:
			nav=""
			usu = Usuario.objects.filter(usuario=request.user)
			if usu.exists():
				usu=usu[0]
				tienda=usu.tienda.nombre
				nav=navbar(usu)
			return func(self,request,id,nav,tienda)
		return redirect("/blocked")

	return menu


def navbar(usu):
	# ADMIN
	if usu.autorizar_orden or usu.crear_usuario or usu.crear_clientes or usu.historial_clientes or usu.modificar_clientes or usu.crear_proveedor:
		nav='<li><a href="/admin"><i class="fa fa-bank fa-fw"></i>admin</a></li>'
	# # link a conta
	# if usu.cuentas_por_cobrar or usu.cuentas_por_pagar or usu.historial_de_ventas or usu.historial_de_compras or usu.impuestos:
	# 	nav+='<li><a href="/conta"><i class="fa fa-check-square-o fa-fw"></i>contabilidad</a></li>'
	# # link a ventas
	if usu.orden_de_compra or usu.inventario or usu.facturacion:
	 # or usu.generar_proforma or usu.generar_facturas or usu.agregar_clientes_contado or usu.solicitar_orden_de_compra or usu.ingresar_solicitud_de_credito or usu.solicitar_envios_de_productos or usu.modifica_descripcion_de_la_factura or usu.historial_de_productos or usu.historial_de_clientes:
		nav+='<li><a href="/ventas"><i class="fa fa-shopping-cart fa-fw"></i>ventas</a></li>'
	# BODEGA
	if usu.listar_traslados or usu.autorizar_traslados or usu.solicitar_traslados or usu.crear_marca or usu.crear_producto or usu.combinar_productos or usu.cargar_compra :
		nav+='<li><a href="/bodega"><i class="fa fa-cloud-download fa-fw"></i>bodega</a></li>'
	# # link a caja
	# if usu.generar_contrasena or usu.recibos_de_pago or usu.imprimir_facturas:
	# 	nav+='<li><a href="/caja"><i class="fa fa-credit-card fa-fw"></i>caja</a></li>'
	# # multitienda
	# if usu.multitienda:
	# 	nav+='<li><a href="/tienda"><i class="fa fa-shopping-cart fa-fw"></i>tienda</a></li>'
	return nav

