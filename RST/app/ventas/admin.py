from django.contrib import admin

from .models import Historial,Orden,Compra,Venta


admin.site.register(Historial)
admin.site.register(Orden)
admin.site.register(Compra)
admin.site.register(Venta)