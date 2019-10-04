# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-09-20 23:28
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('logo', models.ImageField(upload_to='offer/logo', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif'])])),
                ('codes', models.FileField(upload_to='offer/codes', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['csv'])])),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('order', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='code',
            name='offer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offer.Offer'),
        ),
        migrations.AddField(
            model_name='code',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
