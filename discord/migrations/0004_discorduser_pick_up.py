# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-05-11 19:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discord', '0003_discorduser_stickers'),
    ]

    operations = [
        migrations.AddField(
            model_name='discorduser',
            name='pick_up',
            field=models.BooleanField(default=False),
        ),
    ]
