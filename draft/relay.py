import os
import django
django.setup()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nba.settings")

from draft.models import Player


import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class DraftPick(WebsocketConsumer):
    def connect(self):
        # Join draft room
        async_to_sync(self.channel_layer.group_add)(
            'draft',
            self.channel_name
        )

        self.accept()

    # Receive message from WebSocket (recieves name selected from JS backend)
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        increasingDraft = text_data_json['increasingDraft']
        player = text_data_json['player']
        selectedId = text_data_json['id']
        personName = text_data_json['name']
        stat = text_data_json['stat']
        draftOrder = text_data_json['draftOrder']
        if increasingDraft:
            draftOrder += 1
        else: 
            draftOrder -= 1
        
        statNames = ["points", "assists", "totalRebounds","blocks", "threePointsMade", "fouls", "freeThrowsMade"]
        statRange = list(range(len(statNames)))
        #statMap = dict(zip(statRange,statNames))
        statMap = {0: "points", "1": "assists", "2": "totalRebounds", "3": "blocks", "4" : "threePointsMade", "5" : "fouls", "6": "freeThrowsMade"}
        print(statMap)
        print(stat)
        print(type(stat))
        statName = statMap[stat]

        stat_players = Player.objects.filter(stat=statName)
        chosen_player = stat_players.filter(name=player)
        chosen_player.update(allegiance=personName)

        #https://stackoverflow.com/questions/687295/how-do-i-do-a-not-equal-in-django-queryset-filtering
        #Filter out all not unpicked when loading
        #Implement when different stat types can be assigned to player in js


        # Tell update draft room function to update the draft rooms with the latest pick
        async_to_sync(self.channel_layer.group_send)(
            'draft',
            {
                'type': 'update_draft_room',
                'player': player,
                'selectedId': selectedId,
                'name': personName,
                'stat' : stat,
                'draftOrder' : draftOrder
            }
        )

    # Receive draft pick
    def update_draft_room(self, event):
        player = event['player']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'player': player,
            'id': event['selectedId'],
            'name': event['name'],
            'stat': event['stat'],
            'draftOrder' : event['draftOrder']
        }))

#Not needed for now, but may be of use later
# def disconnect(self, close_code):
#     # Leave room group
#     async_to_sync(self.channel_layer.group_discard)(
#         self.room_group_name,
#         self.channel_name
#     )