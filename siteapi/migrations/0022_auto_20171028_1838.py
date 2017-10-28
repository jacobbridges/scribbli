# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-28 18:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siteapi', '0021_auto_20171001_0507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='storys', to='siteapi.StoryStatus'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='story',
            name='tags',
            field=models.ManyToManyField(related_name='storys', to='siteapi.StoryTag'),
        ),
    ]