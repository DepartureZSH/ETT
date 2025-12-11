from django.urls import re_path
from .MARL.consumers import TrainingConsumer

websocket_urlpatterns = [
    re_path(r"ws/train/$", TrainingConsumer.as_asgi()),
]