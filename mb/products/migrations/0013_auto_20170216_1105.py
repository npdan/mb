# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20170216_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=6, null=True),
        ),
    ]