from django.urls import re_path

from . import relay

websocket_urlpatterns = [
    re_path(r'ws/submit/', relay.DraftPick.as_asgi()),
]