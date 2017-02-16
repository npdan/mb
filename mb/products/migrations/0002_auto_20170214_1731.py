# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 22:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='active',
            field=models.PositiveIntegerField(choices=[(1, 'Freshman'), (2, 'Sophomore'), (3, 'Junior')], default=1),
        ),
        migrations.AddField(
            model_name='item',
            name='available',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='cat_name',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now, max_length=256),
        ),
        migrations.AddField(
            model_name='item',
            name='name',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AddField(
            model_name='item',
            name='size_value',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='stock_qty',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='type_name',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AddField(
            model_name='item',
            name='type_num',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='vintage',
            field=models.CharField(default='', max_length=256),
        ),
    ]
