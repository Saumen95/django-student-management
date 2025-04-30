import json
from channels.generic.websocket import AsyncWebsocketConsumer

class NoteConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        """
        Establishes the WebSocket connection and adds the connection to the
        relevant room group based on the note_id in the URL.
        """
        self.note_id = self.scope['url_route']['kwargs']['note_id']
        self.room_group_name = f'note_{self.note_id}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):

        """
        Receive message from WebSocket, deserializes the message and broadcasts it
        to the room group.

        :param text_data: The message sent from the WebSocket client.
        """
        data = json.loads(text_data)
        # Broadcast message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'note_edit',
                'message': data['message']
            }
        )

    # Receive message from room group
    async def note_edit(self, event):
        """
        Receive message from room group and send to WebSocket.

        :param event: Dict containing keys: `type` and `message`.
        :type event: dict
        """
        message = event['message']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
