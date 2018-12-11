from django.conf.urls import url

from . import consumers


websocket_urlpatterns = [
    url(r'^ws/alertas/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
    url(r'^ws/alertas/$', consumers.alertas),
]