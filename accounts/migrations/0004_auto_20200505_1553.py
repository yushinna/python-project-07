# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2020-05-05 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200505_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='no-image.png', upload_to='images'),
        ),
    ]
