# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0008_auto_20171028_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='land',
            name='approve_date',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]