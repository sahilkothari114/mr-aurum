# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-24 04:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(max_length=255, verbose_name='User Type')),
            ],
        ),
    ]
