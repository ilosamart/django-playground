# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 12:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='task',
            table='tasks',
        ),
    ]
