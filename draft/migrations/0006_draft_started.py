# Generated by Django 3.1.2 on 2021-05-15 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draft', '0005_remove_player_statorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='draft_started',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('draftStarted', models.BooleanField(verbose_name=False)),
            ],
        ),
    ]
