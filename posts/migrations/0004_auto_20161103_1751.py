# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-03 17:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20161102_1212'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inves',
            old_name='investigacion',
            new_name='linea_de_investigacion',
        ),
    ]
