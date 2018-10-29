# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-10-27 18:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0012_auto_20181027_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='race',
            field=models.CharField(choices=[('NA', 'Prefer not to answer'), ('American Indian or Alaskan Native', 'American Indian or Alaskan Native'), ('Asian / Pacific Islander', 'Asian / Pacific Islander'), ('Black or African American', 'Black or African American'), ('Hispanic', 'Hispanic'), ('White / Caucasian', 'White / Caucasian'), ('O', 'Multiple ethnicity / Other (Please Specify)')], default='NA', max_length=100),
        ),
        migrations.AlterField(
            model_name='application',
            name='graduation_year',
            field=models.IntegerField(choices=[(2018, '2018'), (2019, '2019'), (2020, '2020'), (2021, '2021'), (2022, '2022'), (2023, '2023'), (2024, '2024'), (2025, '2025')], default=2018),
        ),
    ]
