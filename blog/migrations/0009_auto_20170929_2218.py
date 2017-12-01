# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-29 22:18
from __future__ import unicode_literals

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20170929_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='taggs',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]