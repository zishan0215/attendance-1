# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-05 12:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panels', '0002_auto_20160505_1219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='password',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='username',
        ),
    ]
