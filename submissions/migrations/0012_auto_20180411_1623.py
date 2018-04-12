# Generated by Django 2.0.2 on 2018-04-11 23:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0011_remove_magic_card_card_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='magic_card',
            name='card_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='magic_card',
            name='card_color',
            field=models.CharField(choices=[('U', 'Blue'), ('R', 'Red'), ('W', 'White'), ('B', 'Black'), ('G', 'Green')], max_length=15),
        ),
        migrations.AlterField(
            model_name='magic_card',
            name='card_type',
            field=models.CharField(choices=[('Enchantment', 'Enchantment'), ('Atifact', 'Artifact'), ('Creature', 'Creature'), ('Land', 'Land'), ('Planeswalker', 'Planeswalker')], max_length=15),
        ),
    ]
