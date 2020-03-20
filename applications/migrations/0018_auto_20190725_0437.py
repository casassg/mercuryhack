# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2019-07-25 11:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0017_application_contacted_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='assigned',
        ),
        migrations.AlterField(
            model_name='application',
            name='contacted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contacted_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
