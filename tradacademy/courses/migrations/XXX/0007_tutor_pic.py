# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-13 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_daterange'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='pic',
            field=models.ImageField(default='', upload_to='images/tutors'),
            preserve_default=False,
        ),
    ]