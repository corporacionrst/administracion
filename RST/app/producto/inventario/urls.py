from django.urls import path,include
from .views import index,compra,venta

urlpatterns = [
    path('',index.as_view(),name="index"),
    path("compra/",compra.as_view(),name="compra"),
    path("venta/",venta.as_view(),name="venta")
]
