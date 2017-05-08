# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-07 23:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('link', models.CharField(max_length=200, null=True)),
                ('image', models.CharField(max_length=200, null=True)),
                ('meters_walk_to_ov', models.IntegerField(default=0, null=True)),
                ('time_walk_to_ov', models.IntegerField(default=0, null=True)),
                ('time_walk_to_dart', models.CharField(max_length=200, null=True)),
                ('dart_station', models.CharField(max_length=200, null=True)),
                ('dart_for_sorting', models.IntegerField(default=0, null=True)),
            ],
        ),
    ]
