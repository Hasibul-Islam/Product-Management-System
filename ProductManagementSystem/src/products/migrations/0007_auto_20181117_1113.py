# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-17 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20181117_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costing',
            name='total_profit',
            field=models.IntegerField(default=0),
        ),
    ]