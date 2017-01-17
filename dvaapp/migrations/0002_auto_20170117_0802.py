# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-17 08:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='video',
            name='frames',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='video',
            name='length_in_seconds',
            field=models.IntegerField(default=0),
        ),
    ]
