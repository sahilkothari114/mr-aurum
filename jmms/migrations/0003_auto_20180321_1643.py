# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-21 11:13
from __future__ import unicode_literals

from django.db import migrations
import jmms.models


class Migration(migrations.Migration):

    dependencies = [
        ('jmms', '0002_auto_20180321_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rating',
            field=jmms.models.IntegerRangeField(help_text='Rating of the User'),
        ),
    ]