# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 20:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteapi', '0007_auto_20170222_0611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writer',
            name='email',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='writer',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
