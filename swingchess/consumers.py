from channels.generic.websocket import AsyncWebsocketConsumer
import json


class ChessConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, code):
        pass

    async def receive(self, text_data=None, bytes_data=None):
        await self.send(text_data=text_data, bytes_data=bytes_data)
        text_data_jason = json.loads(text_data)
        message = text_data_jason['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))
