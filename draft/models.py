from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=500)
    index = models.CharField(max_length=100, default='0')
    allegiance = models.CharField(max_length=100, default = 'Billiam')
    team = models.CharField(max_length = 100, default = 'beep boop')
    stat = models.CharField(max_length=100, default = 'null')

    def __str__(self):
        return self.name
