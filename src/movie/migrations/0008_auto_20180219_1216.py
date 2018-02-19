# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-19 20:16
from __future__ import unicode_literals

from django.db import migrations, models
import movie.validators


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_auto_20180219_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='studio',
            field=models.CharField(default='Studio Ghibli', max_length=120, validators=[movie.validators.validate_studio_capital]),
        ),
    ]
