# marlapp/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class TrainingConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        print("connect")
        await self.channel_layer.group_add("train_channel", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        print("disconnect")
        await self.channel_layer.group_discard("train_channel", self.channel_name)

    async def send_log(self, event):
        print("send_log")
        await self.send(text_data=json.dumps(event["data"]))
