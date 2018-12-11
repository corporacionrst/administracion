from django.urls import path
from .views import index,orden

urlpatterns = [
    path('',index.as_view(),name="index"),
    path("orden/",orden.as_view(),name="orden")
]
