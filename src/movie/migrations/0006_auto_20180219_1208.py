# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-19 20:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_auto_20180219_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(blank=True, max_length=120, unique=True),
        ),
    ]
