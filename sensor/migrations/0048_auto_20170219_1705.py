# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0047_remove_rawdata_string_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawdata',
            name='status',
            field=models.IntegerField(choices=[(0, b'Valid'), (3, b'Value out of range'), (5, b'Sensor offline')], default=0),
        ),
    ]
