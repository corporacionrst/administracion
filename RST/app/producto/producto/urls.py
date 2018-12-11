from django.urls import path,include
from .views import index,marca,producto,combinar,consulta,combinacion,stock

urlpatterns = [
    path('',index.as_view(),name="index"),
    path('marca/',marca.as_view(),name="marca"),
    path('crear/',producto.as_view(),name="producto"),
    path('combinar/',combinar.as_view(),name="combinar"),
    path('consulta/',consulta.as_view(),name="consulta"),
    path('combinacion/',combinacion.as_view(),name="combinacion"),
    path('bodega/',stock.as_view(),name="stock"),
]
