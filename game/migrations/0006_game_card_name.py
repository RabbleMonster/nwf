# Generated by Django 2.0.2 on 2018-04-11 23:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_game_round'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='card_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
    ]
