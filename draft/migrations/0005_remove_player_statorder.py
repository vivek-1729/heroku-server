# Generated by Django 3.0.8 on 2021-03-31 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('draft', '0004_player_statorder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='statOrder',
        ),
    ]