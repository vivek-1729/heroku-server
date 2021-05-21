import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nba.settings")
import django
django.setup()


from draft.models import Player
from top25 import getPlayer


#Player.objects.all().delete()

possibleStats = ["points", "assists", "totalRebounds","blocks", "threePointsMade", "fouls", "freeThrowsMade"]

statOrder = 0 
for stat in possibleStats:
    players = getPlayer(stat)
    j = 1
    statOrder += 1
    for name, team in players.items():
        p1 = Player(name = name, index = j, allegiance = 'Unpicked', team = team, stat = stat)
        p1.save()
        j+=1


'''
p1 = Player(name='Tacko Bell', index='5', team = 'Unpicked')  
p1.save()
'''


