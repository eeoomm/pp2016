# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 10:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inves',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=140)),
                ('direccion', models.CharField(max_length=140)),
                ('email', models.CharField(max_length=140)),
                ('telefono', models.IntegerField()),
                ('ext', models.IntegerField()),
                ('celular', models.IntegerField()),
                ('investigacion', models.TextField()),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('sni', models.CharField(max_length=140)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
