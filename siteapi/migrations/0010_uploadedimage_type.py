# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteapi', '0009_auto_20170304_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedimage',
            name='type',
            field=models.CharField(default='nothing', max_length=40),
            preserve_default=False,
        ),
    ]