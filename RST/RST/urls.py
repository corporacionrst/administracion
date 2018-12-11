from django.conf import settings
from django.urls import path,include
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
	path('alertas/',include('app.alertas.urls')),
    path('admin_punto_php/', admin.site.urls),
    path('admin/',include('app.administrador.urls')),
    path('bodega/',include('app.bodega.urls')),
    path('inventario/',include('app.producto.inventario.urls')),
    path('persona/',include('app.persona.urls')),
    path('ventas/',include('app.ventas.urls')),
    path('',include('app.inicio.urls')),
]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT,show_indexes=True)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT,show_indexes=True)
