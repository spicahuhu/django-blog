# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-01 07:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='created_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='创建时间'),
        ),
    ]
