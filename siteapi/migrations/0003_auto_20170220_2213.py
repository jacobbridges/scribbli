# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 22:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteapi', '0002_auto_20170220_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alphainvitation',
            name='date_expires',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 21, 22, 13, 59, 165072), verbose_name='date expires'),
        ),
    ]
