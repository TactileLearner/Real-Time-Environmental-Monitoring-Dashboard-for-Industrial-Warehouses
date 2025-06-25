

import json
import asyncio
import random
from channels.generic.websocket import AsyncWebsocketConsumer

class SensorDataConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('sensor_data_group', self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('sensor_data_group', self.channel_name)

    async def send_data(self, event):
        await self.send(text_data=json.dumps(event['data']))



class DataConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        while True:
            temperature = round(random.uniform(20, 30), 2)
            humidity = round(random.uniform(40, 60), 2)
            await self.send(text_data=json.dumps({
                'temperature': temperature,
                'humidity': humidity
            }))
            await asyncio.sleep(2)  # Push new data every 2 seconds