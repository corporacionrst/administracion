from django.contrib import admin

from .models import (
	Marca,
	Producto,
	Lista,
	Combinacion,
	Imagen,
	Detalle,
	TipoDeProducto,
	Codigo,
	Inventario
	)
admin.site.register(Marca)
admin.site.register(Producto)
admin.site.register(Lista)
admin.site.register(Combinacion)
admin.site.register(Codigo)


admin.site.register(Imagen)
admin.site.register(Detalle)
admin.site.register(TipoDeProducto)
admin.site.register(Inventario)

