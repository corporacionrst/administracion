from django.urls import path,include
from .views import index,agregar

urlpatterns = [
    path('',index.as_view(),name="index"),
    path('agregar/',agregar.as_view(),name="agregar"),
]
