# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-03 16:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.CharField(max_length=466, primary_key=True, serialize=False),
        ),
    ]
