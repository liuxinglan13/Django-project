# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 03:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170731_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='timeago',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='modified_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
