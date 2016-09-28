# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-27 19:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pastebin', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paste',
            old_name='paste',
            new_name='code',
        ),
        migrations.AlterField(
            model_name='paste',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='paste',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(7)),
        ),
    ]