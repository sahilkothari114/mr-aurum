# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-16 16:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jmms', '0034_hallmark_verification'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cutting_phase',
            unique_together=set([('jewellery_id', 'cutter_id')]),
        ),
    ]
