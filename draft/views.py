import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nba.settings")
import django
django.setup()
from django.shortcuts import render
from .models import Player
# Create your views here.
#first_pick_name = input('Name of person with first draft pick: ')
first_pick_name = 'Billiam'
def index(request):
    return render(request, 'index.html')

def draft(request, name):
    possibleStats = ["points", "assists", "totalRebounds","blocks", "threePointsMade", "fouls", "freeThrowsMade"]
    allStats = [Player.objects.filter(stat=x) for x in possibleStats]
    statOrder = list(range(len(allStats)))
    players = list(zip(allStats,statOrder))
    #TODO: Only show the unpicked players so if someone reloads then only the unpicked players will be there
    # players = Player.objects.filter(stat="points")
    return render(request, 'draft.html', {'players':players, 'person':name, 'first': first_pick_name})
#docker run -p 6379:6379 -d redis:5