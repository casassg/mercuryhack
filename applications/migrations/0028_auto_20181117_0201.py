# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-11-17 02:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0027_auto_20181117_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='degree',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='application',
            name='major',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
