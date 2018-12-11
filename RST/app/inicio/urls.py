
from django.urls import path,include
from .views import index

urlpatterns = [
    path('',index.as_view(),name="index"),
]
