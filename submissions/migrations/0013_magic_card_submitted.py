# Generated by Django 2.0.2 on 2018-04-12 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0012_auto_20180411_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='magic_card',
            name='submitted',
            field=models.BooleanField(default=False),
        ),
    ]