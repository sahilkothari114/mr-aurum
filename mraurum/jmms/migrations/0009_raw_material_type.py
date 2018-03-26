# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-24 06:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jmms', '0008_delete_raw_material_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Raw_Material_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_name', models.CharField(max_length=255, verbose_name='Material Name')),
                ('material_purity', models.PositiveIntegerField(verbose_name='Material Name')),
                ('material_current_price', models.PositiveIntegerField(verbose_name='Current Price')),
                ('material_unit', models.PositiveIntegerField(verbose_name='Material Unit')),
            ],
        ),
    ]
