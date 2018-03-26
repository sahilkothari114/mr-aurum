# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-24 11:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jmms', '0017_cutting_phase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cutting_phase',
            name='lost_weight',
        ),
        migrations.AddField(
            model_name='cutting_phase',
            name='receive_weight',
            field=models.FloatField(default=0.0, verbose_name='Receive Weight'),
        ),
        migrations.AlterField(
            model_name='cutting_phase',
            name='other_cost',
            field=models.PositiveIntegerField(verbose_name='Other Cost'),
        ),
    ]