# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 12:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20170214_1848'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemCategory',
            fields=[
                ('category', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('cat_name', models.CharField(max_length=256)),
            ],
        ),
    ]
