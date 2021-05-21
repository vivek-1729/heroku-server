import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nba.settings")
import django
django.setup()

from draft.models import Player

for player in Player.objects.all():
    player.allegiance = 'Unpicked'
    player.save()