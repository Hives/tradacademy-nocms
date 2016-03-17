# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-17 01:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_squashed_0011_remove_venue_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='gmap_lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='venue',
            name='gmap_lng',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='venue',
            name='gmap_zoom',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]