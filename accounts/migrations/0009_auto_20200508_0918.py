# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-05-08 09:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200507_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(blank=True, default='2000-12-31', null=True),
        ),
    ]