# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-09-05 20:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_studentprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StudentProfile',
        ),
    ]
