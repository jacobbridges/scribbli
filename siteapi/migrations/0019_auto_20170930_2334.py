# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-30 23:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siteapi', '0018_auto_20170930_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', related_query_name='child', to='siteapi.Destination'),
        ),
        migrations.AlterField(
            model_name='race',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='races', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='race',
            name='world',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='races', to='siteapi.World'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='race',
            unique_together=set([('name', 'world')]),
        ),
    ]