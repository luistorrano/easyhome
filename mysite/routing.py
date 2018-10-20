
# chat/routing.py
from django.conf.urls import url

from . import consumers
from . import views

websocket_urlpatterns = [
    url(r'^ws/chat/(?P<room_name>[^/]+)/$', views.ChatConsumer),
]
