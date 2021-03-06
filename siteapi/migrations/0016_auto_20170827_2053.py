# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-27 20:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siteapi', '0015_auto_20170826_2005'),
    ]

    operations = [
        migrations.RenameField(
            model_name='world',
            old_name='system',
            new_name='parent',
        ),
        migrations.RemoveField(
            model_name='uploadedimage',
            name='date_modified',
        ),
        migrations.AddField(
            model_name='world',
            name='avatar',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='world_avatars', to='siteapi.UploadedImage'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='universe',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='universe',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='uploadedimage',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='uploadedimage',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='uploadedimages', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='world',
            name='background',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='world_backgrounds', to='siteapi.UploadedImage'),
        ),
        migrations.AlterField(
            model_name='world',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='world',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='world',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='worlds', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='world',
            name='universe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='worlds', to='siteapi.Universe'),
        ),
        migrations.RemoveField(
            model_name='world',
            name='thumbnail',
        ),
        migrations.AlterUniqueTogether(
            name='world',
            unique_together=set([('name', 'universe')]),
        ),
    ]
