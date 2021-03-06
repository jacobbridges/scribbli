# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-30 03:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siteapi', '0012_auto_20170430_0229'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('slug', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('is_closed', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='date modified')),
            ],
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('slug', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('is_region', models.BooleanField()),
                ('is_public', models.BooleanField()),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='date modified')),
                ('background', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='siteapi.UploadedImage')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destinations', related_query_name='destination', to='siteapi.Writer')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destinations', related_query_name='destination', to='siteapi.Destination')),
                ('thumbnail', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='siteapi.UploadedImage')),
                ('world', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destinations', related_query_name='destination', to='siteapi.World')),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField()),
                ('is_public', models.BooleanField()),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='date modified')),
                ('characters', models.ManyToManyField(to='siteapi.Character')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stories', related_query_name='story', to='siteapi.Writer')),
            ],
        ),
        migrations.CreateModel(
            name='StoryPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='date modified')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', related_query_name='post', to='siteapi.Chapter')),
                ('characters', models.ManyToManyField(related_name='in_posts', related_query_name='in_post', to='siteapi.Character')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='story_posts', related_query_name='story_post', to='siteapi.Writer')),
                ('pov', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', related_query_name='post', to='siteapi.Character')),
            ],
        ),
        migrations.CreateModel(
            name='StoryStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='date modified')),
            ],
        ),
        migrations.CreateModel(
            name='StoryTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='date modified')),
            ],
        ),
        migrations.AddField(
            model_name='story',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='status', related_query_name='status', to='siteapi.StoryStatus'),
        ),
        migrations.AddField(
            model_name='story',
            name='tag',
            field=models.ManyToManyField(related_name='tags', related_query_name='tag', to='siteapi.StoryTag'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chapters', related_query_name='chapter', to='siteapi.Destination'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chapters', related_query_name='chapter', to='siteapi.Writer'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='story',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chapters', related_query_name='chapter', to='siteapi.Story'),
        ),
        migrations.AlterUniqueTogether(
            name='destination',
            unique_together=set([('name', 'world', 'slug')]),
        ),
        migrations.AlterUniqueTogether(
            name='chapter',
            unique_together=set([('name', 'story', 'slug')]),
        ),
    ]
