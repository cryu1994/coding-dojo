# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-17 23:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_model', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.CharField(max_length=10),
        ),
    ]
