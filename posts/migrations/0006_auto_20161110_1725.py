# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-10 17:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20161110_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inves',
            name='celular',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='inves',
            name='ext',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='inves',
            name='sni',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
    ]