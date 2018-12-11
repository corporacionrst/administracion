from django.urls import path
from .views import traslado

urlpatterns = [

    # path('index/',index.as_view(),name="index"),
    path('traslado/',traslado.as_view(),name="traslado")
]
