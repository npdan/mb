# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20170215_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='active',
            field=models.PositiveIntegerField(choices=[(1, 'Active'), (2, 'Inactive'), (3, 'Maybe')], default=1),
        ),
    ]