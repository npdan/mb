# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 13:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20170215_0759'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemType',
            fields=[
                ('type_num', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=256)),
            ],
        ),
        migrations.RemoveField(
            model_name='item',
            name='type_name',
        ),
        migrations.AlterField(
            model_name='item',
            name='type_num',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.ItemType'),
        ),
    ]