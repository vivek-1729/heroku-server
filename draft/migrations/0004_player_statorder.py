# Generated by Django 3.0.8 on 2021-03-31 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draft', '0003_auto_20210331_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='statOrder',
            field=models.CharField(default='null', max_length=10),
        ),
    ]