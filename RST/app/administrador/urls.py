from django.urls import path,include
from .views import index,tiendas

urlpatterns = [
    path('',index.as_view(),name="index"),
    path('usuario/',include('app.usuario.urls')),
    path('tiendas/',tiendas.as_view(),name="tiendas"),
    path('persona/',include('app.persona.urls')),
    path('autorizar/',include('app.autorizar.urls')),
]
