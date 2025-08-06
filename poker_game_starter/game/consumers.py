import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .poker_logic import create_deck, shuffle_deck, deal_cards
from .redis_handler import load_room, save_room, delete_room

class PokerGameConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_code = self.scope['url_route']['kwargs']['room_code']
        self.room_group_name = f'game_{self.room_code}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

        room = load_room(self.room_code) or {
            'players': [],
            'deck': [],
            'hands': {},
            'community': [],
            'current_turn': 0
        }

        player_id = self.channel_name
        if player_id not in room['players']:
            room['players'].append(player_id)

        save_room(self.room_code, room)
        await self.send_room_update(room)

    async def disconnect(self, close_code):
        room = load_room(self.room_code)
        if not room:
            return

        player_id = self.channel_name
        if player_id in room['players']:
            room['players'].remove(player_id)

        if not room['players']:
            delete_room(self.room_code)
        else:
            save_room(self.room_code, room)
            await self.send_room_update(room)

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        action = data.get('action')

        room = load_room(self.room_code)
        if not room:
            return

        if action == 'start':
            deck = shuffle_deck(create_deck())
            hands, community, deck = deal_cards(deck, len(room['players']))
            room['deck'] = deck
            room['hands'] = dict(zip(room['players'], hands.values()))
            room['community'] = community
            room['current_turn'] = 0
            save_room(self.room_code, room)
            await self.send_room_update(room)

        elif action == 'next':
            room['current_turn'] = (room['current_turn'] + 1) % len(room['players'])
            save_room(self.room_code, room)
            await self.send_room_update(room)

        elif action == 'fold':
            player_id = self.channel_name
            if player_id in room['players']:
                room['players'].remove(player_id)
            if len(room['players']) <= 1:
                winner = room['players'][0] if room['players'] else "No one"
                await self.channel_layer.group_send(self.room_group_name, {
                    'type': 'game_over',
                    'winner': winner
                })
                delete_room(self.room_code)
                return

            save_room(self.room_code, room)
            await self.send_room_update(room)

    async def send_room_update(self, room):
        for player_id in room['players']:
            await self.channel_layer.send(player_id, {
                'type': 'player_update',
                'room': room,
                'your_id': player_id,
            })

    async def player_update(self, event):
        room = event['room']
        your_id = event['your_id']
        await self.send(text_data=json.dumps({
            'action': 'update',
            'players': room['players'],
            'your_hand': room['hands'].get(your_id),
            'community_cards': room['community'],
            'turn': room['current_turn']
        }))

    async def game_over(self, event):
        await self.send(text_data=json.dumps({
            'action': 'game_over',
            'winner': event['winner']
        }))
