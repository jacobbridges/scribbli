# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 22:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteapi', '0003_auto_20170220_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alphainvitation',
            name='date_expires',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 21, 22, 15, 51, 651428), verbose_name='date expires'),
        ),
        migrations.AlterField(
            model_name='alphainvitation',
            name='unik',
            field=models.CharField(max_length=36),
        ),
    ]
