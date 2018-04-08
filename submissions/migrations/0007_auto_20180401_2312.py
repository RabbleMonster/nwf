# Generated by Django 2.0.2 on 2018-04-02 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0006_auto_20180306_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magic_card',
            name='card_name',
            field=models.CharField(default='NRHEC', max_length=256),
        ),
        migrations.AlterField(
            model_name='magic_card',
            name='card_type',
            field=models.CharField(choices=[('Enchantment', 'Enchantment'), ('Atifact', 'Artifact'), ('Creature', 'Creature'), ('Land', 'Land'), ('Planeswalker', 'Planeswalker')], max_length=5),
        ),
    ]
