# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-03-13 22:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email')),
                ('name', models.CharField(max_length=255, verbose_name='Full name')),
                ('email_verified', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_director', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('can_review_dubious', models.BooleanField(default=False)),
                ('is_hardware_admin', models.BooleanField(default=False)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('mlh_id', models.IntegerField(blank=True, null=True, unique=True)),
                ('type', models.CharField(choices=[('H', 'Hacker'), ('M', 'Mentor'), ('S', 'Sponsor'), ('V', 'Volunteer'), ('O', 'Organizer')], default='H', max_length=2)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
